import hashlib
import os
from user_registration import UserSchema

class Authentication:
    def __init__(self):
        self.users = UserSchema()

    def hash_password(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + key

    def verify_password(self, stored_password, provided_password):
        salt = stored_password[:32]
        stored_key = stored_password[32:]
        new_key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return stored_key == new_key

    def authenticate_user(self, email, password):
        user = self.users.get_user(email)
        if user and self.verify_password(user['password'], password):
            return True, "login_success"
        return False, "login_failed"

    def two_factor_authentication(self, user, provided_token):
        if user['2fa_token'] == provided_token:
            return True, "2fa_success"
        return False, "2fa_failed"
