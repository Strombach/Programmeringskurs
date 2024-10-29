# A file to keep all the args-classes needed to run tools in the main script.
#TODO: For better code

class Crypto_Args:
    def __init__(self, file="", decryptkey=None, encrypt=True, newkey=True, key=None):
        self.file = file
        self.decryptkey = decryptkey
        self.newkey = newkey
        self.encrypt = encrypt
        self.key = key

class Domenus_Args:

    def __init__(self):
        self.domain = self.set_domain()
        self.threads = self.set_threads
        self.ports = self.set_ports,
        self.silent = self.set_silent
        self.verbose = self.set_verbose
        self.savefile = self.set_savefile
        self.enable_bruteforce = self.set_enable_bruteforce
        self.engines = self.set_engines

    def set_domain(self):
        return "example.com"

    def set_threads(self):
        return 20

    def set_ports(self):
        return None

    def set_silent(self):
        return True

    def set_verbose(self):
        return False

    def set_savefile(self):
        return None

    def set_enable_bruteforce(self):
        return False

    def set_engines(self):
        return None
