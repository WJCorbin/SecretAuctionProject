import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    global dealer1
    global dealer2
    global player1
    global player2
    global dealer_hand
    global player_hand
    global dealer_total
    global player_total
    
    dealer1 = random.randint(0, len(cards)-1)
    dealer2 = random.randint(0, len(cards)-1)
    dealer_hand = [dealer1, dealer2]
    player1 = random.randint(0, len(cards)-1)
    player2 = random.randint(0, len(cards)-1)
    player_hand = [player1, player2]
    dealer_total = dealer1 + dealer2
    player_total = player1 + player2
    if dealer_total == 21:
        print(f"Dealer's Hand:  {dealer_hand}")
        print(f"Dealer's Total: {dealer_total}")
        print(f"Player's Hand:  {player_hand}")
        print(f"Player's Total: {player_total}")
        print("Dealer has BlackJack, You Lose!!!")
        choice = input("Would you like to continue? Press 'y' or 'n': ")
        if choice == "y":
          deal()  
        else:
            return
    dealer2 = dealer_hand[1]
    dealer_hand[1] = "_"
    dealer_total = dealer1
    if player_total == 21:
        print(f"Dealer's Hand:  {dealer_hand}")
        print(f"Dealer's Total: {dealer_total}")
        print(f"Player's Hand:  {player_hand}")
        print(f"Player's Total: {player_total}")
        print("Player has BlackJack, You Win!!!")
        choice = input("Would you like to continue? Press 'y' or 'n': ")
        if choice == "y":
          deal()  
        else:
            return
    player_turn()

def player_turn():
    print(f"Dealer's Hand:  {dealer_hand}")
    print(f"Dealer's Total: {dealer_total}")
    print(f"Player's Hand:  {player_hand}")
    print(f"Player's Total: {player_total}")
    choice = input("Would you like to Hit or Stand? Press 'h' or 's': ")
    if choice == 'h':
        player_hand += random.randint(0, len(cards)-1)
        player_total += player_hand[-1]
        if player_total > 23:
            if player_hand[0] == 11:
                player_hand[0] = 1
                player_total -= 10
            elif player_hand[1] == 11:
                player_hand[1] = 1
                player_total -= 10
            else:
                print(f"Dealer's Hand:  {dealer_hand}")
                print(f"Dealer's Total: {dealer_total}")
                print(f"Player's Hand:  {player_hand}")
                print(f"Player's Total: {player_total}")
                print("Player Busted!!!")
                choice = input("Would you like to continue? Press 'y' or 'n': ")
                if choice == "y":
                    deal()
                else:
                    return
        player_turn()
    dealer_turn()

def dealer_turn():
    dealer_hand[1] = dealer2
    dealer_total += dealer2
    print(f"Dealer's Hand:  {dealer_hand}")
    print(f"Dealer's Total: {dealer_total}")
    print(f"Player's Hand:  {player_hand}")
    print(f"Player's Total: {player_total}")

deal()