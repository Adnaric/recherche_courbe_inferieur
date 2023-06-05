import matplotlib as mpt 
import matplotlib.pyplot as plt 
import numpy as np


nb_fichier = 1
continuer = True
while continuer==True:
    print('Entrez le nom du'+' fichier'+ str(nb_fichier)+':')
    nom = input()
    if nom !='':
        with open(nom+'.dat','r') as datFile:
            donnée = [data.split() for data in datFile]
        exec('x'+str(nb_fichier)+'=[]')
        exec('y'+str(nb_fichier)+'=[]')
        for i in range (len(donnée)-1):
            exec('x'+str(nb_fichier)+'.append(float(donnée['+str(i)+'][0]))')
            exec('y'+str(nb_fichier)+'.append(float(donnée['+str(i)+'][1]))')
        nb_fichier+=1
    else:
        continuer = False
    


point_intersection = [[0],[0]]
courbe_inf_int = []

def comparaison_point(y1,y2,x1,x2):
    if y1[0] < y2[0]:
        courbe_inf = 1
        courbe_inf_int.append(1)
    elif y1[0]> y2[0]:
        courbe_inf = 2
        courbe_inf_int.append(2)
    else:
        courbe_inf=0
        
    
    for i in range(len(y1)-2):
        if y1[i+1] < y2[i+1]:
            if courbe_inf == 2:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1])
                courbe_inf = 1
                courbe_inf_int.append(1)
            if courbe_inf == 0:
                courbe_inf = 1
                courbe_inf_int.append(1)
        elif y1[i+1] == y2[i+1]:
            point_intersection[0].append(i+1)
            point_intersection[1].append(y1[i+1])
            courbe_inf == 0
        else : 
            if courbe_inf == 1:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1])
                courbe_inf_int.append(2)
                courbe_inf = 2
            if courbe_inf == 0:
                courbe_inf = 2
                courbe_inf_int.append(2)
    


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


for i in range(1,nb_fichier-1):
    for j in range(i+1,nb_fichier):
        exec('comparaison_point(y'+str(i)+',y'+str(j)+',x'+str(i)+',x'+str(j)+')')

with open("point_d'intersection.dat","w")as fichier:
    for i in range(len(point_intersection[0])-1):
        fichier.write(str(point_intersection[0][i])+' '+str(point_intersection[1][i]))

for i in range(1,nb_fichier):
    exec('plt.plot(x'+ str(i)+',y'+str(i)+')')


plt.plot(point_intersection[0],point_intersection[1], 'ro')

plt.show()