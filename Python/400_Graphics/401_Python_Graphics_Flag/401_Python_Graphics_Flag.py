
from graphics import *;


window = GraphWin("Window", 500,500);

Rectangle1 = Rectangle(Point(50,50), Point(400,250));
Rectangle1.draw(window);
Rectangle1.setFill("red")

Rectangle2 = Rectangle(Point(50,50), Point(230,150));
Rectangle2.draw(window);
Rectangle2.setFill("blue")

Rectangle3 = Rectangle(Point(30,50), Point(50,500));
Rectangle3.draw(window);
Rectangle3.setFill("grey")

window.getMouse();
window.close();

