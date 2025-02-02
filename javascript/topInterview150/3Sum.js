// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: 
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

// Example 2:

// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.

// Example 3:

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.


const exampleOne = [-1,0,1,2,-1,-4];
const exampleTwo = [0,1,1];
const exampleThree = [0,0,0]

const threeSum = (nums) => {
    const results = [];
    nums = nums.sort((a, b) => a - b)
    for (let pivot = 0; pivot < nums.length - 2; pivot++) {
        if (nums[pivot] > 0) {
            break
        }

        if (pivot > 0 && nums[pivot] == nums[pivot - 1]) {
            continue;
        }

        let low = pivot + 1;
        let high = nums.length - 1;
        while (low < high) {
            let total = nums[pivot] + nums[low] + nums[high];
            if (total < 0) {
                low++
            } else if (total > 0) {
                high--
            } else {
                results.push([nums[pivot], nums[low], nums[high]])
                low++
                high--

                while (low < high && nums[low] == nums[low - 1]) {
                    low++
                }

                while (low < high && nums[high] == nums[high + 1]) {
                    high--;
                }
            }
        }

    }
    return results
  
    
    
}

threeSum(exampleOne)