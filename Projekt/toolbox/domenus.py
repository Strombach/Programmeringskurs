import argparse
from sublist3r import main as sublister

HELP_STRING = """
        DomEnus
        Like the latin \"dominus\", meaning \"lord\" or \"master\").
        Is a sub[DOM]ain [ENU]merator using [S]ublist3r.
        """

def save_to_file():
    print("Saving...")

def filter_result(filter_input, subdomains, include = False):
    filter_list = filter_input.replace(" ","").lower().split(",")

    filtered_subdomains = []

    for subdomain in subdomains:
        for filter_text in filter_list:
            if filter_text in subdomain.lower() and include:
                filtered_subdomains.append(subdomain)
            elif not filter_text in subdomain and not include:
                filtered_subdomains.append(subdomain)

    return filtered_subdomains

def main(flags):
    print("Searching for subdomains...")
    result = sublister(
    domain=flags.domain,
    threads=flags.threads,
    ports=flags.ports,
    silent=flags.silent,
    verbose=flags.verbose,
    savefile=None,
    enable_bruteforce=False,
    engines=None)

    if flags.filterInclude or flags.filterExclude:
        if flags.filterExclude:
            filtered_result = filter_result(flags.filterExclude, result, include=False)
        else:
            filtered_result = filter_result(flags.filterInclude, result, include=True)
        print("\nSubdomains found:\n")
        for subdomain in filtered_result:
            print(subdomain)
    else:
        print("\nSubdomains found:\n")
        for subdomain in result:
            print(subdomain)

    input("\nPress Enter to continue...")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="DomEnus",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description= HELP_STRING
)

    # Mandatory
    parser.add_argument("-d","--domain", help="The domain[s] to enumerate.")

    # Optional to change
    parser.add_argument("-fi", "--filterInclude", help="Comma separated list of words to search for and include.")
    parser.add_argument("-fe", "--filterExclude", help="Comma separated list of words to search for and exclude.")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (Default: 10).")
    parser.add_argument("-p", "--ports", default=None, help="List of ports, comma separated.")
    parser.add_argument("-s", "--silent", action="store_true", help="Set to turn Silent mode on")
    parser.add_argument("-v", "--verbose", action="store_true", help="Set to turn verbose mode on")

    args = parser.parse_args()

    main(args)
else:
    import os
    import time
    from .args import Domenus_Args

    def domenus():

        args = Domenus_Args()

        main(args)
