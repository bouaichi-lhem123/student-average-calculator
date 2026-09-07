name = input("Enter your name: ")
gr1 = float(input("Enter the economics grade: "))
gr2 = float(input("Enter the statistics grade: "))
gr3 = float(input("Enter the accounting grade: "))

ave = (gr1 + gr2 + gr3) / 3

print(f"Average of {name} is: {ave:.2f}")

if ave >= 10:
    print("Admitted")
else:
    print("Not admitted")
