import random 
import art
import os
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand = []
player_hand = []

def show_dealer_cards(count):
    dealer_hand_minus_one = []
    for i in range(count):
        dealer_hand_minus_one.append(dealer_hand[i])

    print(f"not Full Dealer Hand {dealer_hand_minus_one} total: {sum(dealer_hand_minus_one)} + X")

def show_cards(player, name):
    print(f"{name} Hand {player} total: {sum(player)}")

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
        print(f"Your New Hand {player_hand} total: {sum(player_hand)}\n\n\n")  

def player_stats():
    if sum(dealer_hand) >21:
        print("You Win, Dealer has more than 21")
        show_cards(player_hand, "Your")
        show_cards(dealer_hand, "Dealer")
        dealer_hand.clear()
        player_hand.clear()
    elif sum(player_hand) == 21:
        print("You Win")
        show_cards(player_hand, "Your")
        show_cards(dealer_hand, "Dealer")
        dealer_hand.clear()
        player_hand.clear()
        return False
    elif sum(player_hand) > 21:
        print("You Lose")
        show_cards(player_hand, "Your")
        dealer_hand.clear()
        player_hand.clear()
        return False
    else:
        return True

def check_winner():
    if sum(dealer_hand) <= 21:
        if sum(player_hand) > sum(dealer_hand):
            print("You Win")
            show_cards(player_hand, "Your")
            show_cards(dealer_hand, "Dealer")
        elif sum(player_hand) == sum(dealer_hand):
            print("Draw")
            show_cards(player_hand, "Your")
            show_cards(dealer_hand, "Dealer")
        else:
            print("You Lose")
            show_cards(player_hand,"Your")
            show_cards(dealer_hand,"Dealer")
    else:
        print("You Win, Dealer has more than 21")
        show_cards(player_hand, "Your")
        show_cards(dealer_hand, "Dealer")

def main():
    print(art.logo)
    gameIsActive = True
    iteration = 1
    first_hand(player_hand)
    first_hand(dealer_hand)

    while gameIsActive:
    
        show_cards(player_hand, "Your")
        show_dealer_cards(iteration)
        # print(f"Full Dealer Hand {dealer_hand} total: {sum(dealer_hand)}")
        state = input("\nDraw again? ")
        if state == "y":
            iteration +=1
            another_draw(player_hand) 
            another_draw(dealer_hand) 
            sum_checker()
            gameIsActive = player_stats()
        else:
            #break 
            gameIsActive = False
            check_winner()


while True:
    main()
    start_again = input("\n\n\nCare to Play Again? ")
    if start_again == "y":
        os.system('cls')
        main()
    else:
        print(art.bye)
        break
