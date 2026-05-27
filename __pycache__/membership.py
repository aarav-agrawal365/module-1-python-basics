print("please enter marks you obtained in 5 subjects")
eng=int(input("marks obtained in english"))
sci=int(input("marks obtained in science"))
hist=int(input("marks obtained in history"))
geo=int(input("marks obtained in geography"))
math=int(input("marks obtained in math"))

total=eng+sci+hist+geo+math
ave=int(total/5)

validRange=range(0,101)

if ave not in validRange:
    print("Invalid input!")

elif ave in range(81,101):
    print("excellent!")
elif ave in range(41,81):
    print("good")
elif ave in range(0,41):
    print("try harder!!!")