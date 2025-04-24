function accept(params) {
    var hide = document.querySelector(params);
    hide.remove();
    var requestsDeacrease = document.querySelector(".badge");
    requestsDeacrease.innerText--;
    var requestsIncrease = document.querySelector("#increas");
    requestsIncrease.innerText++;
}

function decline(params) {
    var hide = document.querySelector(params);
    hide.remove();
    var requestsDeacrease = document.querySelector(".badge");
    requestsDeacrease.innerText--;
}

function change() {
    var changeName = document.querySelector("#changeName");
    changeName.innerText = "Marwan Amer";
}