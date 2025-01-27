// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

const input = [1,2,3,4,5,6,7]; // [5,6,7,1,2,3,4]
const step = 3;
const inputTwo = [-1,-100,3,99]; // [3,99,-1,-100]
const stepTwo = 2;


const rotate = (nums, k) => {
    let count = 0;
    while (count < k) {
        for (let i = 0; i < nums.length; i++) {
            let temp = nums[i]
            nums[i] = nums[nums.length - 1]
            nums[nums.length - 1] = temp
        }
        count++
    }
    

    return nums
}

// rotate(input, step)
rotate(inputTwo, stepTwo)


