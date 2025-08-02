def twoSum(nums,target):
    d={}
    for a in range(0,len(nums)-1):
        b=target-nums[a]
        if(b in d):
            return [a,d[b]]
        else:
            d[nums[a]]=a
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))
