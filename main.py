import random 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
player_hand = []

def deal_card():
    return random.choice(cards)

def first_hand(player):
    for i in range(2):
        card = deal_card()
        player.append(card)

first_hand(player_hand)
first_hand(dealer_hand)

player_hand_sum = 0

while player_hand_sum < 21:
    print(f"Your Hand {player_hand} total: {sum(player_hand)}")
    print(f"Dealer Hand {dealer_hand} total: {sum(dealer_hand)}")
    
    state = input("again? ")
    if state == "y":
        card = deal_card()
        player_hand.append(card)
        player_hand_sum += sum(player_hand)
    else:
        break

print(f"You Lose {player_hand} total: {sum(player_hand)}")