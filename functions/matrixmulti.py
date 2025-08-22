a = [ [1,2,3,4] , [5,6,7,8] , [9,10,11,12] ]  
b = [ [10,20] , [30,40] , [50,60] , [70,80] ]
 
aROWS,aCOLS = 3,4
bROWS,bCOLS = 4,2
cROWS,cCOLS = 3,2
 
c = [[0,0],[0,0],[0,0]]
for i in range(aROWS):
   for j in range(aCOLS):
       for k in range(bCOLS):
           c[i][k] += a[i][j] * b[j][k]

print("Matrix Product:\n",c)
