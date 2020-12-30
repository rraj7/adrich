array = [0,4,2,5,1,3] 
target = [1,0,5,3,2,4] 
#Instead of this linear search we can also use hashmap but using this 
#there were a lot of errors in that approach
def LinearSearch(array, x): 
    for i in range(1,len(array)):
        if array[i] ==x:
            return i

#array = [4,0,2,5,1,3] 
#target = [1,0,5,3,2,4] 0,5,1


def Car(array,target):
    for i in range(0,len(array)-1):
        
            if (array[i] == target[i]):
                print("No need to move for this position")
                print(array)   
            
            elif array[i]==0:

                movingcar = target[i]
                #print(movingcar)

                #SEARCH THE POSITION TO BE SWAPPED 

                carposition = LinearSearch(array,movingcar)
                # SWAP 
                #print(array[carposition]
                array[i],array[carposition] = array[carposition],array[i]
                print(array)

            elif (array[i]!= target[i]):
                print(i)
                #search position of array[i] in target and swap using 0 
                movingcar = array[i]
                #print(movingcar)
                carposition = LinearSearch(target,movingcar)
                #Swap using 0 
                findzero = LinearSearch(array,0)
                
                array[findzero],array[carposition] = array[carposition],array[findzero]
                array[i], array[carposition] = array[carposition],array[i]
            
                print(array)



a = Car(array,target)
print(a)


