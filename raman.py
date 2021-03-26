print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit");
choice = int(input("Enter your choice: ")); # take input from console
if (choice>=1 and choice<=4): # taking input from 1 to 4
	print("Enter two numbers: ");
	num1 = int(input());
	num2 = int(input());
if choice == 1: # perform addition if 1
	res = num1 + num2;
	print("Result = ", res);
elif choice == 2: # perform subtraction if 2
	res = num1 - num2;
	print("Result = ", res);
elif choice == 3: # perform multiplication if 3
	res = num1 * num2;
	print("Result = ", res);
elif choice == 4: # perform division if 4
	res = num1 / num2;
	print("Result = ", res);
elif choice == 5:
	exit(); # exit if 5
else:
	print("Wrong input..!!"); 