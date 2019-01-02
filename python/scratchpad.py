'''
Your task: return
- the highest score from the list,
- the last added score,
- the three highest scores,
- and a report on the difference between the last and the highest scores.
'''

scores = [30, 20, 70, 50]

latest = scores[-1]

personal_best = max(scores)

middlelist = scores.copy()
middlelist.sort(reverse=True)
personal_top = middlelist[:3]

if latest == personal_best:
    message = "Your latest score was {0}. That's your personal best!".format(latest)
else:
    message = "Your latest score was {0}. That's {1} short of your personal best!".format(latest, personal_best-latest)
