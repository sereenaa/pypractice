# ask the user for a number 
# tell the user whether the number is even or odd 

## extra 
## if the number is a multiple of 4, print a different message 

no = int(input("Give me a number: "))
if (no%4 == 0) :
    print("The number is a multiple of 4") 
elif (no%2 == 0) :
    print("The number is even") 
else: 
    print("The number is odd") 

