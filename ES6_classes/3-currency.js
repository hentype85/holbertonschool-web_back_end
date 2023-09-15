export default class Currency {
  // constructor
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // getter
  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  // setter
  set code(newCode) {
    this._code = newCode;
  }

  set name(newName) {
    this._name = newName;
  }

  // return the attributes
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
