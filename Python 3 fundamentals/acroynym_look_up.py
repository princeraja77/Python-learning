def look_up(srh_word):
    try:
        with open("/workspaces/Python-learning/Python 3 fundamentals/acroynms.txt") as fo:
            for line in fo:
                if srh_word in line:
                    return line
            return False
    except FileNotFoundError as e:
        return e

if __name__=="__main__":
    srh_word=input("Enter the acronym you want definition:\n")
    res=look_up(srh_word)
    if res==False:
        print(f"{srh_word} acroynm not found")
    else:
        print(res)