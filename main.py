import random 

cards = [11,11,11,11,11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
player_hand = []


def deal_card():
    return random.choice(cards)

def first_hand(player):
    for i in range(2):
        card = deal_card()
        player.append(card)

def another_draw(player):
    card = deal_card()
    player.append(card)

def sum_checker():
    # print(f"Your Hand {player_hand} total: {sum(player_hand)} Lets Check Sum")
    if sum(player_hand) > 21 and 11 in player_hand:
        print(f"Your Hand {player_hand} total: {sum(player_hand)} Changing 11 to 1")
        for i in range(len(player_hand)):
            if player_hand[i] == 11:
                player_hand[i] = 1
        print(f"Your New Hand {player_hand} total: {sum(player_hand)}")  

def player_stats():
    if sum(player_hand) == 21:
        print("You Win")
        print(f"Your Hand {player_hand} total: {sum(player_hand)}")
        return False
    elif sum(player_hand) > 21:
        print("You Lose")
        print(f"Your Hand {player_hand} total: {sum(player_hand)}")
        return False
    else:
        return True

first_hand(player_hand)
first_hand(dealer_hand)

gameIsActive = True

while gameIsActive:
    print(f"Your Hand {player_hand} total: {sum(player_hand)}")
    print(f"Dealer Hand {dealer_hand} total: {sum(dealer_hand)}")
    state = input("again? ")
    if state == "y":
        another_draw(player_hand) 
        sum_checker()
        gameIsActive = player_stats()
    else:
        break #Compare hands
