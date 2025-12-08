# bruteforce logic to  find duplicates in a list (need to call count many times and complexity high)

# nums=[1,2,3,2,4,3]
# for i in set(nums):
#     if nums.count(i)>1:
#         print(i)
#

#optimal logic
nums = [1,2,3,2,4,3]
seen = set()
dupes = set()
for num in nums:
    if num in seen:
        dupes.add(num)
    else:
        seen.add(num)
print(list(dupes))