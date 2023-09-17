export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // when the class is cast into a Number, it return the size
  valueOf() {
    return this._size;
  }

  // when the class is cast into a String, it return the location
  toString() {
    return this._location;
  }
}
  