import random
import string

def get_user_choice(prompt):
  while True:
    user_input = input(prompt).strip().lower()
    if user_input in ['yes', 'y']:
      return True
    elif user_input in ['no', 'n']:
      return False
    else:
      print("Please answer with 'yes' or 'no'.")

while True:
  print('--- Welcome to the Password Generator ---')
  all_characters = string.ascii_letters

  if get_user_choice("Include numbers? (yes/no): "):
    all_characters += string.digits

  if get_user_choice("Include punctuation? (yes/no): "):
    all_characters += string.punctuation

  password = ''

  while True:
    try:
      password_length = int(input('Please enter your password length: '))
      if password_length <= 0:
          print('Please enter a positive number!')
          continue
      break
    except ValueError:
      print('Invalid Input: Enter whole numbers only')

  for i in range(password_length):
    password += random.choice(all_characters)

  print(f"Your generated password is: {password}")
  
  if not get_user_choice("Do you want to generate another password? (yes/no): "):
    print("Thank you for using the Password Generator. Goodbye! 👋")
    break