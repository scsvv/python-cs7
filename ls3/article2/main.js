x = "a";
y = 10

try {
    x = parseInt(x);
}
catch {
    x = 0
}
console.log(x + y)