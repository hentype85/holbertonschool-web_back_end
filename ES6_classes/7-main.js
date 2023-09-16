import Airport from "./7-airport.js";
/*
const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);
console.log(airportSF.toString());
*/
const airportSF = new Airport();
airportSF._name = 'San Francisco Airport';
airportSF._code = 'SFO';
console.log(airportSF);
console.log(airportSF.toString());