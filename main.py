
jeu1 = [1,4,6,3,7,2,5]

jeu2 = [2,5,3,4,8,4,6]

point_intersection = []

def comparaison_point():
    if jeu1[0] < jeu2[0]:
        courbe_inf = 1
    elif jeu1[0]> jeu2[0]:
        courbe_inf = 2
    else:
        courbe_inf=0
    
    for i in range(len(jeu1)-2):
        if jeu1[i+1] < jeu2[i+1]:
            if courbe_inf == 2:
                intersection(jeu1[i], jeu2[i], jeu1[i+1], jeu2[i+1],i)
                courbe_inf = 1
            if courbe_inf == 0:
                courbe_inf = 1
        elif jeu1[i+1] == jeu2[i+1]:
            point_intersection.append([i+1, jeu1[i+1]])
            courbe_inf == 0
        else : 
            if courbe_inf == 1:
                intersection(jeu1[i], jeu2[i], jeu1[i+1], jeu2[i+1],i)
                courbe_inf = 2
            if courbe_inf == 0:
                courbe_inf = 2
    


def intersection(y1n, y2n, y1n1, y2n1,x):
    #Recherche des fonction affines
    a1 = (y1n1-y1n)/(x+1-x)
    a2 = (y2n1-y2n)/(x+1-x)
    b1 = y1n - a1 * x
    b2 = y2n - a2 * x
    #Recherche du point d'intersection
    x_int = (b2-b1)/(a1-a2)
    y_int = (a1*b2-b1*a2)/(a1-a2)
    point_intersection.append([x_int,y_int])

comparaison_point()
print(point_intersection)