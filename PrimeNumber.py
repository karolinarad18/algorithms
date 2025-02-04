import math

print("Sprawdź czy twoja liczba jest liczbą pierwszą")
a = int(input("Podaj liczbę: "))
if a<2:
    print(a, "nie jest liczbą pierwszą")
liczbaPierwsza=True
for i in range(2,int(math.sqrt(a))+1): #sprawdzamy tylko do pierwiastka, bo jezeli do tego momentu nie ma zadnych
    if a%i==0: #dzielników to liczba jest liczbą pierwszą, bo na pierwiastku kończą się "pary" liczb
        liczbaPierwsza=False; #np: liczba 16 - 1,2,4,8,16 -->1x16,2x8,4x4,
        break

if liczbaPierwsza:
    print(a, "jest liczbą pierwszą")
else:
    print(a, "NIE jest liczbą pierwszą")













# dzielenia=0;
# for i in range(2,a+1):
#     if a%i==0:
#         dzielenia=dzielenia+1
#
# if dzielenia==1:
#     print(a, "to liczba pierwsza")
# else:
#     print(a, "to nie liczba pierwsza")