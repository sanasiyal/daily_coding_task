 Mission:
You are creating a Smart Arithmetic Calculator that can perform basic operations: Addition (+), Subtraction (-), Multiplication (*), and Division (/). 

 Instructions:
️⃣ Ask the user to choose an operation:




print("lets explore calculator")

num1 = int(input("enter your number:"))
choice = input("select anyone operator (+ , - , * , /):")
num2 = int(input("enter your number:"))


if choice == "+":
  print(f"Result: {num1 + num2}")
elif choice == "-":
  print(f"Result: {num1 - num2}")
elif choice == "*":
  print(f"Result: {num1 * num2}")

elif choice == "/":
 print(f"Result: {num1 / num2}")
else:
 print("invalid")
