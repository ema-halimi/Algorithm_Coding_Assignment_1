#In the language of your choice, implement two algorithms for computing the last five digits of the nth Fibonacci number that are based on (a)
#the recursive definition-based algorithm F(n); (b) the iterative definitionbased algorithm Fib(n). Perform an experiment to find the largest value
#of n for which your programs run under 1 minute on your computer.

#a)
def fiblast5(n):
  f=[0,1];
  for i in range(2,n+1):
    f.append((f[i-1]+f[i-2])%100000);
  return f[n];
print(fiblast5(61));

#b)
def fiblast5_rec(n):
  if(n==0 or n==1):
    return n;
  else:
    return (fiblast5_rec(n-1)+fiblast5_rec(n-2))%100000;
print(fiblast5_rec(23));

