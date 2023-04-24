// let number = 0

// if (number == 0){
//     alert("Равно 0!")
// }
// else{
//     alert("Не равно 0")
// }

// let number = prompt("Введите число:")
// if (number == 0){
//     alert("Число рано нулю")
// }
// else if (number > 0) {
//     alert ("Число больше нуля")
// }
// else {
//     alert("Число меньше нуля")
// }

// let x = prompt("Введите координаты X")
// let y = prompt("Введите координаты Y")
// if (x > 0 && y > 0){
//     alert("Точка находится в 1-ом квадранте")
// }
// else if (x < 0 && y > 0){
//     alert("Точка находится в 2-ом квадранте")
// }
// else if (x < 0 && y < 0){
//     alert("Точка находится в 3-ем квадранте")
// }
// else if (x == 0){
//     alert("Точка находится на оси Y")
// }
// else if (y == 0){
//     alert("Точка находится на оси X")
// }
// else if (y == 0 && x == 0){
//     alert("Точка находится пересечении осей X и Y")
// }
// else {
//     alert("Точка находится в 4-ом квадранте")}

// Циклы

// WHILE

// let i = 0;
// while ( i < 10 ){
//     document.write(i+"<br>")
//     // document.write(`<h1>${i}<br></h1>`)
//     i = i + 1;
//     // ++i
// }


// FOR

// for (let i = 0; i < 10; i++){
//     document.write(`<h1>${i}<br></h1>`)
// }


// let C = prompt("Введите число:")
// for (let i = 1; i < 10; i++){
//     N = C * i
//     document.write(`<h1> ${C} * ${i} = ${N} <br></h1>`)
// }

// let a = prompt("Введите число:")
// var s = 0
// for (let i = 0; i <= a; i++) {
//     s += i
// }
// document.write(`<h1>${s}<br></h1>`)

// for (let C = 1; C < 10; C++) {
//     for (let i = 1; i < 11; i++) {
//         N = C * i
//         document.write(`<h1> ${C} * ${i} = ${N} <br></h1>`)
//     }
//     document.write(`<br>`)
// }

let a = 1
var b = '!'
while (a != b){
    a = prompt("Введите число")
    document.write(`<h1>${a}<br></h1>`)
}