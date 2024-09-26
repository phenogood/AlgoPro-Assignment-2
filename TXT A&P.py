def update_score(username, score):
    complete = False
    with open('DB.txt', 'r') as file:
        lines = file.readlines()

    with open('DB.txt', 'w') as file:
        for x in lines:
            if x.startswith(username + ':'):
                current = int(x.split(': ')[1].strip())
                new = current + score
                file.write(f'{username}: {new}\n')
                complete = True
            else:
                file.write(x)
        
        if complete == False:
            file.write(f'{username}: {score}\n')

while True:
    entry = str(input('continue or stop? ')).lower()
    
    if entry == 'stop':
        print('Thanks for using. See u next time!')
        break
    
    option = str(input('What do u wanna do?\n1. Read\n2. Add\n3. Change\n4. Play\nOption: ')).lower()
    
    if option in ('1', 'read'):
        with open('DB.txt', 'r') as file:
            c = file.read()
            print(c)
        continue
    
    elif option in ('2', 'add'):
        new = str(input('What would your username be? '))
        with open('DB.txt', 'a') as file:
            file.write(f'{new}: 0\n')
    
    elif option in ('3', 'change'):
        with open('DB.txt', 'r') as file:
            c = file.read()
            print(c)
            
        old = str(input('Enter the username you want to change: '))
        new = str(input('What is the new username? '))

        with open('DB.txt', 'r') as file:
            lines = file.readlines()

        with open('DB.txt', 'w') as file:
            for line in lines:
                if line.startswith(old + ':'):
                    file.write(f'{new}: {line.split(": ")[1]}')
                else:
                    file.write(line)
    
    elif option in ('4', 'play'):
        username = str(input('What is your username? '))
        
        from random import randint
        number = randint(1, 101)
        
        while True:
            guess = int(input('Guess the number: '))
            if guess < number:
                print('higher')
            elif guess > number:
                print('lower')
            elif guess == number:
                print(f"You got it! It's {number}!")
                score = 0
                score += 1
                update_score(username, score)
                break
            
    else:
        print('Umm are u sure??')
