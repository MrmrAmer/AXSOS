let input = [3,2,4]

let target = n = 6

let output = []

for (let i = 0; i < input.length; i++) {
    for (let j = i +1; j < input.length; j++) {
        if (input[i] + input[j] == n) {
            output.push(i);
            output.push(j);
        }
    }
    
}

console.log(output);


var twoSum = function(nums, target) {
    let output = []
    for (let i = 0; i < nums.length; i++) {
        for (let j = i +1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                output.push(i);
                output.push(j);
            }
        }
    }
    return output;
};

console.log(twoSum([3,2,4], 6));
console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([3,3], 6));
