def authenticate_user(username: str, password: str):
    return username == "admin" and password == "password"
