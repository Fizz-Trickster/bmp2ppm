# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:57:42 2022

@author: yoonys
"""

import numpy as np

import time

import paramBMP

# ========================================
# Function
# ========================================


def hex2dec(hexVar):
  decVar = int(hexVar, 16)

  return decVar


def getBMPHeader(bmpHexData):
  dict_Header                     = {}

  dict_Header['bfType']           = bmpHexData[paramBMP.para['BFTYPE_START_ADDR'] : paramBMP.para['BFTYPE_END_ADDR']]
  dict_Header['bfSize']           = bmpHexData[paramBMP.para['BFSIZE_START_ADDR'] : paramBMP.para['BFSIZE_END_ADDR']]
  dict_Header['bfReserved1']      = bmpHexData[paramBMP.para['BFRES1_START_ADDR'] : paramBMP.para['BFRES1_END_ADDR']]
  dict_Header['bfReserved2']      = bmpHexData[paramBMP.para['BFRES2_START_ADDR'] : paramBMP.para['BFRES2_END_ADDR']]
  dict_Header['bfOffBits']        = bmpHexData[paramBMP.para['BFOFFS_START_ADDR'] : paramBMP.para['BFOFFS_END_ADDR']]
  dict_Header['biSize']           = bmpHexData[paramBMP.para['BISIZE_START_ADDR'] : paramBMP.para['BISIZE_END_ADDR']]
  dict_Header['biHres']           = bmpHexData[paramBMP.para['BIHRES_START_ADDR'] : paramBMP.para['BIHRES_END_ADDR']]
  dict_Header['biVres']           = bmpHexData[paramBMP.para['BIVRES_START_ADDR'] : paramBMP.para['BIVRES_END_ADDR']]
  dict_Header['biPlanes']         = bmpHexData[paramBMP.para['BIPLAN_START_ADDR'] : paramBMP.para['BIPLAN_END_ADDR']]
  dict_Header['biBitCount']       = bmpHexData[paramBMP.para['BIBITC_START_ADDR'] : paramBMP.para['BIBITC_END_ADDR']]
  dict_Header['biCompression']    = bmpHexData[paramBMP.para['BICOMP_START_ADDR'] : paramBMP.para['BICOMP_END_ADDR']]
  dict_Header['biSizeImage']      = bmpHexData[paramBMP.para['BISIMG_START_ADDR'] : paramBMP.para['BISIMG_END_ADDR']]
  dict_Header['biXPelsPerMeter']  = bmpHexData[paramBMP.para['BIXPEL_START_ADDR'] : paramBMP.para['BIXPEL_END_ADDR']]
  dict_Header['biYPelsPerMeter']  = bmpHexData[paramBMP.para['BIYPEL_START_ADDR'] : paramBMP.para['BIYPEL_END_ADDR']]
  dict_Header['biClrUsed']        = bmpHexData[paramBMP.para['BICLRU_START_ADDR'] : paramBMP.para['BICLRU_END_ADDR']]
  dict_Header['biClrImportant']   = bmpHexData[paramBMP.para['BICLRI_START_ADDR'] : paramBMP.para['BICLRI_END_ADDR']]

  # decode
  dict_Header['Offset']           = getDecodeData(dict_Header['bfOffBits']  , paramBMP.para['BFOFFS_BYTE_SIZE'])
  dict_Header['Hres']             = getDecodeData(dict_Header['biHres']     , paramBMP.para['BIHRES_BYTE_SIZE'])
  dict_Header['Vres']             = getDecodeData(dict_Header['biVres']     , paramBMP.para['BIVRES_BYTE_SIZE'])

  return dict_Header


def getDecodeData(i_data, BYTE_SIZE):
  o_data = ""
  for idx in range(0, BYTE_SIZE):
    o_data = i_data[2*idx:2*(idx+1)] + o_data

  return hex2dec(o_data)


# ========================================
# main
# ========================================
start = time.time()

#i_filePath = './image/24bpp-320x240.bmp'
#i_filePath = './image/flag.bmp'
i_filePath = './image/lena.bmp'
i_fileName = i_filePath.split('/')[-1].split('.')[0]
file = open(i_filePath, 'rb')

bindata = file.read()
strdata = bindata.hex()

bfHeader = getBMPHeader(strdata)

pixData = strdata[2*bfHeader['Offset']:]

R = []
G = []
B = []
print(len(pixData))

for idx in range(0, len(pixData), 2):
  data = pixData[idx:idx+2]       
  if idx % 3 == 0:
    B.append(hex2dec(data))
  elif idx % 3 == 1:
    R.append(hex2dec(data))
  else :
    G.append(hex2dec(data))

Rdata_1d = np.array(R)
Gdata_1d = np.array(G)
Bdata_1d = np.array(B)

Rdata_2d = Rdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])
Gdata_2d = Gdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])
Bdata_2d = Bdata_1d.reshape(bfHeader['Vres'], bfHeader['Hres'])

Rdata_2d_rev = np.flip(Rdata_2d, axis=0)
Gdata_2d_rev = np.flip(Gdata_2d, axis=0)
Bdata_2d_rev = np.flip(Bdata_2d, axis=0)


o_filePath = i_fileName + '.ppm'
ppmFile = open(o_filePath, 'w')

ppmFile.write('P3\n')
ppmFile.write('{0} {1}\n'.format(bfHeader['Hres'], bfHeader['Vres']))
ppmFile.write('255\n')

for Vidx in range(0, bfHeader['Vres']):
  for Hidx in range(0, bfHeader['Hres']):
    ppmFile.write('{0} {1} {2}\n'.format(Rdata_2d_rev[Vidx][Hidx], Gdata_2d_rev[Vidx][Hidx], Bdata_2d_rev[Vidx][Hidx]))
    

end = time.time()
print('processing time  = {0:0.5f} sec'.format(end-start))

file.close()
ppmFile.close()
