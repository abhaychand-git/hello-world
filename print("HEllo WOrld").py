x = int ( (input("Enter:")))

if (x % 4 == 0 or x % 400 == 0) and x % 100 != 0:
    print("leap")

else:
    print("not leap")