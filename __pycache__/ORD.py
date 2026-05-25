alp=input("Please enter a character: ")

ascii=(ord(alp))

print(ascii)

if  65<=ascii<=90 or 97<=ascii<=122:
    print("It is an alphabet")
else:
    print("It is not an alphabet")
