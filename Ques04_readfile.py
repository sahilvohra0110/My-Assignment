#functiont to read the file:
with open("readme.csv") as readme:
    readmefile= readme.read()
print(readmefile)

#functiont to read the file:
with open("readme.csv", "a") as file: #a=append write content, w for overwrite..
    file.write("Hi, I am learning Python!!!")
