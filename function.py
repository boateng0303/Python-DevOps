
b = "today"     # b is a global variable declared at the root of your module so that all the functions can access it
def hello():
    global c     # this is another way to declare global variable
    c = "now"
    a = "monday"  # this variable is a local variable
    print('hello')
    print(a)

def display_name(name):
    print(f'hello {name}')
    print(b)


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

def convert_Pounds(num):
    pounds = num * 2.205
    return pounds


def main():
    my_value = addition(2,7)
    print(my_value)              # if you want call the function  that is a stored in variable we can declare like this
                                          


if __name__=="__main__":       # This code means do not execute any script below this constructor when the function is imported 
    main()


# x= addition(5, 7)
# print(x)


# pound_calc = convert_Pounds(12)
# print(pound_calc)