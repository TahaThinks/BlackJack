import random 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
player_hand = []

def deal_card():
    card = random.choice(cards)
    print(card)

deal_card()