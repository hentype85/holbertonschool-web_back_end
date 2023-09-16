export default class Building {
  constructor(sqft) {
    this._sqf = sqft;
  }

  //getter
  get sqft() {
    return this._sqf;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
