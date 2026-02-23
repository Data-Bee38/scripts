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

//crypto
const sha256 = async s => [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)))].map(b => b.toString(16).padStart(2,"0")).join("");
sha256("hello world").then(console.log);
// => b94d27b9934d3e08a52e52d7da7dabfade...

//global ipv6
const randomGlobalIPv6 = () => [(0x2000 + Math.floor(Math.random()*0x2000)).toString(16).padStart(4,"0"), ...Array.from({length:7},()=>Math.floor(Math.random()*0x10000).toString(16).padStart(4,"0"))].join(":");

//link local ipv6
const randomLinkLocalIPv6 = () => ["fe80","0000","0000","0000",...Array.from({length:4},()=>Math.floor(Math.random()*0x10000).toString(16).padStart(4,"0"))].join(":");

//private ipv6
const randomULA = () => [`fd${Math.floor(Math.random()*256).toString(16).padStart(2,"0")}`, ...Array.from({length:7},()=>Math.floor(Math.random()*0x10000).toString(16).padStart(4,"0"))].join(":");

//multicast
const randomMulticastIPv6 = () => ["ff"+Math.floor(Math.random()*16).toString(16)+["1","2","5","8","e"][Math.floor(Math.random()*5)], ...Array.from({length:7},()=>Math.floor(Math.random()*0x10000).toString(16).padStart(4,"0"))].join(":");

//1	interface-local          ex) ff71:f308:0a98:59b2:98f7:b771:33ca:289a 
//2	link-local               ex) fff2:d2b9:e14f:89b4:3fab:4fa8:c8a3:9725
//5	site-local               ex) ffb5:5472:b8e8:cd74:d673:dd2f:da55:a13a
//8	organization-local       ex) ffe8:6824:be5b:8a4c:bc49:b2a5:4cc4:0557
//e	global                   ex) ffae:61e9:6cf0:c426:4cfc:df61:e3ed:0ae6





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
    <button type="button" id="submitButton" >Submit</button>

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







