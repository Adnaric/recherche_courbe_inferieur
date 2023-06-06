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
    

for i in range(1,nb_fichier-1):
    for j in range(i+1, nb_fichier):
        exec('point_intersection_'+str(i)+'_et_'+str(j)+'= [[0],[0]]')

for i in range(1,nb_fichier-1):
    for j in range(i+1, nb_fichier):
        exec('courbe_inf_int_'+str(i)+'_et_'+str(j)+'= []')


def comparaison_point(y1,y2,x1,x2,num_courbe1, num_courbe2):
    if y1[0] < y2[0]:
        courbe_inf = 1
        exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(1)')
    elif y1[0]> y2[0]:
        courbe_inf = 2
        exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(2)')
    else:
        courbe_inf=0
        
    
    for i in range(len(y1)-2):
        if y1[i+1] < y2[i+1]:
            if courbe_inf == 2:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1],num_courbe1,num_courbe2)
                courbe_inf = 1
                exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(1)')
            if courbe_inf == 0:
                courbe_inf = 1
                exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(1)')
        elif y1[i+1] == y2[i+1]:
            exec('point_intersection_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'[0].append(i+1)')
            exec('point_intersection_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'[1].append(y1[i+1])')
            courbe_inf == 0
        else : 
            if courbe_inf == 1:
                intersection(y1[i], y2[i], y1[i+1], y2[i+1],x1[i],x1[i+1],num_courbe1,num_courbe2)
                exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(2)')
                courbe_inf = 2
            if courbe_inf == 0:
                courbe_inf = 2
                exec('courbe_inf_int_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'.append(2)')
    


def intersection(y1n, y2n, y1n1, y2n1,x,xn1, num_courbe1,num_courbe2):
    #Recherche des fonction affines
    a1 = (y1n1-y1n)/(xn1-x)
    a2 = (y2n1-y2n)/(xn1-x)
    b1 = y1n - a1 * x
    b2 = y2n - a2 * x
    #Recherche du point d'intersection
    x_int = (b2-b1)/(a1-a2)
    y_int = (a1*b2-b1*a2)/(a1-a2)
    exec('point_intersection_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'[0].append(x_int)')
    exec('point_intersection_'+str(num_courbe1)+'_et_'+str(num_courbe2)+'[1].append(y_int)')


for i in range(1,nb_fichier-1):
    for j in range(i+1,nb_fichier):
        exec('comparaison_point(y'+str(i)+',y'+str(j)+',x'+str(i)+',x'+str(j)+','+str(i)+','+str(j)+')')


 
premiere_ligne = ''
for i in range(1,nb_fichier-1):
    for j in range(i+1,nb_fichier):
        exec("premiere_ligne += 'Courbe_"+str(i)+"_"+str(j)+"\t\t\t'")

with open("point_d'intersection.dat","w")as fichier:
    fichier.write(premiere_ligne+'\n')
    deuxieme_ligne = ''
    for i in range(1,nb_fichier-1):
        for j in range(i+1,nb_fichier):
            deuxieme_ligne+='x\ty\t'
    fichier.write(deuxieme_ligne+'\n')
    k=0
    l = 0
    ligne = ''
    while k < 5:
        for i in range(1,nb_fichier-1):
            for j in range(i+1,nb_fichier):

                exec("if len(point_intersection_"+str(i)+"_et_"+str(j)+"[0])-1>l: ligne +=str(point_intersection_"+str(i)+"_et_"+str(j)+"[0][l-2])+'\t'+str(point_intersection_"+str(i)+"_et_"+str(j)+"[1][l-2])+'\t'")
                    #exec("ligne +=str(point_intersection_"+str(i)+"_et_"+str(j)"[0][l])+'  '+str(point_intersection_"+str(i)+"_et_"+str(j)"[1][l])+' '")
                exec("if len(point_intersection_"+str(i)+"_et_"+str(j)+"[0])-1<l: ligne+='\t\t\t\t'; k+=1")
        l +=1
        fichier.write(ligne+'\n')        


        



for i in range(1,nb_fichier):
    exec('plt.plot(x'+ str(i)+',y'+str(i)+')')

for i in range(1,nb_fichier-1):
    for j in range(i+1,nb_fichier):
        exec("plt.plot(point_intersection_"+str(i)+"_et_"+str(j)+"[0],point_intersection_"+str(i)+"_et_"+str(j)+"[1],'ro')")



plt.show()