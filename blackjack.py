import random

DECKSIZE = 2
#these classes outline what a deck is and the values of the cards as well as 
# deck manipulation functions like shuffle and draw


#how each card is stored
class Card:	#this is the actual cards
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return f"{self.value} of {self.suit}"

#contains function shuffle and draw
class Deck:	#this is a deck of cards (using class Card)
	def __init__(self):
		self.cards = []	#this is the "deck"
		self.discard = [] #this is the discard pile that will take the cards after they're used (to reset deck)
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
		for i in range(DECKSIZE):
			for suit in suits:
				for value in values:
					card = Card(suit, value)
					self.cards.append(card)
		self.shuffle()
		
	def reset(self):
		self.cards.extend(self.discard)	#adds back all discarded (used) cards
		self.discard.clear()	#discard pile is empty now
		self.shuffle()		#shuffles the deck all together again

	def shuffle(self):	#this shuffles the deck
		random.shuffle(self.cards)

	def draw(self, n=1):		#this draws a card and allows you to draw multiple
#		print(self.cards[-1])	
		if len(self.cards) < n:	#this should never happen, but in case try to draw more cards than there are in deck (or deck empty)
			self.reset()		#reset the deck (shuffle all cards together)
		return [self.cards.pop() for _ in range(n)]


#this next class takes care of the dealer's hand and functions the dealer deals with 
#such as 

class Dealer:
	def __init__(self, deck):	#to create SAME deck between dealer and player it'll be passed in
		self.hand = []			#this is the dealers hand at all times
		self.deck = deck		#this creates the deck to be played with

	def __str__(self):
		cards = [str(card) for card in self.hand]
		return ', '.join(cards)

	def deal(self, n=1):				#this should be adding two cards to dealers hand
		self.hand += self.deck.draw(n)
#		for _ in self.hand:
#			print(_.value)

	def play(self):				#this should have dealer draw until they hit soft 17
		while self.hand_value() < 17:
			self.deal()
			#self.hand += self.deck.draw()
		#print(self.hand_value())
		return self.hand_value()

	def hand_value(self):		#this is how you determine the dealer's hand value
		value = 0	#store the soft hand value
		ace = 0		#store number of aces in hand
		for card in self.hand:
			if card.value in ["Jack", "Queen", "King"]:
				value += 10
			elif card.value == "Ace":
				ace += 1
				value += 11	#soft value

			else:
				value += int(card.value)

		while ace and (value > 21 or value == 17):	#as long as there's soft aces I'll reduce
			ace -= 1		#each ace turned hard (1) reduces number of soft aces
			value -= 10		#soft ace = 11, hard ace = 1

		return value

class Player:
	def __init__(self, deck):
		self.hand = []
		self.deck = deck

	def __str__(self):
		cards = [str(card) for card in self.hand]
		return ', '.join(cards)

	def deal(self, n=1):				#this is to add cards to player's hand
		self.hand += self.deck.draw(n)
	
	def hit(self):				#this is player hitting (draw a card)
		self.deal()	#should add a card from the dealer's deck to player's hand
		#print(self.hand_value())
		return self.hand_value()

	def hand_value(self):		#this is how you determine the dealer's hand value
		value = 0	#store the soft hand value
		ace = 0		#store number of aces in hand
		for card in self.hand:
			if card.value in ["Jack", "Queen", "King"]:
				value += 10
			elif card.value == "Ace":
				ace += 1
				value += 11	#soft value

			else:
				value += int(card.value)

		while ace and value > 21:	#as long as there's soft aces I'll reduce
			ace -= 1		#each ace turned hard (1) reduces number of soft aces
			value -= 10		#soft ace = 11, hard ace = 1

		return value

class Blackjack():
	def __init__(self):
		self.deck = Deck()
		self.dealer = Dealer(deck)
		self.player = Player(deck)

	def play_game(self):
		self

	def endRound(self):
		self.deck.reset()
		self.dealer.hand.clear()
		self.player.hand.clear()		#clears both dealer and player's hands (since they're now discarded)






def playRound():#play round of blackjack, dealer deals and then player hits/stays	
	my_player.deal()
	my_dealer.deal()
	dealerShows = str(my_dealer)
	my_player.deal()
	my_dealer.deal()
	return(dealerShows)

def playGame(): #play the game until player wants to 'Leave'
	deck = Deck()


#how a round of blackjack goes
#player places bets
#dealer deals at one card at a time, starts with player ends with self
#dealer deals 2nd card to players and leaves their 2nd card face down
#players choose to hit, double, (split if able), or stand
#dealer turns over their card, and hits until at least HARD 17 (in this mode)
#if deck is < 50%, dealer shuffles deck again, and repeat

deck = Deck()
if len(deck.cards) < DECKSIZE*26:	#checks that the current deck isn't less than half, otherwise remakes it
	deck = Deck()
my_dealer = Dealer(deck)
my_player = Player(deck)

dealerShows = playRound(deck)#, my_dealer, my_player)
print("Dealer shows: " + dealerShows)
#playerTurn = input("Hit or Stay?")
while input("You have: " + str(my_player) + " for " + str(my_player.hand_value()) + " - Hit or Stay?") == "Hit":
	my_player.deal()
	if my_player.hand_value() > 21:
		print("You busted.")
		break

my_dealer.play()

print(my_dealer)
if my_dealer.hand_value() > my_player.hand_value() and my_dealer.hand_value() < 22:
	print("You lose.")