import os
import nmap
import ipaddress

scanner = nmap.PortScanner()

### Functions
def print_menu(options, menu_text):
     if menu_text:
          print(menu_text)

     for index, option in enumerate(options):
          print(f"{[index + 1]} {option}")

def Save_To_File(data):
     print(data)

def Scan_Ip(ips_to_scan, flags):
     for ip in ips_to_scan:
          ip_str = str(ip)
          print(f"Scanning {ip_str}")
          test = scanner.scan(hosts=ip_str, arguments=flags)
          print(test)

def Nmap_Scan_Menu():
     options = ["TCP Connect Scan (-sT)", "Stealth scan (-sS) !!REQUIRES RUNNING SCRIPT AS ROOT!!", "Version scan (-sV)", "Enter own flags", "Back to main menu"]
     userInput = False
     while not userInput:
          os.system("clear")
          print_menu(options, "NMAP Scanner")
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
               # Scan_Ip(ips_to_scan, flags)
          except ValueError:
               os.system("clear")
               print("Not a valid number. Try again")
          print_menu(options, "NMAP Scanner")
     for ip in ips_to_scan:
          print(ip)

def Print_Scan_Menu():
     os.system("clear")
     user_input = False
     while not user_input:
          ip_input = input("Enter the IP:s to scan with space between every IP or IP range (CIDR):\n")
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

def Print_Main_Menu():
     options = ["Enter Ip to scan", "Exit"]
     # os.system("clear")
     
     while True:
          os.system("clear")
          print_menu(options, "NMAP Scanner")
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         print("Enter single or multiple IP:s to scan.")
                         Nmap_Scan_Menu()
                    case 2:
                         print("Bye!")
                         quit()
                    case _:
                         raise ValueError
          except ValueError:
               os.system("clear")
               print("Not a valid number. Try again")
          print_menu(options, "NMAP Scanner")

### Script
Print_Main_Menu()
