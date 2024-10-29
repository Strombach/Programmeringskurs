# A file to keep all the args-classes needed to run tools in the main script.
#TODO: For better code

import os
import validators

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
        self.threads = self.set_threads()
        self.ports = self.set_ports()
        self.silent = self.set_silent()
        self.verbose = self.set_verbose()
        self.savefile = self.set_savefile()
        self.enable_bruteforce = self.set_enable_bruteforce()
        self.engines = self.set_engines()

    def set_domain(self):
        while True:
            domain = input("Enter a domain: ").strip()

            if not validators.domain(domain):
                os.system("clear")
                print("Not a valid domain")
                continue
            else:
                return domain

    def set_threads(self):
        DEFAULT_THREADS = 10

        while True:
            try:
                threads = input(f"Enter number of threads (Leave empty for {DEFAULT_THREADS}): ").strip()

                if threads == "":
                    return DEFAULT_THREADS
                else:
                    return int(threads)
            except ValueError:
                print("Not a number...")

    def set_ports(self):
        while True:
            try:
                ports = input("Specific ports, comma-separated (Leave emtpy for None): ").strip().replace(" ", "")
                if ports == "":
                    return None
                else:
                    port_strings = ports.split(",")

                    for port_str in port_strings:
                        if port_str.isdigit():
                            port = int(port_str)
                            if not 0 <= port <=65535:
                                raise ValueError(f"Invalid port: {port}")
                        else:
                            raise ValueError(f"{port_str} is not a number")
                    return ports

            except ValueError as err:
                print(err)

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
