# num1 = input("Please give me your first number: ")
# num2 = input("Please give me your second number: ")


# print(num1 + num2)

# print(type(num1))
# print(type(num2))




# num1 = input("Please give me your first number: ")
# num1 = int(num1)
# num2 = input("Please give me your second number: ")
# num2 = int(num2)

# print(num1 + num2)
# print(type(num1))
# print(type(num2))


num1=int(input("Please give me your first number: "))
num2=float(input("Please give me your second number: "))


print(num1 + num2)

 



# num1=int(input("Please give me your first number: "))
# num2=int(input("Please give me your second number: "))

# print(num1 + num2)

# name = 'kwasi'
# email= "kwasi@gmail.com"
# profession = "Devops Engineer"

# #print("My name is {name} and my email is {email}. I am {profession}")
# print(f"My name is {name} and my email is {email}. I am {profession}")

# Weight_in_kg = int(input("Give me your weight in kg: "))
# weight_in_pounds = Weight_in_kg * 2.205

# print(f"Your weight in pound is{weight_in_pounds:.2f}lb")

# "1" + "2" = "12"


def hello():
    print('hello')
    

def display_name(name):
    print(f'hello {name}')



display_name('kwasi')


def addition(num1, num2):
    sum = num1 + num2
    return sum

x= addition(5, 7)
print(x)



def command(cmd):
    import os
    os.system(cmd)

command("ls")