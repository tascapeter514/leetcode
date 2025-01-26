// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3

// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2


const numsOne = [3,2,3]
const numsTwo = [2,2,1,1,1,2,2]
const numsThree = [-1,1,1,1,2,1]


// MY SOLUTION
const majorityElement = (arr) => {
    const hash = {}
    arr.forEach(el => hash[el] ? hash[el] += 1 : hash[el] = 1);
    return parseInt(arr.reduce((acc, curr) => hash[curr] > hash[acc] ? acc = curr : acc))
}

majorityElement(numsOne)
majorityElement(numsTwo)
majorityElement(numsThree)

// LEETCODE SOLUTION

// var majorityElement = function(nums) {
//     const hash = {};
//     let res = 0;
//     let majority = 0;

//     for (let n of nums) {
//         hash[n] = 1 + (hash[n] || 0);
//         if (hash[n] > majority) {
//             res = n;
//             majority = hash[n];
//         }
//     }

//     return res;    
// };