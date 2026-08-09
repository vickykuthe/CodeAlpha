class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_played = 0
        self.games_won = 0

    def add_win(self, score):
        self.score += score
        self.games_played += 1
        self.games_won += 1

    def add_loss(self):
        self.games_played += 1

    def win_rate(self):

        if self.games_played == 0:
            return 0

        return (self.games_won / self.games_played) * 100