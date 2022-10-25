Username= input("Greetings!, Please enter your name : ")
print("Hello", Username,"!", "Please select the calculation, Factorial, Palindrome, Fibonnaci or a table? ")
usercalculator= input("My preffered calculator will be : ")

if usercalculator == "Fibonacci":
    fiboseries = int(input("Please enter fibonacci ending series :- "))
    a = 0
    b = 1
    c = 0
    print("Your results are - ")
    while c<fiboseries :
        print(c)
        a= b
        b= c
        c= a+b 
if usercalculator == "Factorial":
    num = int(input("Enter a number: "))    
    factorial = 1    
    if num < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif num == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1,num + 1):    
            factorial = factorial*i    
        print("The factorial of",num,"is",factorial) 
if usercalculator == "Palindrome":
    StringInput = str(input("Please enter your word :"))

    ReverseS = ""
    for i in StringInput:
     ReverseS = i + ReverseS
 
    if (StringInput == ReverseS):
        print("It is palidrome as it is same whether you read it from right or left!")
    else:
        print("It isn't palidrome, because, if you read this word from right to left or visa versa, both are different!")

if usercalculator == "Table":
    tableinput= int(input("Please enter the number for table : "))
    tablerange= int(input("Please enter the range of table : "))
    for i in range (1, tablerange+1):
        print( tableinput, 'x',i, '=', tableinput*i)
else:
    print("Please check whether you are following the right wordcase or invalid input which is not available in calculator.")