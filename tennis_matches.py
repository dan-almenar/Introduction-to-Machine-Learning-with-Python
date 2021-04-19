import random
import pandas as pd

class TennisPlayer(object):
	def __init__(self, name, base_skill=15, skill_court=None, strike_wins=0, strike_lost=0, ego=1):
		self.name = name
		self.base_skill = base_skill
		self.skill_court = skill_court
		self.total_games = 0		
		self.wins = strike_wins
		self.lost = strike_lost
		self.ego = ego
		self.base_skill  = base_skill
		self.match_skill = self.base_skill
	
	def set_ego(self):
		self.ego = (self.wins * 1.2) - (self.lost * 1.2)
		self.ego = round(self.ego, 2)
		return self
	
	def set_skill(self):
		self.base_skill = (self.base_skill+self.ego)+(self.total_games*.05)
		self.base_skill = round(self.base_skill, 2)
		if self.base_skill <=6:
			self.base_skill = 6
		self.match_skill = self.base_skill
		return self


def tennis_match(players):
	players = random.sample(players, 2)
	player1, player2 = players
	court = random.choice(['grass', 'hard', 'clay', 'carpet'])
	for player in players:
		if player.skill_court == court:
			player.match_skill = player.base_skill + 5
	winner = random.choices((player1.name, player2.name),
													weights=[(player1.match_skill*2)**5, (player2.match_skill*2)**5])[0]
	
	match = {'Player 1': player1.name,
					'P1 base skill': player1.base_skill,
					'P1 match skill': player1.match_skill,
					'P1 previous games': player1.total_games,
					'Player 2': player2.name,
					'P2 base skill': player2.base_skill,
					'P2 match skill': player2.match_skill,
					'P2 previous games': player2.total_games,
					'Court': court,
					'Winner': winner}

	update_players_stats(players, winner)
	
	return match

def update_players_stats(players, winner):
	for player in players:
		if player.name == winner:
			player.wins +=1
			player.lost = 0
		else:
			player.lost += 1
			player.wins = 0
	
	for player in players:
			player.total_games +=1
			player.set_ego()
			player.set_skill()
	return

cobain = TennisPlayer('Kurt Cobain', skill_court='grass')
morrison = TennisPlayer('Jim Morrison', skill_court='clay')
jones = TennisPlayer('Brian Jones')
hendrix = TennisPlayer('Jimi Hendrix', base_skill=17, skill_court='hard')
joplin = TennisPlayer('Janis Joplin', base_skill=20)
winehouse = TennisPlayer('Amy Winehouse', base_skill=13, skill_court='carpet')

players = (cobain, morrison, jones, hendrix, joplin, winehouse)

'''

games = [tennis_match(players) for i in range(200)]

df = pd.DataFrame(games)

df.to_csv('tennis_dataframe.csv', index=False)
'''