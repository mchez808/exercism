'''
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game

Your task is to write methods that return
- the highest score from the list,
- the last added score,
- the three highest scores,
- and a report on the difference between the last and the highest scores.
'''

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        latest = self.scores[-1]
        personal_best = max(self.scores)
        if latest == personal_best:
            message = "Your latest score was {0}. That's your personal best!".format(latest)
        else:
            message = "Your latest score was {0}. That's {1} short of your personal best!".format(latest, personal_best - latest)
        return message
