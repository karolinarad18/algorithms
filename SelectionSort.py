tablica = [2,1,6,7,0,22,32]

for i in range(len(tablica)-1):
    theLowestKey = i
    for j in range(i+1, len(tablica)-1): #deklaracja poczatku petli
        if tablica[j]<tablica[theLowestKey]:
            theLowestKey=j
    tablica[i], tablica[theLowestKey] = tablica[theLowestKey], tablica[i]

for i in range(len(tablica)):
    print(tablica[i])