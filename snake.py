from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(position)
        self.snake_segments.append(new_segment)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.setposition(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        length_of_snake = len(self.snake_segments)
        for segment in range(length_of_snake - 1, 0, -1):
            x_pos = self.snake_segments[segment - 1].xcor()
            y_pos = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].setposition(x=x_pos, y=y_pos)

        self.snake_head.forward(20)
        # self.snake_segments[0].left(90)

    def up(self):
        current_heading = self.snake_head.heading()
        if current_heading == 0 or current_heading == 180:
            self.snake_head.setheading(90)

    def down(self):
        current_heading = self.snake_head.heading()
        if current_heading == 0 or current_heading == 180:
            self.snake_head.setheading(270)

    def left(self):
        current_heading = self.snake_head.heading()
        if current_heading != 0:
            self.snake_head.setheading(180)
        # else:
        #     self.snake_segments[0].setheading(current_heading + 90)

    def right(self):
        current_heading = self.snake_head.heading()
        if current_heading != 180:
            self.snake_head.setheading(0)
        # else:
        #     self.snake_segments[0].setheading(current_heading - 90)
