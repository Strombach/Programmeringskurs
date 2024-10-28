# A file to keep all the args-classes needed to run tools in the main script.

class Crypto_Args:
    def __init__(self, file="", decryptkey=None, encrypt=True, newkey=True, key=None):
        self.file = file
        self.decryptkey = decryptkey
        self.newkey = newkey
        self.encrypt = encrypt
        self.key = key
