#nov 30 lesson 2
x = 5
y = 5.5
z = "Hi I exist apparently"
a = True
b = None

list = [x, y, z, a, b]
tup = (x, y, z, a, b)


def ask():
    anwer = ""
    print("Shouild I go again? [y/n]")
    answer = input()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        ask()


for i in range(len(list)):
    print(type(list[i]))



ex = list.pop()
ty = tup[1]

print(ty)
#while a:
 #   a = ask()

##https://www.w3schools.com/python/python_lists_comprehension.asp
##list comprehension doc for next lesson
