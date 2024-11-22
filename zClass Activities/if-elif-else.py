#elif
a = float (input("Enter your number:"))
b = float (input("Enter your number:"))
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

#practice
Score = int (input("Enter your mark:"))
if Score >=90:
    print("Your grade is A.")
elif Score >=80:
    print("Your grade is B.")
elif Score >=70:
    print("Your grade is C.")
elif Score >=60:
    print("Your grade is D.")
else:
    print("Your grade is F.")