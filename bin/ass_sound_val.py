import pickle as pk

def value():
    f=open('ass_sound_val.dat','rb+')
    r=pk.load(f)
    return r
    f.close()

#print(value())