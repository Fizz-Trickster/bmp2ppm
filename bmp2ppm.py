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

# ========================================
# main
# ========================================
file = open('./image/flag.bmp','rb')

bindata = file.read()
strdata = bindata.hex()

bfHeader = {}
bfHeader['bfType']      = strdata[paramBMP.para['TYPE_START_ADDR']:paramBMP.para['TYPE_END_ADDR']]
bfHeader['bfSize']      = strdata[paramBMP.para['SIZE_START_ADDR']:paramBMP.para['SIZE_END_ADDR']]
bfHeader['bfReserved1'] = strdata[paramBMP.para['RES1_START_ADDR']:paramBMP.para['RES1_END_ADDR']]
bfHeader['bfReserved2'] = strdata[paramBMP.para['RES2_START_ADDR']:paramBMP.para['RES2_END_ADDR']]
bfHeader['bfOffBits']   = strdata[paramBMP.para['OFFS_START_ADDR']:paramBMP.para['OFFS_END_ADDR']]

offset = bfHeader['bfOffBits'][6:8]+bfHeader['bfOffBits'][4:6]+bfHeader['bfOffBits'][2:4]+bfHeader['bfOffBits'][0:2] 
offsetDec = hex2dec(offset)
pixData = strdata[2*offsetDec:] 

bfType = strdata[:4]
bfSize = strdata[4:12]
bfReserved1 = strdata[12:16]
bfReserved2 = strdata[16:20]
bfOffBits = strdata[20:28]

# pixData = strdata[108:]

R = []
G = []
B = []
print(len(pixData))
for idx in range(0,int(len(pixData)/6)):
    b,pixData = pixData[:2], pixData[2:]
    g,pixData = pixData[:2], pixData[2:]
    r,pixData = pixData[:2], pixData[2:]
    R.append(hex2dec(r))
    G.append(hex2dec(g))
    B.append(hex2dec(b))

ppmFile = open('./a.ppm','w')    

ppmFile.write('P3\n')
ppmFile.write('124 124\n')
ppmFile.write('255\n')

# for idx in range(0, len(R)):
for idx in range(len(R)-1, -1, -1):
    ppmFile.write('{0} {1} {2}\n'.format(R[idx],G[idx],B[idx]))
    
# hex to ascii
l = chr(hex2dec(bfType[:2]))
m = chr(hex2dec(bfType[2:]))
print(l+m)


listData = list(strdata) 

a = np.array(listData)
b=a.reshape(-1,2)
print(b[0])
print(type(b[0]), type(b[0][0]))

file.close()
ppmFile.close()