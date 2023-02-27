import random


def generate_passwords(words, min_length):
     """Generate a list of passwords by combining the user's inputs"""
     passwords = []
     num_entries = int(input("Enter the number of entries you want to combine: "))
     for i in range(len(words)):
         for j in range(i+1, len(words)):
             for k in range(num_entries):
                 password1 = words[i].lower() + words[j][:k+1]
                 password2 = words[i].lower() + words[j][:k+1].lower()
                 password3 = words[i] + words[j][:k+1].lower()
                 password4 = words[i] + words[j][:k+1]
                 combined_passwords = [password1, password2, password3, password4]
                 for password in combined_passwords:
                     if len(password) >= min_length:
                         passwords.append(password)
     return passwords


print("Welcome to the password generator!")
print("Follow the instructions to generate a list of passwords using your inputs.")

# Get user inputs
words = []
num_words = int(input("Enter the number of words: "))
for i in range(num_words):
     word = input("Enter word " + str(i+1) + ": ")
     words.append(word)

more_words = input("Do you want to enter more words? (Y/N): ").lower()
while more_words == "y":
     num_words = int(input("Enter the number of words: "))
     for i in range(num_words):
         word = input("Enter word " + str(len(words)+i+1) + ": ")
         words.append(word)
     more_words = input("Do you want to enter more words? (Y/N): ").lower()

min_length = int(input("Enter the minimum length of the password: "))

passwords = generate_passwords(words, min_length)

# Save the passwords to a file
with open("passwords.txt", "w") as f:
     for password in passwords:
         f.write(password + "\n")

print(f"Generated {len(passwords)} passwords with a minimum length of {min_length}.")
print("The passwords have been saved to passwords.txt")