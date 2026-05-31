'''
* * * * *
 * * * *
  * * *
   * *
    *
    '''
num = int ( input ("Enter your amount : "))
for i in range(num,0,-1):
    print(" "*(num-i)+"* "*i)