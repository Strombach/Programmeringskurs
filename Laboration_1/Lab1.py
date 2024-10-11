import os
import nmap
import ipaddress
import json
from datetime import datetime

### Functions
def print_menu(options, menu_text, clear_screen):
     if clear_screen:
          os.system("clear")
     if menu_text:
          print(menu_text)

     for index, option in enumerate(options):
          print(f"{[index + 1]} {option}")

def formatting():
     while True:
          try:
               formatted = input("Formatted? [y]es or [n]o: ").lower()
               match formatted:
                    case "y":
                         return 4
                    case "n":
                         return None
                    case _:
                         raise ValueError
          except ValueError:
               print("[y]es or [n]o")

def save_to_file(data):
     options = ["As txt","As json", "Go back"]
     menu_text = "Save file"
     indent = 0
     print_menu(options, menu_text, True)
     while True:
          todays_date = datetime.today()
          try:
               save_or_print = int(input("What type? "))
               match save_or_print:
                    case 1:
                         filetype = "txt"
                         indent = formatting()
                    case 2:
                         filetype = "json"
                         indent = formatting()
                    case 3:
                         ask_if_print_or_save(data)
                    case _:
                         raise ValueError
               with open(f'{todays_date}.{filetype}', 'w') as file:
                    print(f"Saving to file {file.name}")
                    json.dump(data,file, indent=indent)
               break
          except ValueError:
               print("Not a valid number. Try again")

def ask_if_print_or_save(data):
     options = ["Print to here in terminal","Save to file", "Back to main menu"]
     menu_text = "Results are in, what do you want to do?"
     print_results = False
     while True:
          try:
               if print_results:
                    print_results = False
                    print_menu(options, menu_text, True)
                    print(data)
               else:
                    print_menu(options, menu_text, True)
               save_or_print = int(input("Enter an option: "))
               match save_or_print:
                    case 1:
                         print_results = True
                    case 2:
                         save_to_file(data)
                    case 3:
                         main()
                    case _:
                         raise ValueError
          except ValueError:
               print("Not a valid number. Try again")

def scan_ips(ips_to_scan, flags):
     scanner = nmap.PortScanner()
     results = dict()
     for ip in ips_to_scan:
          ip_str = str(ip)
          print(f"Scanning {ip_str}...")
          result = scanner.scan(hosts=ip_str, arguments=flags)
          results["command_line"] = result["nmap"]["command_line"]
          results[f"{ip_str}_results"] = result["nmap"]["scanstats"] | result["scan"]
     return results

def ask_for_ips():
     user_input = False
     
     while not user_input:
          ip_input = input("Enter the IP:s to scan with space between every IP or IP-range (CIDR):\n")
          input_list = ip_input.split(" ")
          
          ip_list = []
          for ip in input_list:
               try:
                    if "/" in ip:
                         new_range = ipaddress.ip_network(ip)
                         ip_list.append(new_range)
                    else:
                         new_ip = ipaddress.ip_address(ip)
                         ip_list.append(new_ip)
               except ValueError as e:
                    os.system("clear")
                    print(f"{e} and won't be added to the list")
          if len(ip_list) > 0:
               user_input = True
               return ip_list

def ask_for_scan():
     menu_text = "What type of scan?"
     options = ["TCP Connect Scan (-sT)", "Stealth scan (-sS) !!REQUIRES RUNNING SCRIPT AS ROOT!!", "Version scan (-sV)", "Enter own flags", "Back to main menu"]
     print_menu(options, menu_text, True)
     while True:
          try:
               user_choice = int(input("Choose arguments: "))
               match user_choice:
                    case 1:
                         flags = "-sT"
                    case 2:
                         flags = "-sS"
                    case 3:
                         flags = "-sV"
                    case 4:
                         flags = input("Enter flags as you would in Nmap: ")
                    case 5:
                         break
                    case _:
                         raise ValueError
               if len(flags) > 1:
                    return flags
               break
          except ValueError:
               print_menu(options, menu_text,True)
               print("Not a valid number. Try again")

def main():
     nmap_flags = ""
     list_of_ips = []
     options = ["Enter IP:s to scan", "Exit"]
     menu_text = "NMAP Scanner"
     print_menu(options, menu_text, True)
     
     while True:
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         nmap_flags = ask_for_scan()

                         if nmap_flags:
                              list_of_ips = ask_for_ips()
                              scan_result = scan_ips(list_of_ips, nmap_flags)
                              ask_if_print_or_save(scan_result)
                         else:
                              pass
                    case 2:
                         print("Bye!")
                         quit()
                    case _:
                         raise ValueError
               print_menu(options, menu_text, True)
          except ValueError:
               print_menu(options, menu_text, True)
               print("Not a valid number. Try again")

### Script
if __name__ == "__main__":
     main()
