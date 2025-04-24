let numbers = ["1", "5", "10", "15", "20", "25", "30"];

var newarray = []

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > 15) {
        newarray.push(numbers[i])
    }
}

console.log(newarray);