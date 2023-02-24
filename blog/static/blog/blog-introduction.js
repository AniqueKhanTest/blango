const framework = "Django"
const language = "Python"

// alert(framework+" is written in "+language)


/* Notice that we’re using triple-equals (===) to compare the variables in the condition.
 Using === means that the types of the items being compared are taken into comparison. F
 or example, in JavaScript we could compare the string '1' and number 1 with ==. 
 This would evaluate to true, as JavaScript coerces them to the same type and then compares. 
 With === type coercion doesn’t take place, so '1' === 1 is false.
*/
const testName = "Ben"
let benCount = 0
if (testName === "Ben"){
    benCount=1
}
// alert("There is "+benCount+" Ben")

const fruit = ["Apple",'Banana']
fruit.push('Cherry')
// alert(fruit)
const fruitCount = {Apple:0,"Banana":1}
fruitCount.Cherry = 2  // add new item to object
fruitCount['Cherry'] = 2 // is equivalent
// alert(fruitCount)



// const theNumber = 1
// let testingName = 'Ben'

// if (theNumber === 1) {
//   let testingName = 'Leo'
//   alert(testingName)
// }

// alert(testingName)

// const theNumber = 1
// let testingName = 'Ben'

// if (theNumber === 1) {
//     testingName = 'Leo'
//   alert(testingName)
// }

// alert(testingName)

// const theNumber = 1

// if (theNumber === 1) {
// let testingName = 'Leo'
//   alert(testingName)
// }

// alert(testingName)


// // Try it out 
const theNumber = 1
let yourName = 'Ben'

if (theNumber === 1) {
  let yourName = 'Leo'
  alert(yourName)
}

alert(yourName)

// let pets = {
//     cats : 1,
//     dogs : 3,
//     fish : 8,
//     birds : 0 
//   }

// alert(pets['dogs'])