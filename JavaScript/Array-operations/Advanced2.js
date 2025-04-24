let input = [1, 2, 3, 4, 5];

var n = 2;

for (let i = 0; i <= n; i++) {
    
    input.push(input[0]);

    input.shift(input[0]);
}

console.log(input);
