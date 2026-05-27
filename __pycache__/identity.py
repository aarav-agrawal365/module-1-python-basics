a=23
if type(a) is int:
    print("true")
else:
    print("false")

b=2.3
if type(b) is not float:
    print("true")
else:
    print("false")

x=46
y=46
if x is y:
    print("they have the same identities")
y=20
if x is not y:
    print("they have different identities")
    