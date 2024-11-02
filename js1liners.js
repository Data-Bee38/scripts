// Generates a random number between min and max
const randnum = (min, max) => Math.round(Math.random() * (max - min)) + min;

// Tells if a number is odd
const isodd = num => num % 2 !== 0;

// Tells if a number is even
const iseven = num => num % 2 === 0;

// Generates a hex color
const genhexcolor = () => '#' + Array.from({ length: 6 }, () => '1234567890ABCDEF'[Math.floor(Math.random() * 16)]).join('');

// Randomizes an array (Fisher-Yates shuffle)
const shufflearray = array => array.sort(() => Math.random() - 0.5);

// Gets a random item from an array
const getarrayitem = arr => arr[Math.floor(Math.random() * arr.length)];

// Removes an item from an array
const removeitem = (array, item) => array.filter(el => el !== item);

// Checks if an array has an item
const hasitem = (array, item) => array.includes(item);

//break array into chunk sizes
const chunk = (arr, size) => Array.apply(null, {length: Math.ceil(arr.length/size)}).map((v, i) => arr.slice(i*size, i*size+size));
