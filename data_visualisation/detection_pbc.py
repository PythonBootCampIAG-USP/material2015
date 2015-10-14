# -*- coding: utf-8 -*-
import pyfits
import matplotlib.pylab as plt
import numpy as np
import glob
from os.path import isfile

################################################################
def read_bias(): 
      """Lê os bias da pasta ./bias e retorna a mediana dos bias"""
      files = glob.glob("bias/*.fits")
      files = np.sort(files)
      hduu = []
      data = []
      for i in range(len(files)):
         hduu.append(pyfits.open(files[i]))
         data.append(hduu[i][0].data)
      mdata = np.median(data,axis=0) #tirando mediana
      copy_data(data[0],mdata)
      hduu[0].writeto("bias/bias_final.fits")
      return mdata
################################################################
def read_flat(bias,colour):
   """le os flats de uma cor e retorna usa média corrigida pelo bias"""
   files = glob.glob("flat/"+colour)
   files = np.sort(files)
   hduu = []
   data = []
   for i in range(len(files)):
      hduu.append(pyfits.open(files[i]))
      data.append(hduu[i][0].data)
   meandata = np.mean(data,axis=0) - bias
   meandata = meandata/np.median(meandata) #Flat tem que ser uma contribuição unitária
   return meandata
################################################################
def copy_data(data1,data2):
   """Copia data2 em data1"""
   for i in range(len(data1)):
      for j in range(len(data1[0])):
         data1[i][j] = data2[i][j]
################################################################
def read_data(colour):
   """le os flats de uma cor e retorna usa média corrigida pelo bias"""
   files = glob.glob("dados/"+colour)
   files = np.sort(files)
   hduu = []
   data = []
   for i in range(len(files)):
      hduu.append(pyfits.open(files[i]))
      data.append(hduu[i][0].data)
   return hduu,data
################################################################
def correction(data,flat,bias): 
   """corrige flat e bias de um conjunto de imagens"""
   for i in range(len(data)):
      data[i] = data[i] - bias
      data[i] = data[i] / flat
   return data
################################################################
def image_stack(hdu,data): 
   """junta todas as imagens obtidas (já deve ter sido usado o imalign)"""
   new = data[0]
   for i in range(len(data)-1):
      new += data[i+1]
   return hdu[0],new
################################################################
def reduction(colour,bias):
   """faz a redução da imagem e salva o fits"""
   flat = read_flat(bias,"flat_"+colour+"*")
   print "Flat "+colour+" pronto!"

   hdu,data = read_data("n6242_"+colour+"*")
   data = correction(data,flat,bias)
   nhdu,new = image_stack(hdu,data)
   nhdu[0].writeto(colour+"_final.fits")
   print "Stack "+colour+" pronto!"
   return nhdu
################################################################
bias = read_bias()
print "Bias pronto!"
hduU = reduction("U",bias)
print "ok!"
