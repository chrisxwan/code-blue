from passlib.apps import custom_app_context as pwd_context

def hash_password(password):
    return pwd_context.encrypt(password)

def verify_password(password1, password2):
    return pwd_context.verify(password1, password2)