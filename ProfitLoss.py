costprice=int(input("cp is: "))
sellingprice=int(input("sp is: "))
if(sellingprice>costprice):
 print("profit")
 profit=sellingprice-costprice
 print(profit)
else:
 print("loss")
 loss=costprice-sellingprice
 print(loss)