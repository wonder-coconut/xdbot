art = open("ascii.txt",'r')
arttxt = art.read().split("$")
i = 0
test = "abcghijkl"
while(i<10):
    for ch in test:
        artchar = arttxt[ord(ch)-97]
        artline = artchar.split("\n")
        print(artline[i], end="")
    print("")
    i = i + 1
print("")