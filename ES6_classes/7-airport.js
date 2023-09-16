export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // customize the string representation of this object
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
