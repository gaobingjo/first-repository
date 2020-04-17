iris$Species=NULL
colnames(iris)=NULL
data1=matrix(0,150,4)
options(digits = 3)
for (i in 1:4) {
  data1[,i]=iris[,i]
}
data2=matrix(0,150,4)
for (i in 1:4) {
  data2[,i]=data1[,i]-matrix(1,150,1)*mean(data1[,i])
}
K=matrix(0,150,150)
for (i in 1:150) {
  for (j in i:150) {
    K[i,j]=K[j,i]=(t(data2[i,])%*%data2[j,])**2
  }
}
X=matrix(0,150,10)
for (i in 1:150) {
  X[i,1]=data2[i,1]**2
  X[i,2]=data2[i,2]**2
  X[i,3]=data2[i,3]**2
  X[i,4]=data2[i,4]**2
  X[i,5]=data2[i,1]*data2[i,2]*sqrt(2)
  X[i,6]=data2[i,1]*data2[i,3]*sqrt(2)
  X[i,7]=data2[i,1]*data2[i,4]*sqrt(2)
  X[i,8]=data2[i,2]*data2[i,3]*sqrt(2)
  X[i,9]=data2[i,2]*data2[i,4]*sqrt(2)
  X[i,10]=data2[i,3]*data2[i,4]*sqrt(2)
}
K1=matrix(0,150,150)
for (i in 1:150) {
  for (j in i:150) {
    K1[i,j]=K1[j,i]=t(X[i,])%*%X[j,]
  }
}
print(K)
print(K1)
print(K-K1)
