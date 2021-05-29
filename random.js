var Chance= require('chance')
const chance = new Chance()
const snakes = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26], [49, 11], [56, 53], [62, 19], [64, 60], [87, 24], [93, 73], [95, 75], [98, 78]]
const uu=[[4,13],[14,7],[6,3]]
let countlist=[]
function harmonic(number) {
    let h = 1
    for (let i = 2; i <= number; i++) {
        h+=1/i
    }
    return h
}
function nharmonic(nth, dice) {
    let dist = []
    let cont=[]
    for (let i = 1; i <= dice; i++) {
        cont.push(i)
        dist.push((1)/(i*nth)) 
    }
    return [cont, dist]
}
function simulation(dice) {
    let count = 0
    let path = []
    let token = 0
    let distribution=nharmonic(harmonic(dice),dice)
    while (token < 100) {
        let roll = chance.weighted(distribution[0],distribution[1]);
        token =token + roll
        count++;
        if (token > 100) {
            token=token - roll
        }
        for (const snake of snakes) {
            if (snake[0] == token) {
                token = snake[1]
                count++;
            }
        }
        path.push(token)
    }
    return [path,count]
}
function simulation1(dice) {
  let count = 0;
  let path = [];
  let token = 0;
  let distribution = nharmonic(harmonic(dice), dice);
  while (token < 16) {
    let roll = chance.weighted(distribution[0], distribution[1]);
    token = token + roll;
    count++;
    if (token > 16) {
      token = token - roll;
    }
    for (const snake of uu) {
      if (snake[0] == token) {
        token = snake[1];
        count++;
      }
    }
    path.push(token);
  }
  return [path, count];
}
for (let i = 0; i < 100000; i++) {
    countlist.push(simulation1(16))
}
let sum = 0
let c = 0
let min=countlist[0][1]
for (let element of countlist) {
    if (min < element[1]) {
        min = element[1]
        index=countlist.indexOf(element)
    }
    sum+=element[1]
}
console.log(min)
console.log(`average is ${sum/countlist.length} the minimum legnth is ${min} and shortest path is ${countlist[index][0]}`)