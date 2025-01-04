from clear_sceen import clear_screen
import signup

def main():
    clear_screen()

    flag=True
    while(flag):
        print("1: login")
        print("2: signup")
        print("0: exit")
        
        x=int(input(""))
        if x==1:
            login()
            clear_screen()
        elif x==2:
            signup()
            clear_screen()
        else:
            flag=False
            clear_screen()
            print("closed successfully...")

def login():
    clear_screen()
    
    flag=True
    while(flag):
        print()
        print("1: log into organisation")
        print("2: Login as user")
        
        x=input()
        if x==1:
            
            clear_screen()
        elif x==2:
            
            clear_screen()
        else:
            flag=False
            clear_screen()


def signup():
    clear_screen()
    
    flag=True
    while(flag):
        print()
        print("1: create head organisation")
        print("2: create a sub organisation")
        print("3: signup as user")

        x=input()
        if x==1:
            signup.create_head()
            clear_screen()
        elif x==2:
            
            clear_screen()
        elif x==3:

            clear_screen()
        else:
            flag=False
            clear_screen()


main()
