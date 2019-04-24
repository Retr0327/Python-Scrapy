a=[int(x) for x in input().split()]

List=[]
nums_len=len(a)

for i in range(nums_len):
        for j in range(i+1, nums_len):
                y=a[i]*a[j]
                List.append(y)
                List.reverse()
                print(List)
