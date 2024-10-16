srh_word=input("Enter the acronym you want definition:\n")
found=False
with open("/workspaces/Python-learning/Python 3 fundamentals/acroynm.txt") as fo:
    for line in fo:
        if srh_word in line:
            print(line)
            found=True
            break
if not found:
    print(f"{srh_word} acroynm not found")
