## Build a phone book program that receives the phone number, and returns the name of the owner. 

# You can follow the table below:
# | Name    | Number      |
# | -------- | ---------- |
# | Amal     | 0531511811 |
# | Mohammed | 0551511231 |
# | Khadijah | 0531511113 |
# | Abdullah  | 0541511123 |
# | Rawan    | 0591511128 |
# | Faisal   | 0581521129 |
# | Layla    | 0563513453 |


# - Ask the user to enter the phone number using input
# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# - If the number is less or more than 10 numbers, print "This is invalid number".
# - If the number contains letters or symbols, print "This is invalid number".
PhoneDict = {"0531511811":"Amal",
             "0551511231":"Mohammed",
             "0531511113":"Khadijah",
             "0541511123":"Abdullah",
             "0591511128":"Rawan",
             "0581521129":"Faisal",
             "0563513453":"Layla"}
def GetPhoneNumber():
    """
    GetPhoneNumber() let you search for Name of Input phone number 
    just Call GetPhoneNumber()
    and you will see steps ... 
    """
    Number = input("Please Enter Phone Number : ")
    if((False in [Letter.isdigit() for Letter in Number ])):
        print() 
        print("This is invalid number __ number contains letters or symbols  [ " + ' , '.join([Letter for Letter in Number if Letter.isdigit() == False ]) + ' ] ')
        print()
    elif(len(Number) != 10):
        print()
        print("This is invalid number __ len(Number) != 10")
        print()
    else:
        if Number not in PhoneDict.keys():
            print()
            print("Sorry, the number is not found") 
            print()
        else: 
            print()
            print(f"The owner of this {Number} is :  {PhoneDict[Number]}") 
            print()

GetPhoneNumber()