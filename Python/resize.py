import sys
archivo=open(sys.argv[1],"r");
time=[]
voltage=[]        

i=0
parameter=sys.argv[1].split(".")
file_write=open(parameter[0]+"_resized.txt","w")
for line in archivo:
        
    file_write.write(line) 
    i+=1
    if(i>10000):
        break
file_write.close()
archivo.close()