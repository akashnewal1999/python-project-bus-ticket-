import cx_Oracle
#from createtable import jay
from insertbookticket import ticket
from insertbooktickettwo import tic
from insertinfo import ak
def book():
    while(True):
        ch=input("do u want to book tickets(yes/no):")
        if(ch=="no"):
            print("thanks for coming")
            break
        else:
            print("select your location---->")
            print("*"*50)
            print("\t\t\tFor Nagpur to Wardha press 1")
            print("\t\t\tFor Nagpur to Hyderabad press 2")
            print("\t\t\tFor Nagpur to Akola press 3")
            print("*"*50)
            at=int(input("your location is:---->"))
            if(at<=3):
                if(at==1):
                    print("1:Nagpur to Wardha")
                    ticket()
                elif(at==2):
                    print("2:Nagpur to Hyderabad")
                    tic()
                elif(at==3):
                    print("3:Nagpur to Akola")
            else:
                raise TypeError
def information():
    print("information")
    print(" only bus will be going hyd,akol,wrd")
    #print("\n")
    ak()
