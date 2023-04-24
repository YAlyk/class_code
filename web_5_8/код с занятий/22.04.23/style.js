// switch (expression){
//     case n1:
//         statments
//         break;
//     case n2:
//         statments
//         break;
//     case n3:
//         statments
//         break;
//     default:
//         statments
// }


// do {
//     code block
// }
// while (condition);

// var sum = 0;
// for (i = 4; i < 8; i++) {
//     if (i == 6) {
//         continue;
//     }
//     sum += i;
// }
// document.write(sum);

// var x = 0;
// while (x < 6) {
//     x++;
// }
// document.write(x)

// var day_of_weekl = 4;
// switch (day_of_weekl) {
//     case 1:
//     case 2:
//     case 3:
//     case 4:
//     case 5:
//         document.write('Workin days');
//         break;
//     case 6:
//         document.write('Saturday');
//     default:
//         document.write('Today is Sunday');
//         break;
// }

// function name(){
//     //code
// }

// function myFunction() {
//     alert('вы вызвали функцию')
// }

// myFunction()

// function myFunction(name) {
//     alert('hi' + name)
// }

// myFunction('тест')
// myFunction('тест2')

// function myFunction(a, b) {
//     return a * b;
// }

// alert(myFunction(5, 8), ' результат умножения 5 и 8')


// var user = prompt('введите имя');
// alert(user);

// var results = confirm('вы действительно хотите закрыть страницу?')
// if (results == true) {
//     alert('вы закрыли страницу');
// }
// else {
//     alert('вы не закрыли страницу');
// }

// function test(number) {
//     while (number < 5) {
//         number++;
//     }
//     return number;
// }

// alert(test(2))

// function multNumber(a, b) {
//     var c = a * b;

// }

// alert(multNumber(2, 6))



function max(a, b) {
    if (a >= b)
        return a;
    else
        return b;
}