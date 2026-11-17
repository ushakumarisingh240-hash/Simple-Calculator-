x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

choice = input("Choose an operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division : ")

if choice == '1':
 print(x + y)
 
elif choice == '2':
 print(x - y)
 
elif choice == '3':
 print(x * y)
 
elif choice == '4':
 print(x / y)