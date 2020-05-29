import pingpong


class HumanPlayer:

    def __init__(self, coordinates):
        self.score = 0
        self.reaction_range = 0
        self.paddle = pingpong.Paddle(coordinates=coordinates)

    @staticmethod
    def is_human():
        return True


class ComputerPlayer:

    def __init__(self, coordinates):
        self.score = 0
        self.reaction_range = (50, 800) # Easy: 10000, Medium: 1000, Hard: 100
        self.paddle = pingpong.Paddle(coordinates=coordinates)

    @staticmethod
    def is_human():
        return False
