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

//IP Address Locator ====================================================================================================================================================

//ipaddress to decimal converter
function ipConverter(input) {
    return typeof input === 'number' ?
        ( (input>>>24) +'.' + (input>>16 & 255) +'.' + (input>>8 & 255) +'.' + (input & 255) ) :
        typeof input === 'string' ?
            input.split('.').reduce(function(ipInt, octet) { return (ipInt<<8) + parseInt(octet, 10)}, 0) >>> 0 :
            (() => { throw new Error("Input must be either a string representing an IP address or an integer."); })();
}

async function getLocationByIpOrInt(ipAddress) {
    try {
        // Convert IP address to decimal
        const decimalIp = typeof ipAddress == "string" ? ipAddress : ipConverter(ipAddress);
        
        // Fetch location using decimal IP address
        const response = await fetch(`https://ipinfo.io/${decimalIp}/json`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching location:', error);
        return null;
    }
}


    /*

    // HTML
    <input type="text" name="addr" value="" id="addr" placeholder="type ip address here...." />
    <button type="button" id="submitButton" ><i class="fa fa-2x fa-arrow-right" aria-hidden="true"></i></button>

    */

    document.getElementById('submitButton').addEventListener('click', function() {
        // Get the value of the input field
        const inputValue = document.getElementById('addr').value;

        // Call the getLocationByIpOrInt() function with the input value as a parameter
        getLocationByIpOrInt(ipConverter(inputValue)).then(locationData => {
            var res = locationData.loc.split(",").map(x=>parseInt(x));
            var lat = res[0];
            var lon = res[1];

            console.log(lat);
            console.log(lon);
            console.log(locationData.city);
            console.log(locationData.region);
            console.log(locationData.country);
            console.log(locationData.postal);
            console.log(locationData);
            
        });
    });

