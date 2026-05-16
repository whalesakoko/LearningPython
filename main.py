#name = input("Tell us your name: ")
#age = input("Tell us your age: ")
from multiprocessing.reduction import steal_handle

#print("Hello " + name + "!" "," + " your age is " + age)

#STRING
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = num1 + num2
#print(result)

#INTEGER
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1) + int(num2)
#print(result)

#FLOAT
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)

#MAD LIBS GAME

#colour = input("Enter a colour: ")
#plural_Noun = input("Enter a plural Noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + colour)
#print(plural_Noun + " are blue")
#print("I love you " + celebrity)


#num1 = 22.4321
#num2 = 22.1234
#print('num 1 is', num1, 'and num 2 is', num2)

#FORMAT METHOD
#print(f'num 1 is {num1} and num 2 is {num2}')

#LIST
#friends = ["Soft", "Akeem", "Shigo", "Bam"]
#print(friends[0])
#print(friends[1])
#print(friends[2])
#print(friends[3])
#print(friends[-1])
#print(friends[1:])
#print(friends[2:])
#print(friends[1:3])
#friends[3] = "Vibe"
#print(friends[3])


#LIST FUNCTION

#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Karen", "Jim", "Oscar", "Toby"]
#friends.extend(lucky_numbers)
#friends.append("Gill")
#friends.insert(1, "Kelly")
#friends.remove("Toby")
#friends.clear()
#friends.pop()
#friends.sort()
#lucky_numbers.sort()
#lucky_numbers.reverse()
#print(friends.index("Karen"))
#print(friends.count("Karen"))
#friends2 = friends.copy()
#print(friends2)
#print(friends)
#print(lucky_numbers)


#TUPLES(immutable/cannot be changed)

#coordinates = (4, 5)
#coordinates = [(4, 5), (6, 7), (8, 9)]
#print(coordinates)
#print(coordinates[1])

#FUNCTIONS (indented)

#def say_hi():
 #   print("hello world")
#say_hi()

#def say_hi(name):
 #   print("Hello " + name)
#say_hi("Michael")
#say_hi("Steve")
#say_hi("John")
#say_hi("James")

#def say_hi(name, gender, age):
 #   print("Hello " + name + " your gender is " + gender + " and your age is " + age)
#say_hi("Michael", "Male", "18")
#say_hi("Steve", "Male", "37")

#def say_hi(name, gender, age):
 #   print("Hello " + name + " your gender is " + gender + " and your age is " + str(age))
#say_hi("Michael", "Male", 18)
#say_hi("Steve", "Male", 37)

#RETURN STATEMENT

#def cube(num):
 #   return num*num*num
#print(cube(5)

#def cube(num):
#    return num*num*num
#result = cube(5)
#print(result)


# IF STATEMENTS

#I wake up
#if I am hungry
 #  I eat breakfast

#I leave my house
#if it is cloudy
 #   I bring an umbrella
#otherwise
 #   I bring sunglasses

#I am at a restaurant
#if I want meat
 #   I order a steak
#otherwise if I want pasta
 #   I order spaghetti & meatballs
#otherwise
 #   I order salad.


#is_male = True
#if is_male:
 #   print("You are male.")
#else:
#    print("You are female.")

#is_male = False
#if is_male:
 #   print("You are male.")
#else:
 #   print("You are female.")

#is_male = True
#is_tall = True

#if is_male or is_tall:
 #   print("You are male or tall or both.")
#else:
 #   print("You are neither male nor tall.")

#is_male = False
#is_tall = True
#   print("You are male or tall or both.")
#else:
#    print("You are neither male nor tall.")


#is_male = False
#is_tall = False

#if is_male or is_tall:
 #   print("You are male or tall or both.")
#else:
 #   print("You are neither male nor tall.")

#is_male = True
#is_tall = True

#if is_male and is_tall:
 #   print("You are a tall male.")
#else:
 #   print("You are either not male or not tall or both.")

#is_male = False
#is_tall = False

#if is_male and is_tall:
 #       print("You are a tall male.")
#elif is_male and not(is_tall):
#        print("You are a short male.")
#elif not(is_male) and is_tall:
#        print("You are not a male but you are tall.")
#else:
 #       print("You are not male and not tall.")




#secretPasswords = ["Spiral", "Larvae", "Grind", "Goat", "Bird"]
#entryPrices = {"Adult":15, "Children":10, "Pensioner":5}
#whatPassword = input("What's your secret password?: ")
#whatCategory = input("Are you a Child, Adult, or Pensioner?: ")

#if whatPassword in secretPasswords:
 #   print("Your secret password is correct!")



#IF STATEMENTS AND COMPARISONS

#def max_num(num1, num2, num3):
 #   if num1 >= num2 and num1 >= num3:
  #      return num1
   # elif num2 >= num1 and num2 >= num3:
    #    return num2
    #else:
     #   return num3

#print(max_num(300, 40, 50 ))

#BUILDING A CALCULATOR

#num1 = float(input("Enter the first number: "))
#op = input("Enter the operator: ")
#num2 = float(input("Enter the second number: "))
#if op == "+":
 #   print(num1 + num2)
#elif op == "-":
 #   print(num1 - num2)
#elif op == "*":
 #   print(num1 * num2)
#elif op == "/":
 #   print(num1 / num2)
#else:
 #   print("You have entered an invalid operator")

#DICTIONARIES (Keys & Values)

#monthsConversions = {
 #  "Jan": "January",
 #  "Feb": "February",
 #  "Mar": "March",
 #  "Apr": "April",
 #  "May": "March",
 #  "Jun": "June",
 #  "Jul": "July",
 #  "Aug": "August",
 #  "Sep": "September",
 #  "Oct": "October",
 #  "Nov": "November",
 #  "Dec": "December",

#

#print(monthsConversions)
#print(monthsConversions ["Feb"])
#print(monthsConversions ["Jan"])
#print(monthsConversions.get("Dec"))
#print(monthsConversions.get("Luv", "Not a valid key"))

#While loop


#i = 1
#while i <= 10:
 #   print(i)
 #   i += 1
#print("Done with loop")

#BUILDING GUESSING GAME (While Loop)

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limt = 3
# out_of_guesses = False

# while guess != secret_word:
#     guess = input("Guess a word: ")
# print("You Won!")

# name = input("Tell us your name: ")
# age = input("Tell us your age: ")
# print("Your name is " name "and you are " age)

import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")

        task = {
            "description": description,
            "due": due_date,
            "completed": False
        }

        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                status = "Done" if task["completed"] else "pending"
                print(f"{i+1}. {task['description']} | Due: {task['due']} | {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task['description']} | Completed: {task['completed']}")
            
            try:
                num = int(input("Enter task number to mark complete: ")) - 1
                
                if 0 <= num < len(tasks):
                    tasks[num]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as complete!")
                else:
                    print("Invalid task number!")
                    
            except ValueError:
                print("Please enter a valid number")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task['description']}")

            try:
                num = int(input("Enter task number to delete: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['description']}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number")


                

    elif choice == "5":
        break
    else:
        print("Invalid option") 





            