arr = []
for i in range(3):
    a = int(input())
    arr.append(a)
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i] == nums[i+1]:
                print("True")
                exit()
            else:
                print("False")
has_33(arr)   