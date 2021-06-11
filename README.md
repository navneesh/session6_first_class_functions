# Purpose of this project
This project contains the functions to decide the winner of a poker game. Following functions are defined

# deck_cards
This function is used to create a deck of cards when it is passed with two input parameters. List of 4 suits and list of 13 values.

'''python
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
'''

# draw_two_hands
This functions draws two random hands from the deck of cards passed an input.
The number of cards per hand" can be passed a parameter.

# modify_hand
This function is used to convert the non-numerical values (ace/queen/jack/king) of the input-hand into numerical values for ease in calculation.


# find_hand_type
This function , when passed with a modified_hand, return the type of the hand. There are 10 predefined types:

'''python
hand_type = {"royal_flush":10, "straight_flush":9, "four_of_a_kind":8, "full_house":7, "flush":6, "straight":5, "three_of_a_kind":4, "two_pair":3, "one_pair":2, "high_card":1}
'''

# find_winner
This function, when passed with two input hands, decides the winner based on the following rules:
a. If hand_type of both hnds are unequal, we decide the winner without looking into the values of the hand,
b. If, however, the hand-types are equal, then we check the values to determine the winner.
Example: if we have two hands with "straight flush", then we decide the winner by taking the sum of values of both the hands.
         The hand with the sequence of bigger number wins.

# play_poker
Ths is the wrapper function which is the interface for the game.
This takes two hands as output and utilizes the above mentioned functions to define a winner.         
