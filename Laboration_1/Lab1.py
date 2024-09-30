import os
import nmap

scanner = nmap.PortScanner()
userInput = False



scanner.scan(hosts='10.10.10.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
for host, status in hosts_list:
     print(host, status)

# while not userInput:
#     test = scanner.
#     print(test)
#     print("Enter a number in the menu:")
#     print("1. Scan")
#     print("2. Save to file")

#     if input() == "1":
#         print("Option 1")
#     elif input() == "2":
#         print("Option 2")
#     else:
#         print("Not a Valid Option")
