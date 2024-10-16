acroynms={"LOL":"Laugh out loud","IDK":"I don't know"}

# acroynm='LOL'
acroynm='BTW'
try:
    desc=acroynms[acroynm]
    print(f"The definition of {acroynm} is {desc}")
except:
    print(f"The {acroynm} acronym does not exist")

a=1234
b=0
try:
    if b==0:
        raise ZeroDivisionError
except:
    print("you are trying to devide by zero")
