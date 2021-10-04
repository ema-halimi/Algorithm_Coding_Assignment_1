#There are 2n glasses standing next to each other in a row, the first n of them filled with soda drink and the remaining n glasses empty. 
#Make the glasses alternate in a filled-empty-filled-emty pattern in the minimum number of glass moves.

NumberOfGlasses = int(input ("Enter number of glasses:"))
x=int(NumberOfGlasses/2)
moves=0
#F for full glasses and E for empty glasses
lst = list(x*'F'+x*'E')
print (lst)

def AlternateofGlasses(x, List, moves):
    for a in range (0,x):
      if a%2!=0:
        lst[a],lst[-a-1]=lst[-a-1],lst[a]
        moves+=1
    print ("Number of moves =",moves)

AlternateofGlasses (x,lst,moves)
print (lst)
     












  


