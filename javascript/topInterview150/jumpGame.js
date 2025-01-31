// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

 

// Example 1:

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// Example 2:

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

const test = [2,3,1,1,4];
const testTwo = [3,2,1,0,4];
const edge = [2,0]

const canJump = function(nums) {
    console.log(nums[nums.length - 1], nums[0])
    for (let i = 0; i <= nums.length - 1; i += nums[i] - 1) {
        console.log('nums[i]:', nums[i], i)
       
        if (nums[i] == nums[nums.length - 1]) {
            return true
        } else if (nums[i] === 0 && nums[nums.length - 1] != 0) {
            console.log('inner nums:', nums[i])
            return false
        }
    }
    return
    // return nums[i] === nums[nums.length - 1] ? true : false
    
    
};
 // console.log(i, nums[i])
// console.log(canJump(test))
// console.log(canJump(testTwo))
console.log(canJump(edge))


