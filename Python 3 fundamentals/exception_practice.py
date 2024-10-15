acroynms={"LOL":"Laugh out loud","IDK":"I don't know"}

# acroynm='LOL'
acroynm='BTW'
try:
    desc=acroynms[acroynm]
    print(f"The definition of {acroynm} is {desc}")
except:
    print(f"The {acroynm} acronym does not exist")
