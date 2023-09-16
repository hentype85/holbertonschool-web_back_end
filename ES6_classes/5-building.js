export default class Building {
  constructor(sqft) {
    // prevents instantiation of an abstract class instance
    if (this.constructor !== Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }

    this._sqf = sqft;
  }

  // getter
  get sqft() {
    return this._sqf;
  }
}
