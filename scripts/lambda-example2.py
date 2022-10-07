from numpy import full


full_name = lambda first_name, last_name: first_name.strip().title() + " " + last_name.strip().title()

print(full_name("   João", "almeida"))

