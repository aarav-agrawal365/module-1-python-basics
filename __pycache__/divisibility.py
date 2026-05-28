print("please enter a number (numerator):")
nume=int(input())

print("please enter another number(denominator)")
deno=int(input())


if nume%deno==0:
    print(nume, "is divisible by", deno)

else:
    print(nume, "is not divisible by", deno)
    