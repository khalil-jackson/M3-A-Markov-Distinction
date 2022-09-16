# M3-A-Markov-Distinction
Create a coding project that uses a Markov chain to generate visual art

System Title: A Little Turtle Goes a Long Way

Description: This project seeks to create a piece of visual art by the use of Markov matrices in Turtle. The idea is two break the project down into two sections: 1. the strategy to implement a markov matrix to create a list of directions that will serve as the turtle's route and 2. the strategy to take in lists of directions and make the turtle follow those directions accordingly.

System Documentation: markov_turtle.py uses the Turt class, the get_next_movement function, the compose_route function, and a Markov matrix to determine the route of the turtle. get_next_movement takes in the current direction of the turtle and uses numpy.random.choice to take the probabilities of transitioning from that direction to another to generate the next step. compose_route creates a list of those directions by starting with one, what is referred to as the prior, and call on the previous function until the desired length of the function is reached; then that value is returned. The main asks for user input to get the prior and the length of the route.

turtle_routing.py contains a helper function, move_turtle, that takes in a list of directions, iterates through them, then takes thos directions and implements them in Turtle; markov_turtle.py imports this helper function from the file and passes in the list from compose_route to make the visual art.

To run the code, you input a direction--forward, left, right, or back--along with a number between 1 and 100; these inputs serve as the prior and route length, respectively. From there, the markov_turtle.py file creates the list then uses the imported function from turtle_routing.py to create the piece.

Creativity: I beleive this project to be creative because it requries a level of abstraction to see ranomized line patterns as a result of randomized probabilities.

Challenges: This project was a challenging one for me, because I have not coded in Python since my first semester of college, which was six semesters ago. Even if I were still somewhat actively coding in Python, it is not the easiest language for me to code in (I found Java to be a language I gravitated towards quickly and can still get back into it little-to-no effort). Figuring out a language again, fixing bugs, and using a new text editor to complete a project in a week where I only have about 3-4 unscheduled hours is a huge task.

Meaning to Me: I like the idea of revisiting things I have done before and seeing how I am now relative to then. Using the same language and the same library I used to begin my time as a computer scientist allows me to see exactly how far I have come in attitude, understanding, and the efficiency in which I break down a problem and absorb information. This project helped me familiarize myself with Python more so than I think simple exercizes would have, and now I know my defficiencies and where I need to focus my attention on (mainly identifying bugs and remembering Python conventions).

