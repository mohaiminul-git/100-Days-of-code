def formate_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

formate_name("islam"," niloy")
def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
       return False

print(is_leap_year(1989))
        
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

operations= {"+" :add, "-" :substract, "*":multiply, "/": division}
def calculator():
    shoud_continue = True
    first_num= float(input("what's the first number?"))
    while shoud_continue:
        chose_operation = input(operations.keys())
        sceond_num= float(input("what's the sceond number?"))
        new_num =operations[chose_operation](first_num,sceond_num)
        print(new_num)
        ask_again = input('Do you want to continue ("Yes","no"):')
        
        if ask_again.lower()== "yes":
            first_num= new_num
            
        

        else:
            shoud_continue = False
            print("\n" *20)
            calculator()
            


calculator()
