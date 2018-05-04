
#write and read a txt file
"""
poem = '''\
Programe is fun
 when u have done
 if u wanna have fun
 fck off!
 '''

f = open('poem.txt','w')
f.write(poem)
f.close

f = open('poem.txt','r')
while True:
    line = f.readline()
    if(len(line) == 0):
        break
    print(line)
f.close()
"""

#cPickle  and pickle

import pickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')

p.dump(shoplist,f)

f.close()

del(shoplist)

f = open(shoplistfile,'rb')
storedlist=p.load(f)

print(storedlist)
