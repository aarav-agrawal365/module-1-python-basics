print("Enter your marks you obtained in 4 subjects")
math=int(input("maths:"))
english=int(input("english:"))
history=int(input("history:"))
science=int(input("science:"))

sum=math+english+history+science
print("the total marks you obtained are:",sum)

percentage=(sum/400)*100

print("percentage marks=",percentage)