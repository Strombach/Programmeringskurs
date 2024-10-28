import argparse
from sublist3r import main as sublister

HELP_STRING = """
        DomEnus
        Like the latin \"dominus\", meaning \"lord\" or \"master\").
        Is a sub[DOM]ain [ENU]merator using [S]ublist3r.
        """

def main(flags):
    domain = flags.domain
    subdomains = sublister(domain, 20, ports=None, silent=True, verbose=False, savefile=None, enable_bruteforce=False, engines=None)
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

    argparse_args = parser.parse_args()

    main(argparse_args)
