n = 7

for y in range(-n,n+1):
    for x in range(-n,n+1):
        if x+y<=n and x+y>=-1*n and x-y<=n and x-y>=-1*n and (x+y)%2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

'''
Output:

       *       
      * *      
     * * *     
    * * * *    
   * * * * *   
  * * * * * *  
 * * * * * * * 
* * * * * * * *
 * * * * * * * 
  * * * * * *  
   * * * * *   
    * * * *    
     * * *     
      * *      
       *

'''
