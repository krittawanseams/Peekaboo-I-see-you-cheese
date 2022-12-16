# Peekaboo-I-see-you-cheese
This program is apart of Computer Programming 1 course.
Inspired by Pac-Man game and I had to give the characters a sense of gravity.


### Overview and features

In this game, the mouse finds cheeses, which is about collecting cheeses, an accumulation of cheeses is made. There are cats that are an impediment. The cat will walk around, if the cat not catching the mouse, and the mouse will walk to the point of the pink circle. You'll advance to the next level.

The mouse is controlled by the arrow keys: press the up arrow to jump, the left arrow to move to the left, the right arrow to move to the right, and the space bar to high jump.


### Program's requirement

There are 2 Python modules required in the program

`turtle` : used for the display part 

`json` : used for collect various maps


### Program design

There are six classes in this program.

`Pen` : This class defines the shape of the map's wall.

`Stage` : This class includes a function for randomizing a map from the maps.json file.

`Player` : This class has the shape of a mouse character and the methods of jumping, walking left, walking right, high jump, and checking whether or not it collided with another.

`Enemy` : This class has the shape of cats.

`Cheese` : This class has the shape of cheeses and disappear when they collide with the mouse.

`NextLevel` : This class defines the shape of the next level.


### Code structure


This program consists of 6 python files and  1 json file.
* [stage.py](stage.py) : contains the Stage class, Pen class and loop-stage function
* [main.py](main.py) : run the main program.
* [mouse.py](mouse.py) : contains the Player class
* [cat.py](cat.py) : contains the Enemy class
* [cheese.py](cheese.py) : contains the Cheese class
* [next_level.py](next_level.py) : contains the NextLevel class
* [maps.json](maps.json) : contains various maps of this game.


