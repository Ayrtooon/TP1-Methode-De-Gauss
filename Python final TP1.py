# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:00:01 2021

@author: Wealif
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from bibliotheque import *

menu_choix = 0


# Lancement du programme
#AffichageMenu()

print("------------------------------------------------------------------------------------------------------------------------------------")
print("                             TP1 - Méthode de Gauss pour la résolution de systèmes linéaires                                        ")
print("------------------------------------------------------------------------------------------------------------------------------------")

while True:
    menu_choix = int(input("Rentrez votre choix ( valeur entre 1-4): \n 1- Vérifier une méthode de résolution \n 2- Résolution de AX=B avec 2 matrices aléatoires\n 3- Créer 3 tableaux excels (indices/normes/incertitudes) \n 4- Sortie\n\n Reponse :\n"))
    if menu_choix == 1:
        
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Vérifier l'agorithme de Gauss \n 2- Vérifier la résolution LU\n 3- Illustration de la méthode du pivot partiel\n 4- Vérifier la méthode du pivot total \n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1:
            A = np.array([[3,2,-1,4],[-3,-4,4,-2],[6,2,2,7],[9,4,2,18]])
            B = np.array([[4],[-5],[-2],[13]])
            print("A= \n", A)
            print("B= \n", B)
            print("la réponse doit être [-1. -2. -3. 2.]")
            print("on obtient avec la méthode de Gauss:")
            print(Gauss(A,B))
    
        elif menu_choix == 2:
            A = np.array([[3,2,-1,4],[-3,-4,4,-2],[6,2,2,7],[9,4,2,18]])
            B = np.array([[4],[-5],[-2],[13]])
            print("A= \n", A)
            print("B= \n", B)
            print("la réponse doit être [-1. -2. -3. 2.]")
            print("on obtient avec la résolution LU:")
            [L,U] = DecompositionLU(A)
            print(resolutionLU(L,U,B))
    
        elif menu_choix == 3:
            A = np.array([[3,2,-1,4],[-3,-4,4,-2],[6,2,2,7],[9,4,2,18]])
            B = np.array([[4],[-5],[-2],[13]])
            print("et on obtient avec la méthode du pivot partiel:")
            print("la réponse doit être \n [[ 9 4 2 18 13]\n [ 0 -2 4 4 0] \n [ 0  0 -1 -2 0] \n [ 0 0 0 -5 -10]]")
            GaussChoixPivotPartiel(A,B)
    
        elif menu_choix == 4:
            A = np.array([[0,2,3],[4,5,6],[7,8,9]])
            B = np.array([[1],[2],[3]])
            print("A= \n", A)
            print("B= \n", B)
            print("la réponse doit être  [0,0,1/3] tandis que la resolution de ce système est impossible par la méthode de Gauss")
            print("et on obtient avec la méthode du pivot total")
            print(GaussChoixPivotTotal(A,B))
    
        elif menu_choix == 5:
            break
    
    elif menu_choix == 2:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Résolution aléatoire via l'agorithme de Gauss \n 2- Résolution aléatoire via la résolution LU\n 3- Résolution aléatoire via la méthode du pivot partiel\n 4- Résolution aléatoire via la méthode du pivot total \n 5- Sortie\n\n Reponse :\n"))
        lim_up=100
        lim_down=-100 
        n=10 #Taille de la matrice
        A = np.random.randint(low=lim_down, high = lim_up, size = (n,n))
        B = np.random.randint(low=lim_down, high = lim_up, size = (n,1))
        
        
        if menu_choix == 1:
            print("on obtient avec la méthode de Gauss:")
            print(Gauss(A,B))
    
        elif menu_choix == 2:
            print("on obtient avec la résolution LU:")
            [L,U] = DecompositionLU(A)
            print(resolutionLU(L,U,B))
    
        elif menu_choix == 3:
            print("et on obtient avec la méthode du pivot partiel:")
            print(GaussChoixPivotPartiel(A,B))
    
        elif menu_choix == 4:
            print("et on obtient avec la méthode du pivot total")
            print(GaussChoixPivotTotal(A,B))
    
        elif menu_choix == 5:
            break

    elif menu_choix == 3:
        
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Valeurs pour l'agorithme de Gauss \n 2- Valeurs pour la résolution LU\n 3- Valeurs pour la méthode du pivot partiel\n 4- Valeurs la méthode du pivot total \n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1:
            print("on obtient avec la méthode de Gauss:")
            temps=[] 
            indices=[]
            normes=[]
            for n in range (0,200,2):
                print(n)
                try :
                     A = np.random.randint(low=0,high=n,size=(n,n))
                     B = np.random.randint(low=0,high=n,size=(n,n))
                     t1 = time.time()
                     x = Gauss(A,B)
                     print(x)
                     t2 = time.time()
                     t = t2 - t1
                     temps.append(t)
                     indices.append(n)
                     norme = np.linalg.norm(A@x-B)
                     normes.append(norme)
            
                    
                except :
                     print('')
                   
            
            df = pd.DataFrame(temps)
            df.to_csv('temps.csv',index=False)
            
            df2 = pd.DataFrame(indices)
            df2.to_csv('indices.csv',index=False)
            
            df3 = pd.DataFrame(normes)
            df3.to_csv('normes.csv',index=False)
            
            print("les fichiers excels sont prêts")


        elif menu_choix == 2:
            print("on obtient avec la résolution LU:")
            temps=[] 
            indices=[]
            normes=[]
            for n in range (0,200,2):
                print(n)
                try :
                     A = np.random.randint(low=0,high=n,size=(n,n))
                     B = np.random.randint(low=0,high=n,size=(n,n))
                     t1 = time.time()
                     [L,U] = DecompositionLU(A)
                     x = resolutionLU(L,U,B)
                     print(x)
                     t2 = time.time()
                     t = t2 - t1
                     temps.append(t)
                     indices.append(n)
                     norme = np.linalg.norm(A@x-B)
                     normes.append(norme)
            
                    
                except :
                     print('')
                   
            
            df = pd.DataFrame(temps)
            df.to_csv('temps.csv',index=False)
            
            df2 = pd.DataFrame(indices)
            df2.to_csv('indices.csv',index=False)
            
            df3 = pd.DataFrame(normes)
            df3.to_csv('normes.csv',index=False)
            
            print("les fichiers excels sont prêts")

    
        elif menu_choix == 3:
            print("et on obtient avec la méthode du pivot partiel:")
            temps=[] 
            indices=[]
            normes=[]
            for n in range (0,200,2):
                print(n)
                try :
                     A = np.random.randint(low=0,high=n,size=(n,n))
                     B = np.random.randint(low=0,high=n,size=(n,n))
                     t1 = time.time()
                     x = GaussChoixPivotPartiel(A,B)
                     print(x)
                     t2 = time.time()
                     t = t2 - t1
                     temps.append(t)
                     indices.append(n)
                     norme = np.linalg.norm(A@x-B)
                     normes.append(norme)
            
                    
                except :
                     print('')
                   
            
            df = pd.DataFrame(temps)
            df.to_csv('temps.csv',index=False)
            
            df2 = pd.DataFrame(indices)
            df2.to_csv('indices.csv',index=False)
            
            df3 = pd.DataFrame(normes)
            df3.to_csv('normes.csv',index=False)
            
            print("les fichiers excels sont prêts")
            GaussChoixPivotPartiel(A,B)
    
    
        elif menu_choix == 4:
            print("et on obtient avec la méthode du pivot total")
            temps=[] 
            indices=[]
            normes=[]
            for n in range (0,200,2):
                print(n)
                try :
                     A = np.random.randint(low=0,high=n,size=(n,n))
                     B = np.random.randint(low=0,high=n,size=(n,n))
                     t1 = time.time()
                     x = GaussChoixPivotTotal(A,B)
                     print(x)
                     t2 = time.time()
                     t = t2 - t1
                     temps.append(t)
                     indices.append(n)
                     norme = np.linalg.norm(A@x-B)
                     normes.append(norme)
            
                    
                except :
                     print('')
                   
            
            df = pd.DataFrame(temps)
            df.to_csv('temps.csv',index=False)
            
            df2 = pd.DataFrame(indices)
            df2.to_csv('indices.csv',index=False)
            
            df3 = pd.DataFrame(normes)
            df3.to_csv('normes.csv',index=False)
            
            print("les fichiers excels sont prêts")
            GaussChoixPivotPartiel(A,B)
            GaussChoixPivotTotal(A,B)
    
        elif menu_choix == 5:
            break

    elif menu_choix == 4:
        break

print("Nous espérons que cela vous a plu ;) ")
print("Au revoir")

