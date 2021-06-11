import random
import collections

# Given lists
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

# creating a deck using ZIP
list(zip(vals*4, sorted(suits*13)))

# creating a deck using MAP & LAMBDA
list (map(lambda x,y: (x,y), sorted([x for x in suits]*13), [y for y in vals]*4  ))

# creating a deck using LIST COMPREHENSION
[(s,v) for s in suits for v in vals]







# creating a deck using a function without use of map, lambda, zip, list comprehension
def deck_cards(suits, vals):
    
    # Validations

    # check if suits are ok
    if len(suits) != 4:
        raise ValueError("there should be a total of 4 suits")
    for suit in suits:
        if suit not in [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]:
            raise ValueError("suit should be one of these: spades , clubs , hearts , diamonds")


    # check if vals are ok
    if len(vals) != 13:
        raise ValueError("there should be a total of 13 vals")
    for val in vals:
        if val not in [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]:
            raise ValueError("val should be one of the value defined in 'vals' list above")

    deck = []
    for s in suits:
        for v in vals:
            deck.append((s,v))
    return deck







def draw_two_hands(deck, cards_in_hand):
    
    # random sample cards for two players based on hand_size
    both_hands = random.sample(deck, cards_in_hand*2)
    
    # return the cards for the two hands
    return both_hands







def modify_hand(hand):
    modified_hand = []
    for x,y in hand:
        if y == 'jack':
            y = 11
        elif y == 'queen':
            y = 12
        elif y == 'king':
            y = 13
        elif y == 'ace':
            y = 14
        else:
            y = int(y)
        modified_hand.append((x,y))
    
    # modified hand has all numbers instead of jack/queen/king/ace
    return modified_hand







def find_hand_type(modified_hand, val_int, cards_in_hand):
    
    # sorted hand to manipulate values in hand
    sorted_modified_hand = sorted([y for x,y in modified_hand])
    
    # do we have same suit in all cards
    if len(set([x for x,y in modified_hand])) == 1:
        
        # if its a royal-flush, the sum should be 14+13+12+11+10
        if sum([int(y) for x,y in modified_hand]) == sum(val_int[-cards_in_hand:]):
            return "royal_flush"        
        # if its a straight-flush, the sum of difference between the sorted values should be "total elements - 1"
        elif sum([sorted_modified_hand[i+1] - sorted_modified_hand[i] for i in range(len(sorted_modified_hand)-1)]) == (len(sorted_modified_hand)-1):
            return "straight_flush"
        else:
            return "flush"
    
    # find the count of occurances of different values
    occurrences = collections.Counter([y for x,y in modified_hand])
    # how many distinct values exist
    unq_values = len(occurrences)
    # count of most common values - list of types
    most_common_counts = occurrences.most_common(unq_values)
    
    # first most common count
    first_most_common = most_common_counts[0][1]    
    # second most common count if it exists
    if unq_values > 1:
        second_most_common = most_common_counts[1][1]
    
    if cards_in_hand == 5 and first_most_common == 3 and second_most_common == 2:
        return "full_house"
    
    # check for "4 of a kind"
    if cards_in_hand in [4,5] and first_most_common == 4:
        return "four_of_a_kind"
    
    # check for "3 of a kind"
    if first_most_common == 3:
        return "three_of_a_kind"
    
    # check for 2 pairs
    if cards_in_hand in [4,5] and first_most_common == 2 and second_most_common == 2:
        return "two_pair"

    # check for straight, i.e., unq suits are more than 1
    if ( len(set([x for x,y in modified_hand])) > 1 ) and ( sum([sorted_modified_hand[i+1] - sorted_modified_hand[i] for i in range(len(sorted_modified_hand)-1)]) == (len(sorted_modified_hand)-1) ):
        return "straight"
    
    # check for 1 pair
    if first_most_common == 2:
        return "one_pair"
    else:
        return "high_card"







def find_winner(hand_type, modified_hand_1, type_1, modified_hand_2, type_2):
    
    if type_1 != type_2:
        if hand_type[type_1] > hand_type[type_2]:
            return modified_hand_1
        else:
            return modified_hand_2
    else:
        if type_1 in ['royal_flush','straight_flush', 'flush', 'straight']:
            return modified_hand_2 if sum([y for x,y in modified_hand_1]) > sum([y for x,y in modified_hand_2]) else modified_hand_2
        elif type_1 in ['four_of_a_kind','three_of_a_kind']:
            list_1 = [y for x,y in modified_hand_1]
            list_2 = [y for x,y in modified_hand_2]
            return modified_hand_1 if max(set(list_1), key = list_1.count) > max(set(list_2), key = list_2.count) else modified_hand_2
        elif type_1 == 'full_house':
            return modified_hand_1 if sum(set([y for x,y in modified_hand_1])) > sum(set([y for x,y in modified_hand_2])) else modified_hand_2
        elif type_1 in ["two_pair", "one_pair"]:
            list_1 = [y for x,y in modified_hand_1]
            set_1 = set(list_1)
            list_2 = [y for x,y in modified_hand_2]
            set_2 = set(list_2)
            return modified_hand_1 if sum([x for x in set_1 if list_1.count(x)==2]) > sum([x for x in set_2 if list_2.count(x)==2]) else modified_hand_2
        elif type_1 == "high_card":
            return modified_hand_1 if max([y for x,y in modified_hand_1]) > max([y for x,y in modified_hand_2]) else modified_hand_2







def play_poker(first_hand, second_hand):
    
    vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

    val_int = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    hand_type = {"royal_flush":10, "straight_flush":9, "four_of_a_kind":8, "full_house":7, "flush":6, "straight":5, "three_of_a_kind":4, "two_pair":3, "one_pair":2, "high_card":1}
    
    # find the number of cards in each hand
    cards_in_hand = len(first_hand)

    # Validations

    # cards_in_hand should be between 3 and 5
    if not (3 <= cards_in_hand <= 5):
        raise ValueError("number of cards in one hand should be between 3 and 5")

    # Values of suits should be among the allowed values
    for suit, val in first_hand:
        if suit not in [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]:
            raise ValueError("suit should be one of these: spades , clubs , hearts , diamonds")
    for suit, val in second_hand:
        if suit not in [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]:
            raise ValueError("suit should be one of these: spades , clubs , hearts , diamonds")

    # check if vals are among the allowed values
    for suit, val in first_hand:
        if val not in [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]:
            raise ValueError("val should be one of the value defined in 'vals' list above")
    for suit, val in second_hand:
        if val not in [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]:
            raise ValueError("val should be one of the value defined in 'vals' list above")




    # get the modified hands for the input hands
    modified_hand_1 = modify_hand(first_hand)
    modified_hand_2 = modify_hand(second_hand)

    # find the type of each hand
    type_1 = find_hand_type(modified_hand_1, val_int, cards_in_hand)
    type_2 = find_hand_type(modified_hand_2, val_int, cards_in_hand)

    # find the winner hand
    winner_hand = find_winner(hand_type, modified_hand_1, type_1, modified_hand_2, type_2)

    # return the original winner hand
    return [type_1, first_hand] if winner_hand == modified_hand_1 else [type_2, second_hand]
