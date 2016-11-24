x=1
f1 = open("plik17_11.txt","wb")
for x in xrange(10):
    for j in xrange(10):
        if(x!=0 and j !=0):
            f1.write(str(x*j,))
    
    f1.write("\n")