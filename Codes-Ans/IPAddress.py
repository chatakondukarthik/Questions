# Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".
# Input : address = "1.1.1.1"
# Output : "1[.]1[.]1[.]1"

ip = input("Enter the ip adress to be shown in different way : ")
ip = ip.replace('.', '[.]')
print(ip)
