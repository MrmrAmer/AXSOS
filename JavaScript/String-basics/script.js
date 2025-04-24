function removeBlanks(str) {
    let output = "";
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            output += str[i];
        }
    }
    return output;
}

console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
console.log(removeBlanks("I can not BELIEVE it's not BUTTER"));

function getDigits(str) {
    let output = "";
    for (let i = 0; i < str.length; i++) {
        if (isNaN(str[i]) == false) {
            output += str[i];
        }
    }
    return output;
}

console.log(getDigits("a1c34kh446d!@#jhas888"));
console.log(getDigits("ani3hD93070BS@$@009gb"));

function acronym(str) {
    let v = str.split(" ");
    let output = "";
    for (let i = 0; i < v.length; i++) {
        if (v[i] !== "") {
            output += v[i][0].toUpperCase();
        }
    }

    return output;
}

console.log(acronym(" there's no free lunch - gotta pay yer way. "));
console.log(acronym("Live from New York, it's Saturday Night!"));

function countNonSpaces(str) {
    let output = "";
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            output += str[i];
        }
    }
    return output.length;
}

console.log(countNonSpaces("Honey pie, you are driving me crazy"));
console.log(countNonSpaces(" Hello World ! "));

function removeShorterStrings(arr, minLength) {
    let x = minLength;
    let output = []
    for (let i = 0; i < arr.length; i++) {
            if (arr[i].length >= x) {
                output.push(arr[i]);
            }
    }
    return output;
}

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));
console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));