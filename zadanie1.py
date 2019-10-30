import math
def wylicz(y,x):
    y_k=y
    x_k=x
    h=math.sqrt(pow(x - koniec_x, 2) + pow(y - koniec_y, 2))
    h=round(h+droga(y_k,x_k),2)
    return h
def droga(y,x):
    a=0
    koniec=0
    while koniec !=1:
        #print("x="+str(x)+" y="+str(y)+"na rodzicu ="+ str(lista_rodzicow[y][x]))
        if lista_rodzicow[y][x] == 1:
            a+=1
            y+=1
        elif lista_rodzicow[y][x] == 2:
            a+=1
            x-=1
        elif lista_rodzicow[y][x] == 3:
            a+=1
            y-=1
        elif lista_rodzicow[y][x] == 4:
            a+=1
            x += 1
        elif x== start_x and y == start_y:
            koniec=1
    return a
def powrut(x,y):
    koniec=0
    while koniec != 1:
        print("x="+str(x)+" y="+str(y))
        if lista_rodzicow[y][x] == 1:
            mapa[y][x]=lista_rodzicow[y][x]
            y += 1
        elif lista_rodzicow[y][x] == 2:
            mapa[y][x]=lista_rodzicow[y][x]
            x -= 1
        elif lista_rodzicow[y][x] == 3:
            mapa[y][x]=lista_rodzicow[y][x]
            y -= 1
        elif lista_rodzicow[y][x] == 4:
            mapa[y][x]=lista_rodzicow[y][x]
            x += 1
        elif x == start_x and y == start_y:
            koniec = 1
lista_otwarta = [['' for col in range(6)] for row in range(6)]
lista_zamknieta = [['' for col in range(6)] for row in range(6)]
lista_rodzicow = [['' for col in range(6)] for row in range(6)]
mapa=[ [0 for col in range(6)] for row in range(6)]
#g p d l karzdy ruch kosztuje 1
#heurystyka h=dlugosc trasy + pierwiastek ((x-koniec_y)^2+(y-koniec y)^2) zakroglamy do 2 miesc po przecinku
#jezeli mamy 2 te same liczby postempujemy zgodnie z koenosciom ruvhu g p  d l
#start = 2,1  koniec 1,5
start_x=1
start_y=2
koniec_x=5
koniec_y=1
mapa[start_y][start_x]="S"
mapa[koniec_y][koniec_x]="K"
mapa[1][1]="X"
mapa[2][2]="X"
mapa[3][3]="X"
mapa[4][4]="X"
x=start_x
y=start_y
odl=2

i=0;
koniec=0
while(koniec!=1):
    pierwszy=0
    #gora
    if y-1>=0and mapa[y-1][x]!="X"and mapa[y-1][x]!="S"and lista_zamknieta[y-1][x]=='':
        lista_rodzicow[y - 1][x] =1
        lista_otwarta[y-1][x]=wylicz(y-1,x)
        print("1")
        odl=2
    #prawo
    if x+1<6 and mapa[y][x+1]!="X"and mapa[y][x+1]!="S"and lista_zamknieta[y][x+1]=='':
        lista_rodzicow[y][x + 1] =2
        lista_otwarta[y][x+1]=wylicz(y,x+1)
        print("2")
        odl=2
    #dol
    if  y+1<6 and mapa[y + 1][x] != "X" and mapa[y + 1][x] != "S" and lista_zamknieta[y + 1][x] == '':
        print("3")
        lista_rodzicow[y + 1][x] =3
        lista_otwarta[y + 1][x] = wylicz(y + 1, x)
        odl=2
    #lewo
    if x-1>=0 and mapa[y][x-1]!="X"and mapa[y][x-1]!="S"and lista_zamknieta[y][x-1]=='':
        print("4")
        lista_rodzicow[y][x - 1] = 4
        lista_otwarta[y][x-1]=wylicz(y,x-1)
        odl=2
    for y in range(6):
        for x in range(6):
            if lista_otwarta[y][x]!='' and pierwszy==0:
                min=lista_otwarta[y][x]
                mapa[y][x] = lista_otwarta[y][x]
                min_x = x
                min_y = y
                pierwszy+=1
            if lista_otwarta[y][x] != '':
                spr=lista_otwarta[y][x]
                mapa[y][x] = lista_otwarta[y][x]
                spr=float(spr)
                if min > spr and lista_otwarta[y][x] != '':
                    min = lista_otwarta[y][x]
                    min_x = x
                    min_y = y
                    odl=2
    x=min_x
    y=min_y
    lista_zamknieta[y][x]=lista_otwarta[y][x]
    mapa[y][x] = lista_otwarta[y][x]
    lista_otwarta[y][x]=''
    print()
    print("obrit="+str(i+2))
    i+=1
    print("pozycja x=" + str(x) + " pozycja y=" + str(y) + " wartosc=" + str(min))
    if (y-1>=0 and mapa[y-1][x]=="K"):
        y-=1
        lista_rodzicow[y][x] = 1
        koniec = 1
        powrut(x,y)
    elif(x+1<=5 and mapa[y][x+1]=="K"):
        x+=1
        lista_rodzicow[y][x] = 2
        koniec = 1
        powrut(x,y)
    elif (y + 1 <= 5 and mapa[y + 1][x] == "K"):
        y += 1
        lista_rodzicow[y][x] = 3
        koniec = 1
        powrut(x,y)
    elif(x-1>=0 and mapa[y][x-1]=="K") :
        x -= 1
        lista_rodzicow[y][x] = 4
        koniec=1
        powrut(x,y)
    if odl==0:
        koniec=1
        print("nie mozna przesc brak mozliwej trasy")
    odl-=1
print("mapa")
for y in range(6):
    for x in range(6):
        print(str(mapa[y][x]) + "       ", end="")
    print()