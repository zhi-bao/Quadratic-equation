from math import sqrt
from time import sleep
def equation_quadratic():
    print("Welcome to equation quadratic solver")
    a = int(input("Please enter the value of a "))
    b = int(input("Please enter the value of b "))
    c = int(input("Also the value of c "))
    print("Progressing ...")
    sleep(2)
    # Here we have to know the solution for our equation
    delta = (b**2) - (4*a*c)

    # After calculating the value of delta we have to know if delta is negative or positive or equal zero
    if delta < 0:
        print("There's no solution for you")

        # May be the user will be retry again let's get him another chance
        yes_list = ['yes', 'y', 'yeb', 'yeah']
        ask_retry = str(input("DO YOU WANT TO RETRY ?"))
        if ask_retry in yes_list:
            equation_quadratic()
        else:
            input("Enter to exit ") # The user have to press enter or any key !
            exit() # The program will exit now
    elif delta == 0:
        x = - b / (2*a)
        print("There's one solution which's ",x)

        # May be the user will be retry again let's get him another chance
        yes_list = ['yes', 'y', 'yeb', 'yeah']
        ask_retry = str(input("DO YOU WANT TO RETRY ?"))
        if ask_retry in yes_list:
            equation_quadratic()
        else:
            input("Enter to exit ")  # The user have to press enter or any key !
            exit()  # The program will exit now
    else:
        # delta > 0
        x1 = (- b - sqrt(delta)) / (2 *a)
        x2 = (- b + sqrt(delta)) / (2 * a)
        print("There's two solution are ",x1,x2)

        # May be the user will be retry again let's get him another chance
        yes_list = ['yes', 'y', 'yeb', 'yeah']
        ask_retry = str(input("DO YOU WANT TO RETRY ?"))
        if ask_retry in yes_list:
            equation_quadratic()
        else:
            input("Enter to exit ")  # The user have to press enter or any key !
            exit()  # The program will exit now


equation_quadratic()