var longestCommonPrefix = function(strs) {
    
let output = ""

for (let j = 0; j < strs[0].length; j++) {
    let x = strs[0][j];
    for (let i = 1; i < strs.length; i++) {
        if (strs[i][j] !== x) {
            return output;
        } 
    }
    output += x;
}
return output;
};

console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["dog","racecar","car"]));
console.log(longestCommonPrefix(["dog","dad"]));
console.log(longestCommonPrefix(["dog","dad", "door"]));
console.log(longestCommonPrefix(["dog", "do", "doggy"]));


