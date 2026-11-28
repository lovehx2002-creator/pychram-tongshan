age = 19

if age >= 18:
    print('你成年了')


if age < 4:
    print('free')
elif age < 10:
    print("4kuai")
elif age < 18:
    print("8 kuai")
else:
    print(29)

if age < 4:
    priece = 0
elif age < 10:
    priece = 4
elif age < 18:
    priece = 8
else:
    priece = 12

print(f"fee is {priece} yuan")
