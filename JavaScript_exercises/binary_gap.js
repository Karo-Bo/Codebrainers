function changeIntoBinaryArray(N) {
    let binaryArray = [];
    let temporaryN = N;

    while (temporaryN != 0) {
        let remainder = temporaryN % 2;
        binaryArray.push(remainder);
        temporaryN = Math.floor(temporaryN / 2);
    }
    return binaryArray;
}


function maxBinaryGap(binaryArray) {
    let currentGap = 0;
    let maximumGap = 0;

    for (let i = 0; i < binaryArray.length; i++) {
        if (binaryArray[i] === 1) {
            // if (binaryArray[i + 1] === 0) {
            for (let j = 0; j < (binaryArray.length - i); j++) {
                if (binaryArray[i + j] === 0) {
                    currentGap++;
                    maximumGap = Math.max(maximumGap, currentGap);
                } else {
                    currentGap = 0;
                }
            }
            // }
        }
    }
    return maximumGap;
}


function solution(N) {

    let maximumBinaryGap = maxBinaryGap(changeIntoBinaryArray(N));

    return maximumBinaryGap;
}


console.log(maxBinaryGap(changeIntoBinaryArray(2172)));
console.log(maxBinaryGap(changeIntoBinaryArray(1041)));
console.log(maxBinaryGap(changeIntoBinaryArray(15)));
console.log(maxBinaryGap(changeIntoBinaryArray(32)));
console.log(maxBinaryGap(changeIntoBinaryArray(591)));

// console.log(4 % 2);
// console.log(Math.floor(4 / 2));