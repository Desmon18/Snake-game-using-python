from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = int(self.read_previous_score())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard(0)

    def read_previous_score(self):
        with open("data.txt", mode="r") as data:
            return data.read()

    def write_new_score(self, high_score):
        with open("data.txt", mode="w") as data:
            data.write(str(high_score))

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=('Times New Roman', 20, 'normal'))

    def count_score(self, score):
        self.clear()
        self.write(arg=f"Score = {score}", move=False, align="center", font=('Times New Roman', 20, 'normal'))

    def reset_score(self, score):
        if score > self.high_score:
            self.high_score = score
            self.write_new_score(self.high_score)
        self.update_scoreboard(0)

    def update_scoreboard(self, score):
        self.clear()
        self.write(arg=f"Score: {score}  High Score: {self.high_score}", move=False, align="center",
                   font=('Times New Roman', 20, 'normal'))
