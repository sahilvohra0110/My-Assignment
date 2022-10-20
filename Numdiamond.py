# patternsize = int(input("Please enter the size of patter : "))
# we can take the input if we don't know the limit in our question, however we have a dedicated number to print which is "3" so we'll take below code:

patternsize = int(3)
for i in range(0, patternsize + 1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print('')