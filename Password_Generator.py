import random as rnd

def generate():
    print('-----------------------------------------------------------------')
    choice = int(input('1. Random Password\n2. Custom Password\nChoose your preference: '))
    if choice == 1:
        print(random_password())
    elif choice == 2:
        print(custom_password())
    else:
        print('Invalid choice. Enter again')
        generate()

#driver function
def main():
    print("---------------------PASSWORD GENERATOR--------------------------")
    answer = input('Would you like to generate password? (Y/N): ').upper()
    if answer == 'Y':
        generate()
    elif answer == 'N':
        print('Exiting application . . . . .')
    else:
        print('Invalid choice. Exiting Application . . . . .')

#Generating Random Password 
def random_password():
    print("Enter minimum length: ")
    min = int(input())
    if min < 8:
        print("Too short to be a strong password. Try Again")
        random_password()

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
    SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-','?']

    TOTAL_LIST = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + DIGITS + SPECIAL_CHARACTERS
    password_list = list(rnd.choice(DIGITS) + rnd.choice(LOWERCASE_CHARACTERS) + rnd.choice(UPPERCASE_CHARACTERS) + rnd.choice(SPECIAL_CHARACTERS))
    max = int(input("Enter maximum length (0 if no maximum length): "))
    if max != 0:
        limit = rnd.randrange(min-4,max-4)
    else: 
        limit = rnd.randrange(min-4,10)
    
    for _ in range(limit):
        password_list += rnd.choice(TOTAL_LIST)
        rnd.shuffle(password_list)
    password = ""
    for _ in password_list:
        password += _
    print("Password generated: ",end="")
    return password

#Generating Customised Password
def custom_password():
    print("Enter minimum length: ")
    min = int(input())
    if min < 6:
        print("Too short to be a strong password. Try Again")
        custom_password()

    max = int(input("Enter maximum length (0 if no maximum length, not same as min): "))
    if max != 0:
        limit = rnd.randrange(min,max)
    else: 
        limit = rnd.randrange(min,20)
    
    words = input("Enter details (eg. Name, Pet name, Date of birth,\n Partner's Name, City of residence, Favourite football team, Social media app using etc.): ").split()
    
    password = ''
    while len(password) <= limit:
        i = rnd.choice(words)
        j = rnd.choice([1,2])
        if j == 1:
            password += i[:len(i)//2]
        else:
            password += i[len(i)//2:]
    
    print("Password generated: ",end="")
    return password
    
if __name__ == '__main__' :
    main()