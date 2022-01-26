# ========================================
# parameter
# ========================================
para = {}

# BitMapFileHeader
# bfType : 2 Byte
para['BFTYPE_BYTE_SIZE']  = 2
para['BFTYPE_START_ADDR'] = 0
para['BFTYPE_END_ADDR']   = para['BFTYPE_START_ADDR'] + 2*para['BFTYPE_BYTE_SIZE']

# bfSize : 4 Byte
para['BFSIZE_BYTE_SIZE']  = 4
para['BFSIZE_START_ADDR'] = para['BFTYPE_END_ADDR']
para['BFSIZE_END_ADDR']   = para['BFSIZE_START_ADDR'] + 2*para['BFSIZE_BYTE_SIZE']

# bfReserved1 : 2 Byte
para['BFRES1_BYTE_SIZE']  = 2
para['BFRES1_START_ADDR'] = para['BFSIZE_END_ADDR']
para['BFRES1_END_ADDR']   = para['BFRES1_START_ADDR'] + 2*para['BFRES1_BYTE_SIZE']

# bfReserved2 : 2 Byte
para['BFRES2_BYTE_SIZE']  = 2
para['BFRES2_START_ADDR'] = para['BFRES1_END_ADDR']
para['BFRES2_END_ADDR']   = para['BFRES2_START_ADDR'] + 2*para['BFRES2_BYTE_SIZE']

# bfOffBits : 4 Byte
para['BFOFFS_BYTE_SIZE']  = 4
para['BFOFFS_START_ADDR'] = para['BFRES2_END_ADDR']
para['BFOFFS_END_ADDR']   = para['BFOFFS_START_ADDR'] + 2*para['BFOFFS_BYTE_SIZE']

# BitMapInfoHeader
# biSize : 4 Byte
para['BISIZE_BYTE_SIZE']  = 4
para['BISIZE_START_ADDR'] = para['BFOFFS_END_ADDR']
para['BISIZE_END_ADDR']   = para['BISIZE_START_ADDR'] + 2*para['BISIZE_BYTE_SIZE']

# biWidth : 4 Byte
para['BIHRES_BYTE_SIZE']  = 4
para['BIHRES_START_ADDR'] = para['BISIZE_END_ADDR']
para['BIHRES_END_ADDR']   = para['BIHRES_START_ADDR'] + 2*para['BIHRES_BYTE_SIZE']

# biHeight : 4 Byte
para['BIVRES_BYTE_SIZE']  = 4
para['BIVRES_START_ADDR'] = para['BIHRES_END_ADDR']
para['BIVRES_END_ADDR']   = para['BIVRES_START_ADDR'] + 2*para['BIVRES_BYTE_SIZE']
