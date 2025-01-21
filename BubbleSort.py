tab = [3,6,8,11,0,9,9]

for i in range(len(tab)):
    for j in range(i+1, len(tab)): #odliczanie od i+1
        if tab[i]>tab[j]:
            tab[i], tab[j]=tab[j], tab[i]

for el in tab:
    print(el)