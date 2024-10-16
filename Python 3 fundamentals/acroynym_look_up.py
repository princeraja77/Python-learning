srh_word=input("Enter the acronym you want definition:\n")
found=False
with open("acroynm.txt",'r') as file:
    for line in file:
        if srh_word in line:
            print(line)
            found=True
            break
if not found:
    print(f"{srh_word} acroynm not found")
