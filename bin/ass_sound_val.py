import pickle as pk
import os

from bin.get_dirs import FILE_SOUND_VALUE

if not os.path.exists(FILE_SOUND_VALUE):
    f = open(FILE_SOUND_VALUE,'wb+')

def value():
    f=open(FILE_SOUND_VALUE,'rb+')
    r=pk.load(f)
    return r
    f.close()

#print(value())
