// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// Example 2:

// Input: head = [1], n = 1
// Output: []

// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]

const firstExample = [1,2,3,4,5];
const firstExampleN = 2;

const secondExample = [1];
const secondExampleN = 1

const thirdExample = [1,2];
const thirdExampleN = 1

const removeNthFromEnd = (head, n) => {
    let left = 0;
    let right = 0;

    while(head[right] != null && head[right] <= head.length - 1) {
        console.log(left, right)
        left++
        right += n
    }

    console.log(left, right)
    console.log(head[left], head[right])
    console.log('head:', head)
    let temp = head[right]
    head[left + 1] = head[right]
    head.pop(temp)
    console.log('head:', head)

}

removeNthFromEnd(firstExample, firstExampleN)