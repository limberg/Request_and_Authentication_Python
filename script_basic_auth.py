import base64

def decode_basic_auth(auth_header: str) -> tuple[str,str]:
    encoded = auth_header.split(" ", 1)[1] 
    decoded_bytes = base64.b64decode(encoded)
    decoded_str = decoded_bytes.decode("utf-8")

    # Separar usuario y contrasenia
    username, password = decoded_str.split(":", 1)
    return username, password


header = "Basic TGltYmVyZzpGZWJyZXJvMTQ="
user, pwd = decode_basic_auth(header)
print(f"Usuario: {user}, Contrasenia: {pwd}")

