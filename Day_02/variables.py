
# Variables in Python

first_name = 'Aslah '
last_name = 'C J'
country = 'india'
city = 'kochi'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Aslah ',
    'lastname': 'C J',
    'country': 'india',
    'city': 'kochi'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Aslah ', 'C J', 'india', 18, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)