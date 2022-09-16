"""
    Written by Khalil Jackson

    This file uses the Turtle class, helper functions, and a Markov matrix to determine the
    route of the turtle.

"""

import numpy as np
import random as rm
from turtle_routing import move_turtle


class Turt():
    def __init__(self, movement_matrix, direction):
        """
            Creates a class for Turtle
            Args:
                movement_matrix: Markov matrix of movement probabilities
                direction: the prior for the Markov matrix
        """
        self.movement_matrix = movement_matrix
        self.movements = list(movement_matrix.keys())
        self.direction = direction


    def get_next_movement(self, current_move):
        """
            Decides the next move the turtle will take
            Args:
                current_move: the current move the turtle is taking
        """
        return np.random.choice(
            self.movements, 
            p=[self.movement_matrix[current_move][next_move] for next_move in self.movements]
            )


    def compose_route(self, current_move, route_length):
        """
            Generates a sequence of moves the turtle will take
            Args:
                current_move: the current move we're looking at
                route_length: the number of moves the turtle will take
        """

        route = []

        route.append(current_move)

        while len(route) < route_length:
            next_move = self.get_next_movement(current_move)
            route.append(next_move)
            current_move = next_move

        return route



def main():
    """
        The main function asks for input that determines the prior move and the length
        of the turtle's route. It creates a Turt class with a matrix for moves
        adn a matric for background color then calls compose_route which uses the 
        helper function get_next_movement to create lists of directions and colors
        filled by the probabilities in the respective Markov matrix.
    """

    direction = input("Which direction would you like to go: forward, backward, left, or right?")
    direction = str.lower(direction)

    route_length = input("What's your favorite number from 1-100?")
    route_length = float(route_length)


    turtle_maker = Turt(
        {
        "forward": {"forward": 0.3, "left": 0.2, "right": 0.2, "backward": 0.3}, 
        "left": {"forward": 0.3, "left": 0.2, "right": 0.2, "backward": 0.3}, 
        "right": {"forward": 0.3, "left": 0.2, "right": 0.2, "backward": 0.3}, 
        "backward": {"forward": 0.3, "left": 0.2, "right": 0.2, "backward": 0.3}},
        direction
        )


    print(turtle_maker.movements)
    print(turtle_maker.compose_route(direction, route_length))


main()