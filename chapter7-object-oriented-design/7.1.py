# 7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would subclass the data structures
# to implement blackjack.
import pdb
from random import shuffle

class DeckOfCards:
	def __init__(self, num_of_decks=4):
		self.clear_decks(num_of_decks)

	def clear_decks(self, num_of_decks=4):
		self.remaining = [i for i in range(1, 14) for j in range(num_of_decks)]
		shuffle(self.remaining)
		self.fold = []

	def draw(self):
		# if no more cards to draw, we are going to shuffle the fold and
		# add them back to remaining
		if not self.remaining:
			# if no more cards in the fold to shuffle, meaning all cards
			# are drawn and no one put back
			if not self.fold:
				raise Exception()
			else:
				shuffle(self.fold)
				self.remaining = self.fold
				self.fold = []

		# after the check of the emptiness of remaining, draw a card
		return self.remaining.pop()

	def num_of_remaining(self):
		return len(self.remaining)

class BlackJack(DeckOfCards):
	"""
	>>> engine = BlackJack()
	>>> dealer = engine.register_dealer()
	>>> player1 = engine.register_player("player1")
	>>> player2 = engine.register_player("player2")
	>>> player3 = engine.register_player("player3")
	>>> engine.initialize_bet()
	>>> engine.bet(player1, 20)
	>>> engine.bet(player2, 30)
	>>> engine.bet(player3, 40)
	>>> engine.hit(dealer)
	>>> engine.hit(dealer)
	>>> engine.hit(player1)
	>>> engine.hit(player1)
	>>> engine.hit(player2)
	>>> engine.hit(player2)
	>>> engine.hit(player3)
	>>> engine.hit(player3)

	"""
	def __init__(self):
		# initialize players and dealer
		self.player = {}
		self.bets = {}
		super().__init__()

	def register_dealer(self, chip=1000):
		self.player["dealer"] = {"chip": chip, "name": "dealer"}
		return self.player["dealer"]

	def register_player(self, name, chip=100):
		if name == "dealer":
			print("Illegal name!")
			return
		self.player[name] = {"chip": chip, "name": name}
		return self.player[name]

	def initialize_bet(self):
		self.clear_decks()
		self.bets = {}
		for name in self.player:
			self.bets[name] = {"cards": []}

	def bet(self, player, chip):
		if chip <= self.player[player["name"]]["chip"]:
			self.bets[player["name"]]["bet"] = chip
		else:
			print("Not enough chip!")

	def hit(self, player):
		self.bets[player["name"]]["cards"].append(self.draw())
		if self.value(player) > 21:
			bet = self.bets[player["name"]]["bet"]
			self.player["dealer"]["chip"] += bet
			player["chip"] -= bet
			del self.bets[player["name"]]
			return False
		else:
			return True

	def value(self, player):
		cards = self.bets[player["name"]]["cards"]
		ace_count = cards.count(1)
		if ace_count == 0:
			return sum([min(i, 10) for i in cards])
		else:
			temp_sum = sum([min(i, 10) for i in cards]) + ace_count * 10
			# maximize the sum while keeping it <= 21
			while ace_count > 0 and temp_sum > 21:	
				temp_sum -= 10
				ace_count -= 1
			return temp_sum

	def stand(self, player):
		self.bets[player["name"]]["value"] = self.value(player)

	def check_dealer_cards(self):
		return self.bets["dealer"]["cards"][0]

	def check_player_cards(self, player):
		return self.bets[player["name"]]["cards"]

	def checkout(self):
		if "dealer" not in self.bets:
			for name, bet_info in self.bets.items():
				self.player["dealer"]["chip"] -= bet_info["bet"]
				self.player[name]["chip"] += bet_info["bet"]				
		else:
			dealer_value = self.value(self.player["dealer"])
			for name, bet_info in self.bets.items():
				if name != "dealer":
					player_value = self.value(self.player[name])
					if player_value > dealer_value:
						self.player["dealer"]["chip"] -= bet_info["bet"]
						self.player[name]["chip"] += bet_info["bet"]
					elif player_value < dealer_value:
						self.player["dealer"]["chip"] += bet_info["bet"]
						self.player[name]["chip"] -= bet_info["bet"]





if __name__ == "__main__":
	engine = BlackJack()
	dealer = engine.register_dealer()
	player1 = engine.register_player("player1")
	player2 = engine.register_player("player2")
	player3 = engine.register_player("player3")
	engine.initialize_bet()
	engine.bet(player1, 20)
	engine.bet(player2, 30)
	engine.bet(player3, 40)
	engine.hit(dealer)
	engine.hit(dealer)
	engine.hit(player1)
	engine.hit(player1)
	engine.hit(player2)
	engine.hit(player2)
	engine.hit(player3)
	engine.hit(player3)
	
	pdb.set_trace()
