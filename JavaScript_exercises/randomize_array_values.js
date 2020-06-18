const codeBrainersStudents = [
    {
        name: 'Michał K.',
        coffees: 1
    },
    {
        name: 'Michał M.',
        coffees: 1
    },
    {
        name: 'Joanna',
        coffees: 2
    },
    {
        name: 'Karolina',
        coffees: 3
    },
    {
        name: 'Grzegorz',
        coffees: 0
    },
    {
        name: 'Damian',
        coffees: 1
    },
    {
        name: 'Sabina',
        coffees: 1
    },
    {
        name: 'Kamila',
        coffees: 0
    },
    {
        name: 'Maksym',
        coffees: 2
    }
];


function copyArray(arr) {
    const newArray = [];

    for (let i = 0; i < arr.length; i++) {
        const student = arr[i];
        newArray.push(student);
    }
    return newArray;
}


function shuffleArray(arr) {
    let temporaryArray = copyArray(arr);
    let shuffledArray = [];

    for (let i = 0; i < arr.length; i++) {
        const randomIndex = Math.floor(Math.random() * temporaryArray.length);
        let student = temporaryArray[randomIndex];
        shuffledArray.push(student);
        temporaryArray.splice(randomIndex, 1);
    }
    return shuffledArray;
}

let randomizedArray = shuffleArray(codeBrainersStudents);


function displayNamesFromArray(arr) {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i].name);
    }
}

displayNamesFromArray(randomizedArray);
