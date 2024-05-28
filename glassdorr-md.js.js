/*This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a 
given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights
[100, 200, 150, 80] and a boat limit of 200,
the smallest number of boats required will be three
*/
function findNoBoat(population,weight) {
  let noBoat = 0
  for (let i = 0; i < population.length; ++i) {
    let person = population[i]

    for (let j = 0; j < population.length; ++j) {
     if (j === i) continue

     let nextPerson = population[j]

     if (nextPerson + person < weight || person == weight) {
      noBoat += 1
      break
     }

    }
  }

   return noBoat
}

let result = findNoBoat([100, 200, 150, 80],200)
console.log(result)
