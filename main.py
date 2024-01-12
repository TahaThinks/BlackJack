import random 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
player_hand = []

def deal_card():
    return random.choice(cards)


for i in range(2):
    card = deal_card()
    player_hand.append(card)

for i in range(2):
    card = deal_card()
    dealer_hand.append(card)

