export default class Building {
  constructor(sqft) {
    // Prevents instantiation of an abstract class instance
    // check if this instance is not an instance of the Building class
    // and if the evacuationWarningMessage method is not overridden
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }

    this._sqf = sqft;
  }

  // getter
  get sqft() {
    return this._sqf;
  }
}
