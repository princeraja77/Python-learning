import acroynym_look_up as al

def add_acronym(acronym):
    res=al.look_up(acronym)
    if res==False:
        definition=input("Enter the definition of acronym\n")
        with open("/workspaces/Python-learning/Python 3 fundamentals/acroynm.txt",'a') as fo:
            fo.write(f"\n{acronym} -> {definition}.")
    else:
        print(f"{acronym} definition already exists")

def main():
    while True:
        print("Welcome to acronym finder:")
        print("Enter 1 to look for acronym")
        print("Enter 2 to add an acronym")
        print("Enter 0 to exit the program")
        choice=int(input("Enter your choice: "))
        if choice==1:
            acronym=input("Enter the acronym you want to search\n")
            res=al.look_up(acronym)
            if res==False:
                print(f"{acronym} acroynm not found")
            else:
                print(res)
        elif choice==2:
            acronym=input("Enter the acronym you want to add\n")
            add_acronym(acronym)
        elif choice==0:
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    main()