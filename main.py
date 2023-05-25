import matplotlib as mpt 
import matplotlib.pyplot as plt 
import numpy as np

x1=[]
y1=[]

print('Entrez le nom du premier fichier:')

nom1 = input()

print('Entrez le nom du deuxième fichier: ')

nom2 = input()

with open(nom1+'.dat','r') as datFile:
    donnée = [data.split() for data in datFile]


for i in range (len(donnée)-1):
    x1.append(float(donnée[i][0]))
    y1.append(float(donnée[i][1]))

with open(nom2+'.dat','r') as datFile:
    donnée = [data.split() for data in datFile]

x2=[]
y2=[]

for i in range (len(donnée)-1):
    x2.append(float(donnée[i][0]))
    y2.append(float(donnée[i][1]))


point_intersection = [[],[]]

def comparaison_point():
    if y1[0] < y2[0]:
        courbe_inf = 1
    elif y1[0]> y2[0]:
        courbe_inf = 2
    else:
        courbe_inf=0
    
    for i in range(len(y1)-2):
        if y1[i+1] < y2[i+1]:
            if courbe_inf == 2:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1])
                courbe_inf = 1
            if courbe_inf == 0:
                courbe_inf = 1
        elif y1[i+1] == y2[i+1]:
            point_intersection[0].append(i+1)
            point_intersection[1].append(y1[i+1])
            courbe_inf == 0
        else : 
            if courbe_inf == 1:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1])
                courbe_inf = 2
            if courbe_inf == 0:
                courbe_inf = 2
    


def intersection(y1n, y2n, y1n1, y2n1,x,xn1):
    #Recherche des fonction affines
    a1 = (y1n1-y1n)/(xn1-x)
    a2 = (y2n1-y2n)/(xn1-x)
    b1 = y1n - a1 * x
    b2 = y2n - a2 * x
    #Recherche du point d'intersection
    x_int = (b2-b1)/(a1-a2)
    y_int = (a1*b2-b1*a2)/(a1-a2)
    point_intersection[0].append(x_int)
    point_intersection[1].append(y_int)

comparaison_point()
print(point_intersection)

with open(nom1+nom2+"point_d'intersection.dat","w")as fichier:
    for i in range(len(point_intersection[0])):
        fichier.write(str(point_intersection[0][i])+' '+str(point_intersection[1][i])+'\n')


plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(point_intersection[0],point_intersection[1], 'ro')

plt.show()