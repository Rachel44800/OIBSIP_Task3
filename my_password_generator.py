import random
import string

print('Hello! Welcome to My Password Generator!')

length = int(input('\nEnter the length of the password: '))
include_sets = [input(f'Include {charset} characters? (y/n): ').lower() == 'y' for charset in ['lowercase', 'uppercase', 'digits', 'symbols']]

all_characters = ''.join([string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation][i] for i in range(4) if include_sets[i])

if not all_characters:
    print('Error: Please select at least one character set.')
else:
    random_password = ''.join(random.sample(all_characters, length))
    print(f'Generated Password: {random_password}') 
