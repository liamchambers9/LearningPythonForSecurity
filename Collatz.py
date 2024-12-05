'''
Function named collatz() that has one parameter named number

if number is even, then collatz() should print number // 2 and return this value

if number is odd, then collatz() should print and return 3 * number + 1


'''
#Creating my function 
def collatz(number):
    if number % 2 == 0:
        return number //2
    elif number % 2 == 1:
        return 3 * number + 1

'''
write a program that lets the user type in an integer that keeps calling collatz()
on that number until the function returns the value 1.
'''
while True: 
    try: 
        number = int(input("Type your number: "))
        break # if successful, break out of the loop 
    except ValueError: 
        print("You must enter an integer. Try again!")

while number !=1:
    collatz(number)
    number = collatz(number)
    print(number)
