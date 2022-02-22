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

# biPlanes : 2 Byte
para['BIPLAN_BYTE_SIZE']  = 2
para['BIPLAN_START_ADDR'] = para['BIVRES_END_ADDR']
para['BIPLAN_END_ADDR']   = para['BIPLAN_START_ADDR'] + 2*para['BIPLAN_BYTE_SIZE']

# biBitCount : 2 Byte
para['BIBITC_BYTE_SIZE']  = 2
para['BIBITC_START_ADDR'] = para['BIPLAN_END_ADDR']
para['BIBITC_END_ADDR']   = para['BIBITC_START_ADDR'] + 2*para['BIBITC_BYTE_SIZE']

# biCompression : 4 Byte
para['BICOMP_BYTE_SIZE']  = 4
para['BICOMP_START_ADDR'] = para['BIBITC_END_ADDR']
para['BICOMP_END_ADDR']   = para['BICOMP_START_ADDR'] + 2*para['BICOMP_BYTE_SIZE']

# biSizeImage : 4 Byte
para['BISIMG_BYTE_SIZE']  = 4
para['BISIMG_START_ADDR'] = para['BICOMP_END_ADDR']
para['BISIMG_END_ADDR']   = para['BISIMG_START_ADDR'] + 2*para['BISIMG_BYTE_SIZE']

# biXPelsPerMeter : 4 Byte
para['BIXPEL_BYTE_SIZE']  = 4
para['BIXPEL_START_ADDR'] = para['BISIMG_END_ADDR']
para['BIXPEL_END_ADDR']   = para['BIXPEL_START_ADDR'] + 2*para['BIXPEL_BYTE_SIZE']

# biYPelsPerMeter : 4 Byte
para['BIYPEL_BYTE_SIZE']  = 4
para['BIYPEL_START_ADDR'] = para['BIXPEL_END_ADDR']
para['BIYPEL_END_ADDR']   = para['BIYPEL_START_ADDR'] + 2*para['BIYPEL_BYTE_SIZE']

# biClrUsed : 4 Byte
para['BICLRU_BYTE_SIZE']  = 4
para['BICLRU_START_ADDR'] = para['BIYPEL_END_ADDR']
para['BICLRU_END_ADDR']   = para['BICLRU_START_ADDR'] + 2*para['BICLRU_BYTE_SIZE']

# biClrImportant : 4 Byte
para['BICLRI_BYTE_SIZE']  = 4
para['BICLRI_START_ADDR'] = para['BICLRU_END_ADDR']
para['BICLRI_END_ADDR']   = para['BICLRI_START_ADDR'] + 2*para['BICLRI_BYTE_SIZE']