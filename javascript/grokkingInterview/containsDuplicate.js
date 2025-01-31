// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input: nums= [1, 2, 3, 4]
// Output: false  
// Explanation: There are no duplicates in the given array.

// Example 2:

// Input: nums= [1, 2, 3, 1]
// Output: true  
// Explanation: '1' is repeating.

let firstExample = [1, 2, 3, 4];
let secExample = [1, 2, 3, 1];
let thirdExample = [1, 2, 4, 10, 2, 1]

function containsDupe(nums) {
    const hash = {}
    for (let i = 0; i <= nums.length - 1; i++) {
        console.log('current num:', nums[i])
        if (hash[nums[i]]) {
            return true
        } else {
            hash[nums[i]] = 1

        }
        
    }
    console.log(hash)

    return false

    
}

// containsDupe(firstExample)
// console.log(containsDupe(firstExample))
console.log(containsDupe(thirdExample))

