import argparse
from sublist3r import main as sublister

HELP_STRING = """
        DomEnus
        Like the latin \"dominus\", meaning \"lord\" or \"master\").
        Is a sub[DOM]ain [ENU]merator using [S]ublist3r.
        """

def main(flags):
    subdomains = sublister(flags.domain, 20, ports=None, silent=True, verbose=False, savefile=None, enable_bruteforce=False, engines=None)
    print("Subdomains found:")
    for subdomain in subdomains:
        print(subdomain)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="DomEnus",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description= HELP_STRING
)

    parser.add_argument("-d","--domain", help="The domain[s] to enumerate.")

    args = parser.parse_args()

    main(args)
else:
    import os
    import time
    from .args import Domenus_Args

    def domenus():

        args = Domenus_Args()

        main(args)
