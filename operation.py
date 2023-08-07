from menu import mn
from defbus import book,information
import sys
def ask():
    mn()
    ch=int(input("enter your choice:--->"))
    print("-"*50)
    try:
        if(ch==1):
            try:
                book()
            except TypeError:
                print("ur are going wrong way:")
        elif(ch==2):

                information()
        else:
            print("thank you for wisting")
            sys.exit()
    except ValueError:
        print("dont enter str ,symbl")
ask()