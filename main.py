#Halee Dischinger
#February 27, 2023
#CIS 245
#Assignment 8.1

#collects user input
fname = input("Enter the file name: ")
name = input("Enter your name: ")
address = input("Enter your street address: ")
phone = input("Enter your phone number: ")

#writes the user's input to the file
data = [name, address, phone]
with open("fname", mode="w") as file:
  file.write(", ".join(data))

#reads the file
with open("fname", "r") as file:
  print(file.read())