name = input("Please enter your name: ")
age = input(f"Hello {name}, please input your age:")
age = int(age)
if 17 < age <= 21:
    print(f"{name} you are adult already")
elif age == 16:
    print(f"{name} you are infant yet")
else:
    print((f"{name} you are grandfather"))
money = 100
if money:
    print(f"you have {money} {name}")
else:
    print(f"{name} you don't have money")

result = None
if result:
    print("Yeah, have something")
else:
    print("Ooops, nothing")

money = None
if money:
    print(f"You have {money}")
else:
    print("You don't have money")
