lst=[6,5,2,7]
target=9
def twoSUm(lst,n):
    lst.sort()
    low=0
    high=len(lst)-1
    
    while(low<high):
        Sum=lst[low]+lst[high]
        if(Sum==target):
            return [low,high]
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
print(twoSUm(lst,target))
