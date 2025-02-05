// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

 

// Example 1:

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

// Example 2:

// Input: nums = [2,0,1]
// Output: [0,1,2]



const testOne = [2,0,2,1,1,0]; //[0,0,1,1,2,2]
const testTwo = [2,0,1]; // [0,1,2]
const testThree = [1, 0, 2]
const sortColors = (nums) => {
    let start = 0;
    let end = nums.length - 1;
    let current = 0;
    while (current <= end) {
        console.log(nums[current], nums)
        if (nums[current] === 2) {
            let temp = nums[end];
            nums[end] = nums[current];
            nums[current] = temp;
            end--
        } else if (nums[current] === 1) {
            current++
        } else {
            let temp = nums[current];
            nums[current] = nums[start];
            nums[start] = temp;
            start++
            current++
        }  
    }

    return nums
   

}

sortColors(testOne)
sortColors(testTwo)
sortColors(testThree)

