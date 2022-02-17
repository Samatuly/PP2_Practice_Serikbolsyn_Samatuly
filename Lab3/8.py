arr = str(input())
arr = arr.split()
def has_33(nums):
    for i in range(len(nums)-1):
        nums[i] = int(nums[i])
        if(nums[i - 2] == 0) and (nums[i - 1] == 0) and (nums[i] == 7):
            print("True")
            exit()
    print("False")
has_33(arr) 