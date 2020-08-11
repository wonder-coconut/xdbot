art = open("ascii.txt",'r')
arttxt = art.read().split("$")
for arty in arttxt:
    print(arty)
    print("\n")