
nums = [2,7,11,15]
target = 9
for x in range(0,len(nums)):
            for y in range(x,len(nums)):
                if(x==y):
                    continue
                if((nums[x]+nums[y])==target):
                    solution = [x,y]
                    print(solution)