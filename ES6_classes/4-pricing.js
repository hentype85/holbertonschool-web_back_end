export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // getter
  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  // setter
  set amount(newAmount) {
    this._amount = newAmount;
  }

  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  // method return the attributes
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // static method convert price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}