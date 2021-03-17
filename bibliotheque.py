# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:29:29 2021

@author: Wealif
"""

import time
import numpy as np 
from matplotlib import pyplot as plt
import math as m
import pandas as pd


#PARTIE 2
#----------------------------------------------------------------------------------------------------------------------
#Question 1
def ReductionGauss(Aaug):
    n,m = np.shape(Aaug)   # On fait apparaître la taille de la matrice avec n les lignes et m les colonnes
    for k in range(0,n-1):
        for i in range(k+1,n):
            gik = Aaug[i,k]/Aaug[k,k]  
            Aaug[i,:] = Aaug[i,:] - (gik*Aaug[k,:])  
            
    return(Aaug)
    
   #----------------------------------------------------------------------------------------------------------------------
#Question 2
def ResolutionSystTriSup(Taug):
    n,m = np.shape(Taug)
    X = np.zeros(n)
    for i in range(n-1,-1,-1):
        somme = 0
        for j in range(i,n-1):
            somme += Taug[i,j]*X[j]
        X[i] = (Taug[i,n]-somme)/Taug[i,i]
    
    return(X)

#----------------------------------------------------------------------------------------------------------------------
#Question 3
def Gauss(A,B):
    Aaug = np.concatenate((A,B.T),axis=1)
    
    Taug = ReductionGauss(Aaug)
    
    sol = ResolutionSystTriSup(Taug)
    
    print(sol)
    
    return(sol)



#PARTIE 3
#----------------------------------------------------------------------------------------------------------------------
#Question 1
def DecompositionLU(A):
    gik_val = []
    n,m = np.shape(A) 
    for k in range (0, n-1):
        for i in range (k+1, n):
            gik = A[i,k]/A[k,k]
            gik_val.append(gik)
            A[i,:]= A[i,:] - gik*A[k,:]
  
    U=A
    L=np.zeros((n,n))
    n,m = np.shape (A)
    
    k=0
    for i in range (0,n):
        L[i,i] = 1 

        
    ligne = 0
    for k in range (0,n-1):
        for i in range(k+1, n):
            L[i,k] = gik_val[ligne]#On a stocké toutes les valeurs de gik dans une liste, puis on les remplace
            ligne = ligne + 1
    return L,U


#----------------------------------------------------------------------------------------------------------------------
#Question 2
def resolutionLower(Aaug):
    #Solveur d'équations matricielles avec une matrice triangulaire inférieure
    n,m = np.shape(Aaug)
    Y = np.zeros(n)
    for i in range (0,n):
        somme = 0
        for k in range(0,n):
            somme = somme + Y[k]*Aaug[i,k]
        Y[i] = (Aaug[i,n] - somme)/Aaug[i,i]
    return Y

#----------------------------------------------------------------------------------------------------------------------
def resolutionLU(L,U,B):
    n,m = np.shape(B)
    Aaug = np.concatenate((L,B), axis=1)#Concatenation L et B
    Y = np.reshape(resolutionLower(Aaug), (n,1))#résoudre equation LY=b avec res(Aaug = LB)
    Aaug = np.concatenate((U,Y), axis = 1)#concatenation U et Y
    X = ResolutionSystTriSup(Aaug)#Résoudre UX=Y avec res(Aaug=UY)
    return X


#Partie 4
#----------------------------------------------------------------------------------------------------------------------
#Question 1
def GaussChoixPivotPartiel(A,B):

    Aaug = np.concatenate((A,B),axis=1)
    n,m = np.shape(Aaug)
    print('\n',Aaug,'\n')
    
    for k in range(n):
        for i in range(0,n-k):
            pivotmax = abs(Aaug[i+k,k])
            if abs(Aaug[k,k])<pivotmax:
                imax = Aaug[k,:].copy()
                Aaug[k,:] = Aaug[i+k,:]
                Aaug[i+k,:] = imax
                print('\n',Aaug)
        for i in range(k+1,n):
            gik = Aaug[i,k]/Aaug[k,k]
            Aaug[i,:] = Aaug[i,:]-gik*Aaug[k,:]
        print('\n',Aaug) #Montrer les étapes
    print('\n',Aaug)
    return(Aaug)
  
#----------------------------------------------------------------------------------------------------------------------    
#Question 2
def GaussChoixPivotTotal(A,B):
    Aaug = np.concatenate((A,B),axis=1)
    n,m = np.shape(Aaug)
    #print('\n',Aaug,'\n')
    
    transf_colonne = []
    transf_ligne = []
    
    for k in range(0,len(Aaug)):
        
        pivotmax = abs(Aaug[k,k])
        
        for k1 in range(k,len(Aaug)):
            for i in range(k,len(Aaug)):
                
                if abs(Aaug[i,k1])>=pivotmax:
                    pivotmax=abs(Aaug[i,k1])
                    ligne_max = i
                    colonne_max = k1
                    
        transf_colonne.append([k,colonne_max])
        transf_ligne.append([k,ligne_max])
        
        new = Aaug[k].copy()
        Aaug[k] = Aaug[ligne_max]
        Aaug[ligne_max] = new
        
        for i in range(0,len(Aaug)):
            
            new2 = Aaug[i,k].copy()
            Aaug[i,k] = Aaug[i,colonne_max]
            Aaug[i,colonne_max] = new2
            
        for j in range(k+1, len(Aaug)):
            gik = Aaug[j,k]/Aaug[k,k]
            Aaug[j,:] = Aaug[j,:] - gik*Aaug[k,:]
            

    X = np.reshape(ResolutionSystTriSup(Aaug),(n,1))

    for i in range(len(transf_colonne)-1,-1,-1):
        if transf_colonne[i][0]!=transf_colonne[i][1]:
            new=X[transf_colonne[i][0],0]
            X[transf_colonne[i][0],0]=X[transf_colonne[i][1],0]
            X[transf_colonne[i][1],0]=new
    return(X)