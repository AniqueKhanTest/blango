console.time("myTimer");
console.count("counter1");
console.log("A normal log message");
console.warn("Warning: something bad might happen");
console.error("Something bad did happen!");
console.count("counter1");
console.log("All the things above took this long to happen:");
console.timeEnd("myTimer");

function addNumber(a, b) {
  return a + b;
}

const result = addNumber(3, 4);
console.log(result);

/*
Arguments to JavaScript functions are implicitly all optional. 
For example, in Python we would implement optional arguments like this:

def say_hello(name=None):
    if name is None:
        print("Hello, no name")
    else:
        print("Hello, " + name)

say_hello()  # name is None
say_hello("Lily")  # name is "Lily"



In JavaScript, we need to check if a variable is === to undefined, which means it hasn’t been passed in. 
This JavaScript function is roughly identical to the Python one:

*/

// function sayHello(name) {
//   if (name === undefined) {
//     console.log("Hello , no name");
//   } else {
//     console.log("Hello , " + name);
//   }
// }

// sayHello(); // name is undefined
// sayHello("Lily"); // name is undefined

/*
Functions can also be assigned to variables. Another way of defining the sayHello() function is like this:
*/

// const sayHello = function (name) {
//   if (name === undefined) {
//     console.log("Hello , no name.");
//   } else {
//     console.log("Hello , " + name);
//   }
// };
// sayHello();

/*
The third way of defining functions is to use anonymous or arrow functions, 
so called because they’re denoted with the => (“arrow”) operator, 
and they’ll be anonymous or unnamed unless they’re assigned to a variable. 
Here’s the sayHello function again:
*/

const sayHello = (testName) => {
  if (testName === undefined) {
    console.log("Hello , no name!");
  } else {
    console.log("Hello , " + testName);
  }
};

sayHello("John");

/*
Using the arrow function also allows us to define lambda functions, that is, basic one-line functions 
that implicitly return a value. These are defined without the use of curly braces or the return keyword.
*/

/*For example, here’s an arrow function that doubles a number:*/
// const doubler = (x) => {
//   return x * 2;
// };

// And here’s the equivalent as a lambda:
const doubler = (x) => x * 2;
console.log(doubler(2));

function showAlert() {
  alert("Timeout finished");
}

// setTimeout(showAlert, 2000);

// For Loop
// for (let i = 0; i < 2; i += 1) {
//   console.log(i);
// }

// While loop
// let i = 0;

// while (i < 2) {
//   console.log(i);
//   i += 1;
// }

// Do while loop
let i = 0;

do {
  console.log(i);
  i += 1;
} while (i < 2);

const numbers = [1, 2, 3];
// For each
numbers.forEach((value) => {
  console.log(value);
});

// Map
const doubled = numbers.map((value) => value * 2);
console.log(doubled);
