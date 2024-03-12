#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w != undefined && w > 0) && (h != undefined && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
