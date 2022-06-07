from graphics import *;

window = GraphWin("Window", 500,500);

impostertext = Text(Point(250,250), "amogas")
impostertext.setSize(30)
impostertext.setFace('helvetica')
impostertext.setTextColor('cyan')

impostertext.draw(window)

window.getMouse();
window.close();
