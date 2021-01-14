# Given an array nums of n integers, are there elements a, b, c 
# in nums such that a + b + c = 0? Find all unique triplets in 
# the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.


#loop through the array and check every combination
#   Purpose: find all combinations of ints which sum to a number
#     Input: list[ints]
#     Input: int representing sum to compare against
#    Return: list[list[ints]]
def threeSum(nums, num):
        trios = [];
        #we're looking at every combination of 3, and we dont want to repeat combinations
        #so we start each inner for loop as one after the outter for loop
        #this way we don't go over the same combination of 3 numbers twice
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == num:
                        vals = [nums[i], nums[j], nums[k]]
                        vals.sort();
                        contains = False;
                        for trio in trios:
                            if trio == vals:
                                contains = True;
                        if(not contains):
                            trios.append(vals);
        return trios;


#example input
nums = [-1,0,1,2,-1,-4];
# nums = []
# nums = [0]
print(threeSum(nums, 0));