import pyotp
from RPA.Robocorp.Vault import Vault


class TOTPLibrary:
    def __init__(self, secretname, secretkey):
        secrets = Vault().get_secret(secretname)
        self.totp = pyotp.TOTP(secrets[secretkey])

    def get_totp(self):
        return self.totp.now()
