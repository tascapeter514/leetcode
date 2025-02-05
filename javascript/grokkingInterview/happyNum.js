// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

//     Starting with any positive integer, replace the number by the sum of the squares of its digits.
//     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
//     Those numbers for which this process ends in 1 are happy.

// Return true if n is a happy number, and false if not.

 

// Example 1:

// Input: n = 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1

// Example 2:

// Input: n = 2
// Output: false


let num = 19
let seven = 7
let testTwo = 1111111


const isHappy = (n) => {
    const sum = (num) => num.toString().split('').map((numStr) => Number(numStr) ** 2).reduce((acc, curr) => acc + curr);
    const visited = []
    let currentSum = sum(n)
    while (currentSum != 1) {
        console.log(currentSum)
        if (visited.includes(currentSum)) {
            return false

        }  else {
            visited.push(currentSum)
            currentSum = sum(currentSum)
        }
    }

    return true
    
}
console.log(isHappy(1111111))


// LEETCODE SOLUTION TWO POINTERS
// var isHappy = function(n) {
//     const sqr = (n) => {
//         let ans = 0;
//         while (n > 0) {
//             let rem = n % 10;
//             ans += rem * rem;
//             n = Math.floor(n / 10);
//         }
//         return ans;
//     };

//     let slow = n;
//     let fast = n;

//     do {
//         slow = sqr(slow);
//         fast = sqr(sqr(fast));
//     } while (slow !== fast);

//     return slow === 1;
// };