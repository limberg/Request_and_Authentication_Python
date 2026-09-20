import jwt

def decode_jwt(token:str) -> dict:
    return jwt.decode(token, options={"verify_signature": False}) # No importa la signature (firma)

jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." \
            "eyJ1c2VyX2lkIjoxLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3MDAwMDAwMDB9." \
            "ZmljdGl2ZV9maXJtYV9qd3Rfc2VjcmV0XzEyMzQ1" # esta ultima parte seria la signature pero no se mostrara en nuestro ejemplo

payload = decode_jwt(jwt_token)
print("Contenido del JWT:")
for k,v in payload.items():
    print(f"{k}: {v}")