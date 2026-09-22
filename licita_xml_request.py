import requests
import json
import xml.etree.ElementTree as ET

from datetime import datetime

response = requests.get('https://contrataciondelsectorpublico.gob.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3.atom')

ns = {
    "atom": "http://www.w3.org/2005/Atom",
    "cbc": "urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2",
    "cac": "urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2",
    "cbc-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2",
    "cac-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2",
}

CPV_TECNOLOGIA = {
    "30",   # Equipos informáticos
    "32",   # Telecomunicaciones
    "48",   # Software
    "72"    # Servicios TI
}

licitaciones = []

if response.status_code == 200:
    

    xml = response.text

    root = ET.fromstring(xml)

    now = datetime.now()

    count = 0

    for entry in root.findall("atom:entry", ns):

        #Filter date
        updated = entry.findtext("atom:updated", namespaces=ns)
        date = datetime.fromisoformat(updated.replace("Z", "+00:00"))

        if date.month != now.month or date.year != now.year:
            continue

        #Filter State
        state = entry.findtext(
                    ".//cbc-place-ext:ContractFolderStatusCode",
                    default="",
                    namespaces=ns
                )

        if state != "PUB":
            continue

        #Filter CPV
        cpv = entry.findtext(
            ".//cac:ProcurementProject/"
            "cac:RequiredCommodityClassification/"
            "cbc:ItemClassificationCode",
            namespaces=ns
        )

        #if cpv[:2] not in CPV_TECNOLOGIA:
        #    continue 

        title = entry.findtext("atom:title", default="", namespaces=ns)
        expediente = entry.findtext(
                        ".//cbc:ContractFolderID",
                        "",
                        ns
                    )
        count += 1

        print(f"{count}. - {title}")
        print(f"   Public date: {updated}")
        print(f"  CPV: {cpv}")

        lic = {
            "expediente": expediente,
            "titulo": title,
            "estado": state,
            "fecha_publicacion": updated,
            "cpv": cpv
        }

        licitaciones.append(lic)

        #with open("licitacion_filtrada.xml", "w", encoding="utf-8") as f:
        #    f.write(response.text)

    with open("licitaciones_filtradas.json", "w", encoding="utf-8") as f:
                json.dump(
                licitaciones,
                f,
                ensure_ascii=False,
                indent=4
            )
else:
    print(f"Error al obtener datos: {response.status_code}")