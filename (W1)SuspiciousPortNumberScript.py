"""

Defining the Progam
I want this program to evaluate if a certain port is common,uncommon, or suspicious.

Logic
First, I have to ensure that the user input is valid. I will do so by establishing that a port number has to be an integer between 1 and 65,535. 


Second, I plan to use conditional statements to check the port number against these categories:
   1. Check if the port number belongs to a well-known list of common ports. 
   2. If not, check if it belongs to uncommon but legitimate ports.
   3. If neither, classify it as suspicious. 

        
"""



#Input Handling 
def get_valid_port():
    while True:
        try:
            port = int(input("Enter a port number: "))
            if 1 <= port <= 65535:
                return port
            else:
                print("Please enter a valid port number between 1 and 65,535")
        except ValueError:
            print("This is not a valid integer. Please enter a valid port number")

valid_port = get_valid_port()
print(f"You entered a valid port number: {valid_port}")

# Determining Common, Uncommon, Suspicious             
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3306, 3389,  8080]
suspicious_ports = [137,139,445] 

# Use valid_port from the handling section 
if valid_port in common_ports:
    print("This is a common port.")
elif valid_port in suspicious_ports:
    print("This is a suspicious port.")
else:
    print("This is an uncommon port")
