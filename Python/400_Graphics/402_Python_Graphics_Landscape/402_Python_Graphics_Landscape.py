import random
from graphics import *;

window = GraphWin("Window", 500,500);

Rectangle1 = Rectangle(Point(-100,-100), Point(600,600));
Rectangle1.draw(window);
Rectangle1.setFill("cyan")
Rectangle1.setOutline("cyan")

Rectangle2 = Rectangle(Point(0,250), Point(600,600));
Rectangle2.draw(window);
Rectangle2.setFill("green")
Rectangle2.setOutline("green")

Sun = Circle(Point(70,70), 50)
Sun.draw(window);
Sun.setFill("yellow")
Sun.setOutline("yellow")

pnt1 = 50

for x in range(0,11):
    pnt2 = random.randrange(270, 480)
    Sun = Circle(Point(pnt1, pnt2), 15)
    Sun.draw(window);
    Sun.setFill("grey")
    Sun.setOutline("grey")
    pnt1 = pnt1 + 40

window.getMouse();
window.close();

