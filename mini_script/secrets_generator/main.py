import secrets

long:int = int(input("Long of generated password: "))
print(f"Your token is\n{secrets.token_urlsafe(long)}")
