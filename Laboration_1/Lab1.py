import os
import nmap
import ipaddress

scanner = nmap.PortScanner()

### Functions
def Print_Main_Menu():
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
                         Scan_all(entered_ips)
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

def Scan_all(ips_to_scan):
     for ip in ips_to_scan:
          ip_str = str(ip)
          print(f"Scanning {ip_str}")
          scanner.scan(hosts=ip_str, arguments='-n -sP -PE -PA21,23,80,3389')
          hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
          for host, status in hosts_list:
               print(host, status)


def Print_Scan_Menu():
     os.system("clear")
     userInput = False
     while not userInput:
          ip_input = input("Enter the IP:s to scan with space between every IP OR one IP range (CIDR):\n")
          input_list = ip_input.split(" ")
          
          ip_list = []
          for ip in input_list:
               try:
                    if "/" in ip:
                         new_range = ipaddress.ip_network(ip)
                         ip_list.append(new_range)
                         break
                    else:
                         new_ip = ipaddress.ip_address(ip)
                         ip_list.append(new_ip)
               except ValueError as e:
                    print(f"{e} and won't be added to the list")

          if len(ip_list) > 0:
               userInput = True
               return ip_list

Print_Main_Menu()
