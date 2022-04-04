nums = (2, 7, 11, 15, 1, 8, 7)
nums1 = list(set(nums))  #去除元组nums中重复的元素存入列表nums1
a = []
l = len(nums1)
i = 0
for i in range(0, l-i):
    for j in range(i+1, l):
        if nums1[i] + nums1[j] == 9:
            a.append((nums1[i],nums1[j]))
print('和为9的是：')
for k in a:
    print(k)