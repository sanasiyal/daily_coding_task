 Mission:
Create a simple program that checks whether a number is Even or Odd.

 Instructions:
 Ask the user to enter a number.
 Check if the number is even or odd using the modulus (%) operator.
 Display the result in a friendly message.


user = int(input("Enter any number:"))

if user % 2 == 0:
  print(f"{user} is even number")
else:
    print(f"{user} is odd number")
