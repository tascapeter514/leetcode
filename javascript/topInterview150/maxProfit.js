// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

// Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

let prices = [7,1,5,3,6,4]; // 5
let morePrices = [7,6,4,3,1] // 0
const test154 = [2,4,1] // 2
const test = [7,2,5,3,6,1] // 4




const maxProfit = (prices) => {
    let left = 0;
    let right = 1;
    let maxProfit = 0;
    while (right < prices.length) {
        if (prices[left] < prices[right]) {
            let profit = prices[right] - prices[left];
            maxProfit = Math.max(maxProfit, profit)
        } else {
            left = right
        }
        right++
        
    }
    return maxProfit

}


// console.log(maxProfit(prices))
// console.log(maxProfit(morePrices))
// maxProfit(prices)
maxProfit(test)




