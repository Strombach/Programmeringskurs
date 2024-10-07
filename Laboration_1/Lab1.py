import os
import nmap
import ipaddress

scanner = nmap.PortScanner()

### Functions
def Save_To_File(data):
     print(data)

def Scan_Ip(ips_to_scan, flags):
     for ip in ips_to_scan:
          ip_str = str(ip)
          print(f"Scanning {ip_str}")
          test = scanner.scan(hosts=ip_str, arguments=flags)
          print(test)

def Nmap_Scan_Menu(ips_to_scan):
     os.system("clear")
     userInput = False
     while not userInput:
          print("What type of scan?")
          print("1. TCP Connect Scan (-sT)")
          print("2. Stealth scan (-sS) !!REQUIRES ROOT!!")
          print("3. Version scan (-sV)")
          print("4. Enter own flags")
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         flags = "-sT"
                    case 2:
                         flags = "-sS"
                    case 3:
                         flags = "-sV"
                    # case 4:
                    
                    case _:
                         raise ValueError
               Scan_Ip(ips_to_scan, flags)
          except ValueError:
               os.system("clear")
               print("Not a valid number. Try again")
     for ip in ips_to_scan:
          print(ip)



def Print_Scan_Menu():
     os.system("clear")
     userInput = False
     while not userInput:
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
               userInput = True
               return ip_list

def Print_Main_Menu():
     os.system("clear")
     userInput = False
     while not userInput:
          print("**** Menu ****")
          print("1. Enter IP:s manually")
          print("2. Exit")
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         print("Enter single or multiple IP:s to scan.")
                         entered_ips = Print_Scan_Menu()
                         Nmap_Scan_Menu(entered_ips)
                    case 2:
                         print("Bye!")
                         quit()
                    case _:
                         raise ValueError
          except ValueError:
               os.system("clear")
               print("Not a valid number. Try again")
          else:
               userInput = True

### Script
Print_Main_Menu()
