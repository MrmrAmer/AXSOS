var allpizzas = [];

function pizzaOven(crust, sauce, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    allpizzas.push(pizza)
    return pizza;
}

var p1 = pizzaOven("deep dish", "traditional", ["mozarrella"], ["pepperoni", "sausage"]);
console.log(p1);
var p2 = pizzaOven("hand tossed", "marinara", ["mozarrella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(p2);
var p3 = pizzaOven("hand tossed", "traditional", ["mozarrella", "feta"], ["sausage", "olives", "onions"]);
console.log(p3);
var p4 = pizzaOven("deep dish", "marinara", ["mozarrella", "feta"], ["pepperoni", "olives"]);
console.log(p4);

function randomPizza() {
    return allpizzas[Math.floor(Math.random() * allpizzas.length)];
}

let randomPizza1 = randomPizza();
let randomPizza2 = randomPizza();

console.log(randomPizza1);
console.log(randomPizza2);

