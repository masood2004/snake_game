from turtle import Turtle


class Snake():
    def __init__(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]

        self.segments = []

        for position in starting_position:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(10)
