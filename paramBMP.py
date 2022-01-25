# ========================================
# parameter
# ========================================
para = {}

# bfType : 2 Byte
para['TYPE_BYTE_SIZE']  = 2
para['TYPE_START_ADDR'] = 0
para['TYPE_END_ADDR']   = para['TYPE_START_ADDR'] + 2*para['TYPE_BYTE_SIZE']

# bfSize : 4 Byte
para['SIZE_BYTE_SIZE']  = 4
para['SIZE_START_ADDR'] = para['TYPE_END_ADDR']
para['SIZE_END_ADDR']   = para['SIZE_START_ADDR'] + 2*para['SIZE_BYTE_SIZE']

# bfReserved1 : 2 Byte
para['RES1_BYTE_SIZE']  = 2
para['RES1_START_ADDR'] = para['SIZE_END_ADDR']
para['RES1_END_ADDR']   = para['RES1_START_ADDR'] + 2*para['RES1_BYTE_SIZE']

# bfReserved2 : 2 Byte
para['RES2_BYTE_SIZE']  = 2
para['RES2_START_ADDR'] = para['RES1_END_ADDR']
para['RES2_END_ADDR']   = para['RES2_START_ADDR'] + 2*para['RES2_BYTE_SIZE']

# bfOffBits : 4 Byte
para['OFFS_BYTE_SIZE']  = 4
para['OFFS_START_ADDR'] = para['RES2_END_ADDR']
para['OFFS_END_ADDR']   = para['OFFS_START_ADDR'] + 2*para['OFFS_BYTE_SIZE']