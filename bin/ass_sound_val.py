
def value():
    f=open('ass_sound_val.txt','r+')
    r=f.read()
    #r=bool(r)
    return r
    f.close()
    

print(value())