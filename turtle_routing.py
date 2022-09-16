"""
    Written by Khalil Jackson

    Is called by the markov_turtle file to take a list then use the list items
    to create Turtle art.
"""

from shutil import move
import turtle

turt = turtle.Turtle()


def move_turtle(self, turtle_route):
    """
        Takes a list of directions and calls the appropriate turtle
        function to move the graphic.
    """

    for move in range(0, len(turtle_route)):

        if turtle_route[move] == "forward":
            turt.forward(100)
        elif turtle_route[move] == "left":
            turt.left(100)
        elif turtle_route[move] == "right":
            turt.right(100)
        else:
            turt.back(100)


move_turtle(["right", "left", "forward", "right", "left", "forward"])

turtle.done()
