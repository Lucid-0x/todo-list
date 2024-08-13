import os
import time
import random

if os.name == 'nt':
    FILE_LIST_PATH = fr"{os.getcwd()}\todo_list.txt"
else: 
    FILE_LIST_PATH = fr"{os.getcwd()}/todo_list.txt"

check_sign = '[x]'
uncheck_sign = '[]'

# if your terminal supports these format you can remove the '#' from them
# check_sign = "✅"
# uncheck_sign = "☐"


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")    

def clear_all():
    with open(FILE_LIST_PATH, 'w', encoding='utf-8'):
        pass

def complete(index):
    with open(FILE_LIST_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sentence_in_list = lines[index -1].strip().split(" ", 1)
    sentence_in_list[0] = check_sign
    lines[index -1] = f"{' '.join(sentence_in_list)}\n"

    with open(FILE_LIST_PATH, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def uncomplete(index):
    with open(FILE_LIST_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sentence_in_list = lines[index -1].strip().split(" ", 1)
    sentence_in_list[0] = uncheck_sign
    lines[index -1] = f"{' '.join(sentence_in_list)}\n"

    with open(FILE_LIST_PATH, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def display_task():
    with open(FILE_LIST_PATH, 'r', encoding='utf-8') as file:
        print(file.read())
        
def add_task():
    title = input("enter the task name: ")

    if title != '':
        with open(FILE_LIST_PATH, 'a', encoding='utf-8') as file:
            file.write(f"{uncheck_sign} {title}\n")

def modifiy_task(index):
    with open(FILE_LIST_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    print(lines[index -1])
    print()
    title = input("Enter the edited task: ")

    if title != '':
        if check_sign in lines[index -1]:
            lines[index- 1] = f"{check_sign} {title}\n"

        else:
            lines[index -1] = f"{uncheck_sign} {title}\n"

    with open(FILE_LIST_PATH, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def check_choice(choice):
    letter = ''
    num = ''
    for x in choice:
        if x.isdigit():
            num += x
        elif x == ',':
            num += x
        else: 
            letter += x
    print(letter)
    print(num)
    return [letter.strip(), num.strip()]

def check_if_list_exist():
    if not os.path.exists(FILE_LIST_PATH):
        with open(FILE_LIST_PATH, 'w'):
            pass

def main():

    cls()
    display_task()
    choice = input("Enter the order> ").lower()
    check_choice(choice)
    letter = check_choice(choice)[0]
    number = check_choice(choice)[1]


    if letter == 'a':
        cls()
        try:
            if number:
                for _ in range(0, int(number)):
                    add_task()
            else:
                add_task()     
        except:
            pass
    
    elif letter == 'm':

        cls()
        try: 
            if ',' in number:
                number.split(',')
                for x in number:
                    if x == ',':
                        pass
                    else:
                        modifiy_task(int(x))
            else:
                modifiy_task(int(number))
        except:
            pass
    
    elif letter == 'c':
        cls()
        try:
            if ',' in number:
                number.split(',')

                for x in number:
                    if x == ',':
                        pass
                    else:
                        complete(int(x))
            else:
                complete(int(number))
        except:
            pass

    elif letter == 'uc':
        cls()
        try:
            if ',' in number:
                number.split(',')

                for x in number:
                    if x == ',':
                        pass
                    else:
                        uncomplete(int(x))
            else:
                uncomplete(int(number))
        except:
            pass

    elif letter == 'random':
        cls()
        try:
            with open(FILE_LIST_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            start_time = time.time()
            duration = 0.2


            while time.time() - start_time < duration:
                task = random.randint(0, len(lines) - 1)
                if uncheck_sign in lines[task]:
                    print(lines[task])
                    break
            else:
                print("no InComplete tasks")
            input("okay got it: ")
        except:
            pass
        
    elif choice == 'clear':
        clear_all()

    elif choice == 'help':
        cls()
        print("""
a + "optional({line number})" --- add task
c + {line number} --- check task
uc + {line number} --- uncheck task
m + {line number} --- modifiy a task
random	-- display one task to do
help -- print these instructions
clear -- delete all tasks
exit -- exit the program
""")
        input("enter to exit: ")

    elif choice == 'exit':
        cls()
        print("have a good day <3")
        exit()

    else:
        pass

check_if_list_exist()
while True:
    main()
