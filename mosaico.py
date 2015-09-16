# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:59:03 2015

@author: rodrigo
"""

import numpy as np
import cv2
import os
import math

entrada = "lenna.png"
fatorDiv = 160

strEntrada = "inputs/" + entrada

img = cv2.imread(strEntrada, 1)

novaL = img.shape[0]/fatorDiv*fatorDiv
novaA = img.shape[1]/fatorDiv*fatorDiv

img = img[0:novaL,0:novaA]

matrizMediasImg = np.zeros((fatorDiv, fatorDiv, 3))
mediaBanco = []
arrayDistancia = []

def calculaMediaInput():

    for i in range((int(img.shape[0]/fatorDiv))*fatorDiv):
        for j in range((int(img.shape[1]/fatorDiv))*fatorDiv):
            matrizMediasImg[i//(img.shape[0]/fatorDiv)][j//(img.shape[1]/fatorDiv)][0] += img[i][j][0]
            matrizMediasImg[i//(img.shape[0]/fatorDiv)][j//(img.shape[1]/fatorDiv)][1] += img[i][j][1]
            matrizMediasImg[i//(img.shape[0]/fatorDiv)][j//(img.shape[1]/fatorDiv)][2] += img[i][j][2]
            
    max = 0
    for i in range(matrizMediasImg.shape[0]):
        for j in range(matrizMediasImg.shape[1]):    
            if (matrizMediasImg[i][j][0] > max):
                max = matrizMediasImg[i][j][0]
            
            if (matrizMediasImg[i][j][1] > max):
                max = matrizMediasImg[i][j][1]
                
            if (matrizMediasImg[i][j][2] > max):
                max = matrizMediasImg[i][j][2]

    for i in range(matrizMediasImg.shape[0]):
        for j in range(matrizMediasImg.shape[1]):  
            matrizMediasImg[i][j] = matrizMediasImg[i][j]/max*256
                



def calculaMediaBanco():
    arrayDiretorios = sorted(os.listdir("banco/"))
    
    for i in range(len(arrayDiretorios)):
        mediaBanco.append([0,0,0])
        
        dirB = "banco/" + arrayDiretorios[i]        
        imgB = cv2.imread(dirB, 1)
        
        for j in range(imgB.shape[0]):
            for k in range(imgB.shape[1]):
                mediaBanco[i][0] += imgB[j][k][0]
                mediaBanco[i][1] += imgB[j][k][1]
                mediaBanco[i][2] += imgB[j][k][2]
                
        mediaBanco[i][0] = mediaBanco[i][0]/(imgB.shape[0]*imgB.shape[1])
        mediaBanco[i][1] = mediaBanco[i][1]/(imgB.shape[0]*imgB.shape[1])
        mediaBanco[i][2] = mediaBanco[i][2]/(imgB.shape[0]*imgB.shape[1])
        
    np.savetxt('dados/banco', mediaBanco)
    
def lerMediaBanco():
    return np.loadtxt('dados/banco')
    
def calculaDistancia(x, y):
    global arrayDistancia
    arrayDistancia = []
    
    for i in range(len(mediaBanco)):
        
        
        dist = math.sqrt(pow((matrizMediasImg[x][y][0]-mediaBanco[i][0]),2) + pow((matrizMediasImg[x][y][1]-mediaBanco[i][1]),2) + pow((matrizMediasImg[x][y][2]-mediaBanco[i][2]),2))
        arrayDistancia.append(dist)

    
def encontraMinDistancia():
    menorDist = min(arrayDistancia)
    indMenorDist = arrayDistancia.index(menorDist)  
    
    
    return indMenorDist
    
    
def adicionaImg(x,y):
    end = sorted(os.listdir("banco/"))
    end = end[encontraMinDistancia()]
    end = "banco/" + end
    
    imgL = cv2.imread(end, 1)
    imgL = cv2.resize(imgL, (img.shape[1]/fatorDiv, img.shape[0]/fatorDiv))
    
    for i in range(img.shape[0]/fatorDiv):
        for j in range(img.shape[1]/fatorDiv):            
            img[(img.shape[0]/fatorDiv)*x+i][(img.shape[1]/fatorDiv)*y+j][0] = imgL[i][j][0]
            img[(img.shape[0]/fatorDiv)*x+i][(img.shape[1]/fatorDiv)*y+j][1] = imgL[i][j][1]
            img[(img.shape[0]/fatorDiv)*x+i][(img.shape[1]/fatorDiv)*y+j][2] = imgL[i][j][2]            

        
def criaMosaico():
    for i in range(fatorDiv):
        for j in range(fatorDiv):
            calculaDistancia(i,j)
            adicionaImg(i,j)

calculaMediaInput()

mediaBanco = lerMediaBanco()

criaMosaico()


cv2.imshow('output', img)

nome = entrada.split(".")[0]
extensao = entrada.split(".")[1]
strSaida = "outputs/" + nome + str(fatorDiv) + "." + extensao


cv2.imwrite(strSaida, img)

cv2.waitKey(0)
cv2.destroyAllWindows()