function addTwoNumbers(l1, l2) {
    let revrse1 = l1.reverse()
    let revrse2 = l2.reverse()
    let stringarry1 = []
    let stringarry2 = []
    revrse1.forEach((element) => {
        stringarry1.push(element.toString())
    })
    let total1 = stringarry1.reduce((total, element) => {
        return total + element
    })
    revrse2.forEach((element) => {
        stringarry2.push(element.toString())
    })
    let total2 = stringarry2.reduce((total, element) => {
        return total + element
    })
    let sum = parseInt(total1) + parseInt(total2)
    //console.log(Array.from(sum))
    let myFunc = num => Number(num);
    var intArr = Array.from(String(sum), myFunc);
    return intArr.reverse()
}
//console.log(addTwoNumbers([2,4,3],[5,6,4])) 
//708