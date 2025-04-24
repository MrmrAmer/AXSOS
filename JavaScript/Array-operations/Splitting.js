let items = ["a", "b", "c", "d", "e"];

var array1 = []
var array2 = []

for (let i = 0; i <= 2; i++) {
    array1.push(items[i]);
}
console.log(array1);

for (let i = 3; i < items.length; i++) {
    array2.push(items[i]);
}
console.log(array2);

