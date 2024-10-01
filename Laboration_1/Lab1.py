import os

### Functions
def Print_Menu():
     userInput = False
     while not userInput:
          print("**** Menu ****")
          print("1. Scan")
          print("2. Open File")
          print("3. Exit")
          try:
               user_choice = int(input("Enter a number: "))
               match user_choice:
                    case 1:
                         print("Scan")
                    case 2:
                         print("Open File")
                    case 3:
                         print("Bye!")
                         quit()
          except ValueError:
               os.system("clear")
               print("Not a valid number. Try again")
          else:
               userInput = True
               print(user_choice)


def Scan_all():
     scanner = nmap.PortScanner()

     scanner.scan(hosts='10.10.10.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
     hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
     for host, status in hosts_list:
          print(host, status)

Print_Menu()
