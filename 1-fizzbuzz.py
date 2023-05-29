mod=int(input("enter a number: "))


if mod%3==0 and mod%5==0 and mod<101:
    print("fizzbuzz")
elif mod%5==0 and mod<101:
    print("buzz")
elif mod%3==0 and mod<101:
    print("fizz")
else:
    print("its not fizzbuzz")
    