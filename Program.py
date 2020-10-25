from AuthGG import *

###########################################
#                                         #
#                                         #
#        github.com/robert169             #
#                                         #
#        discord: roberth#0310            #
#                                         #
#        telegram: @roberth832            #
#                                         #
#                                         #
###########################################

AuthGG.Initialize("AID", "PROGRAM SECRET", "API KEY", "VERSION")

if not AuthGG.is_initialized:
    print("[!] Please initialize your application first!"),
    time.sleep(3),
    os._exit(0)
    
def Logo():
    return (
        print("                                                                                      "),
        print("                                █████╗ ██╗   ██╗████████╗██╗  ██╗    ██████╗  ██████╗ "),
        print("                               ██╔══██╗██║   ██║╚══██╔══╝██║  ██║   ██╔════╝ ██╔════╝ "),
        print("                               ███████║██║   ██║   ██║   ███████║   ██║  ███╗██║  ███╗"),
        print("                               ██╔══██║██║   ██║   ██║   ██╔══██║   ██║   ██║██║   ██║"),
        print("                               ██║  ██║╚██████╔╝   ██║   ██║  ██║██╗╚██████╔╝╚██████╔╝"),
        print("                               ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝ "),
        print("                                                                                      ")
    )

def Title(text):
    return os.system("title {}".format(text))

def Clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    Title("AuthGG Example")
    Clear()
    Logo()
    print("[1] Register")
    print("[2] Login")
    print("[3] All in one")
    print("[4] Extend Subscription")
    print()
    print("[>] ", end="")

    option = str(input())
    if option == "1":
        if not AuthGG.can_register:
            print("[!] Register is not enabled, please try again later!")
            time.sleep(3)
            os._exit(0)
        else:
            Clear()
            Logo()
            print("[>] Username: ", end='')
            username = str(input())
            print()
            print("[>] Password: ", end='')
            password = str(input())
            print()
            print("[>] Email: ", end='')
            email = str(input())
            print()
            print("[>] License: ", end='')
            license = str(input())
            print()
            if AuthGG.Register(username, password, email, license):
                print("[!] You have successfully registered!")
                time.sleep(3)
                os._exit(0)
    elif option == "2":
        if not AuthGG.can_login:
            print("[!] Login is not enabled, please try again later!")
            time.sleep(3)
            os._exit(0)
        else:
            Clear()
            Logo()
            print("[>] Username: ", end='')
            username = str(input())
            print()
            print("[>] Password: ", end='')
            password = str(input())
            print()
            if AuthGG.Login(username, password):
                print("[!] You have successfully logged in!")
                time.sleep(3)
                os._exit(0)
    elif option == "3":
        Clear()
        Logo()
        print("[>] Key: ", end='')
        key = str(input())
        print()
        if (AuthGG.AIO(key)):
            print("[!] Welcome back to my application!")
            time.sleep(3)
            os._exit(0)
        else:
            print("[!] Your key does not exist!")
            time.sleep(3)
            os._exit(0)

    elif option == "4":
        Clear()
        Logo()
        print("[>] Username: ", end='')
        username = str(input())
        print()
        print("[>] Password: ", end='')
        password = str(input())
        print()
        print("[>] License: ", end='')
        license = str(input())
        print()
        if AuthGG.ExtendSubscription(username, password, license):
            print("[!] You have successfully extended your subscription!")
            time.sleep(3)
            os._exit(0)

if __name__ == "__main__":
    main_menu()
