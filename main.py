import ast
import turtle


varInput = ' '
verify = False
database = {}

def getAllRecords():
    global database
    with open('db.txt') as data:
        f = data.read()
        database = ast.literal_eval(f)


def getInput():
    global varInput
    varInput = input("Enter a shape:(Triangle, Square, Pentagon, Hexagon)")  # input

def verifyShape(shape):
    global verify
    if shape in database.keys():
        print('Shape found')
        verify = True
        return verify
    else:
        print('Not found')
        verify = False
        return verify


def drawTriangle():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(50)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def drawSquare():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(50)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def drawPentagon():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(50)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def drawHexagon():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(50)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def printShape(isTrue):
    global varInput
    if isTrue:
        if varInput == 'Triangle':
            drawTriangle()
        elif varInput == 'Square':
            drawSquare()
        elif varInput == 'Pentagon':
            drawPentagon()
        elif varInput == 'Hexagon':
            drawHexagon()
        else:
            print('Finish')
    else:
        print('Shape not found')

#




if __name__ == '__main__':
    getAllRecords()
    getInput()
    verifyShape(varInput)
    printShape(verify)
