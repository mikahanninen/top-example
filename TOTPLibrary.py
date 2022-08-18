import pyotp
from RPA.Robocloud.Secrets import Secrets


class TOTPLibrary:
    def __init__(self, secretname, secretkey):
        secrets = Secrets().get_secret(secretname)
        self.totp = pyotp.TOTP(secrets[secretkey])

    def get_totp(self):
        return self.totp.now()