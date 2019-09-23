#age = int(input("How old are you? "))

#if (age >= 16) and (age <=65):
#if 16 < age < 66:
#    print("Have a good day at work")
#if (age < 16) or (age > 65):
# #    print("Enjoy your free time")
# #else:
# #    print("Have a good day at work")

# #x = input("Please enter some text")
# #if x:
# #    print("You entered '{}'".format(x))
# #else:
# #    print("You did not enter anything")

# #age = int(input("How old are you? "))
# #if not(age <18):
# #    print("You are old enoug to voye")
# #    print("Please put an X in the box")
# #else:
# #    print("Please come back in {0} years".format(18 - age))
# """ name = input("Hello what's your name?")
# age = int(input("How old are you?"))

# if age >= 18 and age <= 30:
#     print("Welcome to the jungle " + name)
# else:
#     print(name + " We are sorry, but we can not let you enter") """
#name = input("Please enter your name: ")
#age = int(input("How old are you, {0}?".format(name)))
#if age <= 18 and age <31:
    #prin("Welcome to club 18-30 holidays, {0}".format(name))
#else:
    #print("I'm sorry, our holidays are only for seriously cool people")

#for state in ["not pinnin'","no more","a stiff","bereft of lift"]:
#    print("This parrot is "+ state)

# for i in range(1,13):
    # for j in range(1,13):
    #     print("{1} times {0} is {2}".format(i,j,i*j))
    # print("===============")

# shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue

#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
if nasty_food_item:
    print("Can't I have anything without spam in it")