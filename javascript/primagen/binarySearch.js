

const test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


const binarySearch = (arr, val) => {
    console.log(arr, val)
    let low = 0;
    let high = arr.length;
    

    while (low < high) {
        let middle = Math.floor(low + (high - low) / 2);
        console.log(middle, arr[middle], low, high)
        if (arr[middle] === val) {
            return true
        } else if (val > arr[middle]) {
            low = middle + 1
        } else {
            high = middle
        } 
    }

    return false

}

console.log(binarySearch(test, 10))

