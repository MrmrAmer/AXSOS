let numbers = ["5", "10", "15", "20", "25"];

console.log(numbers.includes("25"));

let x = numbers.indexOf("25")

if (numbers.includes("25")) {
    console.log("Found at position" + " " + x);
    
} else {
    console.log("Not Found");
    
}
