'''
Objective is to write a program that simulates scanning a range of ports on a target IP address.

1. Ask the user for a target IP address (simple input for now, no need to validate its format)

2. Ask the user for a starting port and ending port. Add input validation to ensure these are integers an within the range 1-65535

3. Loop through the specified range of ports.

            if port number is divisible by 3, print "Port [number]: Open"

            if port number is divisible by 5, print "Port [number]: Closed"

            if port number is divisible by both 3 and 5, print "Port [number]: Filtered"

            Otherwise, print "Port [number]: Unknown"

4. Use a function scan_port(port) to handle the logic for whether a port is open, closed, filtered, or unknown.
'''


targetIP = input("What is your target IP address: ")

while True:
    try: 
        startingPort = int(input("What is the starting port you would like to scan?"))
        if 1 <= startingPort <= 65535: #Check the range
         break
        else:
           print("Port must be between 1 and 65535. Try again.")
    except ValueError:
        print("You must enter an integer. Try again")


while True:
    try:
        endingPort = int(input("What is the port you'd like to end with?"))
        if 1 <= endingPort <= 65535:
            break
        else:
            print("Port must be between 1 and 65535. Try again.")
    except ValueError:
        print("You must enter an integer. Try again")
    

def scanPort(port):
    if port % 3 == 0 and port % 5 == 0:
        return "Filtered"
    elif port % 3 == 0:
        return "Open"
    elif port % 5 == 0:
        return "Closed"

for port in range(startingPort, endingPort + 1):
    status = scanPort(port)
    print(f"Port {port}: {status}")
