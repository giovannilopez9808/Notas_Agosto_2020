import math
import timeit
def primeFactors(n):
   while n % 2 == 0:
      print (2),
      n = n / 2
   for i in range(3,int(math.sqrt(n))+1,2):
      while n % i== 0:
         print (i)
         n = n / i
   if n > 2:
      print (n)
n = 21
file=open("time_clasic.txt","w")
for count in range(1000):
    t_i=timeit.default_timer()
    primeFactors(n)
    t_f=timeit.default_timer()
    file.write(str(t_f-t_i)+"\n")
file.close()
