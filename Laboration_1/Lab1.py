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
     print(ips_to_scan)
     # scanner.scan(hosts='10.10.10.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
     # hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
     # for host, status in hosts_list:
     #      print(host, status)

def Print_Scan_Menu():
     os.system("clear")
     userInput = False
     while not userInput:
          try:
               ips=input("Enter the ips to scan with space between every ip:\n")
               userInput = True
               return ipaddress.ip_address(ips)
          except:
               print("Failed to read IP")

Print_Main_Menu()
