import os
import nmap
import ipaddress

### Functions
def print_menu(options, menu_text):
     os.system("clear")
     if menu_text:
          print(menu_text)

     for index, option in enumerate(options):
          print(f"{[index + 1]} {option}")

def Save_To_File(data):
     print(data)

def scan_ips(ips_to_scan, flags):
     scanner = nmap.PortScanner()
     for ip in ips_to_scan:
          ip_str = str(ip)
          print(f"Scanning {ip_str}")
          # test = scanner.scan(hosts=ip_str, arguments=flags)

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
     os.system("clear")
     menu_text = "What type of scan?"
     options = ["TCP Connect Scan (-sT)", "Stealth scan (-sS) !!REQUIRES RUNNING SCRIPT AS ROOT!!", "Version scan (-sV)", "Enter own flags", "Back to main menu"]
     print_menu(options, menu_text)
     
     while True:
          try:
               user_choice = int(input("Enter a number: "))
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
               os.system("clear")
               print_menu(options, menu_text)
               print("Not a valid number. Try again")

def main():
     nmap_flags = ""
     list_of_ips = []
     options = ["Enter IP:s to scan", "Exit"]
     menu_text = "NMAP Scanner"
     print_menu(options, menu_text)
     
     while True:
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         nmap_flags = ask_for_scan()
                         list_of_ips = ask_for_ips()
                         scan_result = scan_ips(list_of_ips, nmap_flags)
                         # TODO Remove this break
                         break
                    case 2:
                         print("Bye!")
                         quit()
                    case _:
                         raise ValueError
               os.system("clear")
               print_menu(options, menu_text)
          except ValueError:
               os.system("clear")
               print_menu(options, menu_text)
               print("Not a valid number. Try again")

### Script
if __name__ == "__main__":
     main()
