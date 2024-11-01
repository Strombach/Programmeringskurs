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
        self.filterExclude = self.set_filterExclude()
        self.filterInclude = self.set_filterInclude()

    def set_domain(self):
        while True:
            domain = input("Enter a domain: ").strip()

            if not validators.domain(domain):
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
        while True:
            turn_off = input("Turn off silent mode (y or leave empty): ").lower()
            match turn_off:
                case "y":
                    return False
                case "":
                    return True
                case _:
                    print("Not valid. [y] or leave empty")

    def set_verbose(self):
        while True:
            turn_off = input("Turn on verbose mode (y or leave empty): ").lower()
            match turn_off:
                case "y":
                    return True
                case "":
                    return False
                case _:
                    print("Not valid. [y] or leave empty")

    def set_savefile(self):
        # Not implemented here because own solution in domenus script.
        return None

    def set_filterExclude(self):
        while True:
            exclude_words = input("Any specific words to be excluded from the results (comma separated): ").lower().strip().replace(" ", "")

            if exclude_words == "":
                return None
            else:
                return exclude_words

    def set_filterInclude(self):
        if not self.filterExclude:
            while True:
                include_words = input("Any specific words to be included in the results (comma separated): ").lower().strip().replace(" ", "")

                if include_words == "":
                    return None
                else:
                    return include_words

class Webgetter_args:
    def __init__(self):
        self.url = self.set_url()
        self.name = self.set_name()

    def set_url(self):
        while True:
            url = input("Enter a URL: ").strip()

            if not validators.url(url):
                print("Not a valid URL")
                continue
            else:
                return url

    def set_name(self):
        while True:
            name = input("Set name for file/folder, leave empty for \"downloaded\": ").strip()
            return name

class Smuggler_args:
    def __init__(self):
        self.payload = self.set_payload()
        self.htmlfile = self.set_htmlfile()
        self.downloadname = self.set_downloadname()
        self.downloadtagid = self.set_downloadtagid()

    def set_payload(self):
