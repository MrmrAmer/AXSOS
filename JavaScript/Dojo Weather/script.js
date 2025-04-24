function remove(params) {
    var cookie = document.querySelector(params);
    cookie.remove();
}

// function change() {
//     var unit = document.querySelector("#unit");
//     var tempSpans = document.querySelectorAll(".degrees span");

//     for (let i = 0; i < tempSpans.length; i++) {
//         let temp = tempSpans[i].textContent * 1;

//         if (unit.value == "C") {
//             tempSpans[i].textContent = Math.round((temp - 32) * (5 / 9));
//         } else {
//             tempSpans[i].textContent = Math.round(temp * (9 / 5) + 32);
//         }
//     }
// }

// function change() {
//     var unit = document.querySelector("#unit");
//     var tempSpans = document.querySelectorAll(".degrees span");

//     for (let i = 0; i < tempSpans.length; i++) {
//         let temp = parseInt(tempSpans[i].innerText);

//         if (unit.value === "C") {
//             tempSpans[i].innerText = Math.round((temp - 32) * (5 / 9));
//         } else {
//             tempSpans[i].innerText = Math.round(temp * (9 / 5) + 32);
//         }
//     }
// }


function celsiusToFahrenheit(temp) {
    return Math.round(temp * (9 / 5) + 32);
}

function fahrenheitToCelsius(temp) {
    return Math.round((temp - 32) * (5 / 9));
}


function change() {
    var unit = document.querySelector("#unit");
    var tempSpans = document.querySelectorAll(".degrees span");

    for (let i = 0; i < tempSpans.length; i++) {
        let temp = parseInt(tempSpans[i].innerText);

        if (unit.value === "C") {
            tempSpans[i].innerText = fahrenheitToCelsius(temp);
        } else {
            tempSpans[i].innerText = celsiusToFahrenheit(temp);
        }
    }
}


