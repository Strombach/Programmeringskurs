import argparse
from sublist3r import main as sublister

HELP_STRING = """
        DomEnus
        Like the latin \"dominus\", meaning \"lord\" or \"master\").
        Is a sub[DOM]ain [ENU]merator using [S]ublist3r.
        """

def save_to_file():
    print("Saving...")

def print_results(result):
    print("\nSubdomains found:\n")
    for subdomain in result:
        print(subdomain)

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
    results = sublister(
    domain=flags.domain,
    threads=flags.threads,
    ports=flags.ports,
    silent=flags.silent,
    verbose=flags.verbose,
    savefile=None,
    enable_bruteforce=False,
    engines=None)

    if flags.filterInclude or flags.filterExclude and len(results) > 0:
        if flags.filterExclude:
            filtered_results = filter_result(flags.filterExclude, results, include=False)
        else:
            filtered_results = filter_result(flags.filterInclude, results, include=True)

        if len(filtered_result) < 1 and len(results) > 0:
            print("No filtered results found but there are other subdomains")

            while True:
                see_other_results = input("Do you want to see them? [y/n] ").lower()
                if see_other_results == "y":
                    print_results(results)
                    break
                elif see_other_results == "n":
                    break
                else:
                    print("Not valid input: Only [y] or [n] is accepted. ")
    elif len(results) > 0:
        print_results(results)
    else:
        print("No subdomains found...")
        input("Press Enter to go back to main menu...")

    if "filtered_results" in locals() and len(filtered_results) > 0:
        input("Save filtered results to file?")

    if "results" in locals() and len(results) > 0:
        input("Save all results to file?")

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
