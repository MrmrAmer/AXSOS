// let input = [1, 2, 2, 3, 4, 4, 5]
 
// for (let i = 0; i < input.length; i++) {
    // for (let j = i + 1; j < input.length; j++) {
        // if (input[j] == input[i]) {
        // input.splice(input[j], 1);
        // }
    // }
// }
// console.log(input);

let input = [1, 2, 2, 3, 4, 4, 5, 4, 1, 2, 2, 6, 3, 5, 5];
 
for (let i = input.length - 1; i >= 0; i--) {
    for (let j = 0; j < i; j++) {
        if (input[j] == input[i]) {
        input.splice(i, 1);
        }
    }
}
console.log(input);