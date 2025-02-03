// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].

// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]


const exampleOne = [-4,-1,0,3,10]; // [0,1,9,16,100]
const exampleTwo = [-7,-3,2,3,11]; // [4,9,9,49,121]
const exampleThree = [-5,-3,-2,-1] // [1, 4, 9 , 25]
const exampleFour = [2, 2] // [4, 4]

const sortedSquares = (nums) => {
    let start = 0;
    let end = nums.length - 1;
    while (start <= end) {
        if (start === end) {
            nums[start] = Math.pow(nums[start], 2)
            break
        } else {
            nums[start] = Math.pow(nums[start], 2);
            nums[end] = Math.pow(nums[end], 2)
            start++
            end--
        }  
    }


    // return nums.sort((a, b) => a - b)
    console.log(nums.sort((a, b) => a - b))

}
// sortedSquares(exampleThree)
// sortedSquares(exampleOne)
sortedSquares(exampleFour)
