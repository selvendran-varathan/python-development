'Parse a json file'

import yaml

#1 Acquire the data
with open('notes/team_history.json') as f:
    hist = yaml.load(f)

#2 Parse data and convert to a convenient form
dates = [game['date'] for game in hist]
scores = [game['score'] for game in hist]
record = [game['result'] for game in hist]

#3 Do the actual testing or data analysis
print('This season, we played %d games from %s to %s' % (len(record), dates[0], dates[-1]))
print('Our record was %s-%s' % (record.count('won'), record.count('lost')))
print('We %s the first game and %s the last game' % (record[0], record[-1]))
print('We scored %d goals this season' % sum(scores))
print('Or best game had %d goals and out fewest was %d goal' % (max(scores), min(scores)))

