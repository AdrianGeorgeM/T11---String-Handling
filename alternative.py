# Ask the user to enter a string
user_input = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""

# Loop through each character in the user input
for i in range(len(user_input)):
    if i % 2 == 0:
        # If the caracter index is even, make it uppercase
        result += user_input[i].upper()
    else:
        # If the character index is odd, make it lowerccase
        result += user_input[i].lower()

# Print the result
print("Transformedd String:", result)
