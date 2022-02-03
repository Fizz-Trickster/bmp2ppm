# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:57:42 2022

@author: yoonys
"""

import numpy as np

import paramBMP

# ========================================
# Function
# ========================================


def hex2dec(hexVar):
  decVar = int(hexVar, 16)

  return decVar


def getBMPHeader(bmpHexData):
  dict_Header                 = {}

  dict_Header['bfType']       = bmpHexData[paramBMP.para['BFTYPE_START_ADDR'] : paramBMP.para['BFTYPE_END_ADDR']]
  dict_Header['bfSize']       = bmpHexData[paramBMP.para['BFSIZE_START_ADDR'] : paramBMP.para['BFSIZE_END_ADDR']]
  dict_Header['bfReserved1']  = bmpHexData[paramBMP.para['BFRES1_START_ADDR'] : paramBMP.para['BFRES1_END_ADDR']]
  dict_Header['bfReserved2']  = bmpHexData[paramBMP.para['BFRES2_START_ADDR'] : paramBMP.para['BFRES2_END_ADDR']]
  dict_Header['bfOffBits']    = bmpHexData[paramBMP.para['BFOFFS_START_ADDR'] : paramBMP.para['BFOFFS_END_ADDR']]
  dict_Header['biSize']       = bmpHexData[paramBMP.para['BISIZE_START_ADDR'] : paramBMP.para['BISIZE_END_ADDR']]
  dict_Header['biHres']       = bmpHexData[paramBMP.para['BIHRES_START_ADDR'] : paramBMP.para['BIHRES_END_ADDR']]
  dict_Header['biVres']       = bmpHexData[paramBMP.para['BIVRES_START_ADDR'] : paramBMP.para['BIVRES_END_ADDR']]

  # decode
  dict_Header['Offset']       = getDecodeData(dict_Header['bfOffBits']  , paramBMP.para['BFOFFS_BYTE_SIZE'])
  dict_Header['Hres']         = getDecodeData(dict_Header['biHres']     , paramBMP.para['BIHRES_BYTE_SIZE'])
  dict_Header['Vres']         = getDecodeData(dict_Header['biVres']     , paramBMP.para['BIVRES_BYTE_SIZE'])

  return dict_Header


def getDecodeData(i_data, BYTE_SIZE):
  o_data = ""
  for idx in range(0, BYTE_SIZE):
    o_data = i_data[2*idx:2*(idx+1)] + o_data

  return hex2dec(o_data)


# ========================================
# main
# ========================================

# file = open('./image/flag.bmp', 'rb')
# file = open('./image/lena.bmp', 'rb')
file = open('./image/24bpp-320x240.bmp', 'rb')

bindata = file.read()
strdata = bindata.hex()

bfHeader = getBMPHeader(strdata)

pixData = strdata[2*bfHeader['Offset']:]

R = []
G = []
B = []
print(len(pixData))
for idx in range(0, int(len(pixData)/6)):
  b, pixData = pixData[:2], pixData[2:]
  g, pixData = pixData[:2], pixData[2:]
  r, pixData = pixData[:2], pixData[2:]
  R.append(hex2dec(r))
  G.append(hex2dec(g))
  B.append(hex2dec(b))

Rdata_1d = np.array(R)
Gdata_1d = np.array(G)
Bdata_1d = np.array(B)

Rdata_2d = Rdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])
Gdata_2d = Gdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])
Bdata_2d = Bdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])

Rdata_2d_rev = np.flip(Rdata_2d, axis=0)
Gdata_2d_rev = np.flip(Gdata_2d, axis=0)
Bdata_2d_rev = np.flip(Bdata_2d, axis=0)

ppmFile = open('./output.ppm', 'w')

ppmFile.write('P3\n')
ppmFile.write('{0} {1}\n'.format(bfHeader['Hres'], bfHeader['Vres']))
ppmFile.write('255\n')

for Vidx in range(0,bfHeader['Vres']):
  for Hidx in range(0, bfHeader['Hres']):
    ppmFile.write('{0} {1} {2}\n'.format(Rdata_2d_rev[Vidx][Hidx], Gdata_2d_rev[Vidx][Hidx], Bdata_2d_rev[Vidx][Hidx]))
    
  
# hex to ascii
l = chr(hex2dec(bfHeader['bfType'][:2]))
m = chr(hex2dec(bfHeader['bfType'][2:]))
print(l+m)


listData = list(strdata)

a = np.array(listData)
b = a.reshape(-1, 2)
print(b[0])
print(type(b[0]), type(b[0][0]))

file.close()
ppmFile.close()
