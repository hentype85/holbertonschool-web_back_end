import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

try {
    new TestBuilding(200)
}
catch(err) {
    console.log(err);
}
/*
class TestBuilding extends Building {}

test("Building forces override", () => {
  expect(() => {
    new TestBuilding(200);
  }).toThrowError("Class extending Building must override evacuationWarningMessage");
});
*/
