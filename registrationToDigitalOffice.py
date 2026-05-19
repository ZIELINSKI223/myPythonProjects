print("""Welcome to the process of registration to our Digital Office!
      \nTo use the services our Office offers, you must complete:
      \t- Name;
      \t- Surname;
      \t- Date of birth;
      \t- Place of birth;
      \t- Sex; and
      \t- PESEL ID (or your Passport ID)""")
print()
name = input("Please enter your name: ")
while name == "":
    print("You did not provide your name!")
    name = input("Please enter your name: ")
print()
surname = input("Please enter your surname: ")
while surname == "":
    print("You did not provide your surname!")
    surname = input("Please enter your surname: ")
print()
date_of_birth = input("Please enter your date of birth: ")
while date_of_birth == "":
    print("You did not provide your date of birth!")
    date_of_birth = input("Please enter your date of birth: ")
print()
place_of_birth = input("Please enter your place of birth: ")
while place_of_birth == "":
    print("You did not provide your place of birth!")
    place_of_birth = input("Please enter your place of birth: ")
print()
sex = input("Please enter your gender: ")
while sex == "":
    print("You did not provide your gender!")
    sex = input("Please enter your gender: ")
print()
person_id = input("Please enter your PESEL ID or Passport ID: ")
while person_id == "":
    print("You did not provide your documment ID!")
    person_id = input("Please enter your PESEL ID or Passport ID: ")
print()
print(f"Ok! Your full name is {name} {surname} and you born in {place_of_birth}. Your date of birth is {date_of_birth}, also you are a {sex} and your documment ID is {person_id}. Welcome to our Digital Office. You can fully access to our Office offers and enjoy. Happy codding and learning!")


          

