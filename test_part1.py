import pytest
import random
import string
import os
import inspect
import re
import math
import time
import part1
from part1 import deck_cards
from part1 import play_poker


####################################################### Validations for deck_cards()######################################

def test_session6_deck_cards_reqd_positional():
    """Test squared_power function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        part1.deck_cards()

def test_session6_deck_cards_extra_positional():
    """Test squared_power function for extra positional arguments"""
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    vals =  [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    extra = suits
    with pytest.raises(TypeError, match=r".*takes 2 positional arguments but 3 were given*"):
        part1.deck_cards(suits, vals, extra)

def test_session6_deck_cards_invalid_suit():
    """Test squared_power function for extra positional arguments"""
    suits = [ 'spades' , 'tiger' , 'lion' , 'cheetah' ]
    vals =  [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    with pytest.raises(ValueError, match=r".*suit should be one of these: spades , clubs , hearts , diamonds*"):
        part1.deck_cards(suits, vals)

def test_session6_deck_cards_less_suit():
    """Test squared_power function for extra positional arguments"""
    suits = [ 'spades' , 'clubs' , 'hearts' ]
    vals =  [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    with pytest.raises(ValueError, match=r".*there should be a total of 4 suits*"):
        part1.deck_cards(suits, vals)

def test_session6_deck_cards_invalid_vals():
    """Test squared_power function for extra positional arguments"""
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    vals =  [ 'navneesh' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    with pytest.raises(ValueError, match=r".*val should be one of the value defined in 'vals' list above*"):
        part1.deck_cards(suits, vals)

def test_session6_deck_cards_less_val():
    """Test squared_power function for extra positional arguments"""
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    vals =  [ '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    with pytest.raises(ValueError, match=r".*there should be a total of 13 vals*"):
        part1.deck_cards(suits, vals)

def test_session6_deck_cards_output():
    """Test squared_power_list function for output with multiple inputs"""
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    vals =  [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    assert sorted(part1.deck_cards(suits, vals)) == sorted([(s,v) for s in suits for v in vals]), "function def_cards is not returning correct output"











####################################################### Validations for play_poker()######################################

def test_session6_play_poker_no_args():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        part1.play_poker()


def test_session6_play_poker_cards_in_hand_limit():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('hearts', 'king')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*number of cards in one hand should be between 3 and 5*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_play_poker_cards_incorrect_suit():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('SALESFORCE', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*suit should be one of these: spades , clubs , hearts , diamonds*"):
        part1.play_poker(first_hand, second_hand)


def test_session6_play_poker_cards_incorrect_vals():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'SRIGANGANAGAR'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    with pytest.raises(ValueError, match=r".*val should be one of the value defined in 'vals' list above*"):
        part1.play_poker(first_hand, second_hand)



def test_session6_play_poker_cards_output_one_pair():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('hearts', 'king'), ('diamonds', '10'), ('diamonds', '7'), ('diamonds', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'one_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


def test_session6_play_poker_cards_output_royal_flush():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


def test_session6_play_poker_cards_output_straight_flush():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('spades', 'king'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'straight_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"



def test_session6_play_poker_cards_output_flush():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('spades', '2'), ('spades', '10'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"


def test_session6_play_poker_cards_output_four_of_a_kind():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '9'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'four_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


def test_session6_play_poker_cards_output_full_house():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', 'queen'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'full_house', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


def test_session6_play_poker_cards_output_3_of_a_kind():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '5'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"        


def test_session6_play_poker_cards_output_2_pairs():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '8'), ('hearts', 'queen'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'two_pair', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"            


def test_session6_play_poker_cards_output_high_card():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7'), ('hearts', 'queen'), ('spades', 'ace')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5'), ('clubs', '2')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"            


def test_session6_play_poker_cards_output_high_card_4_cards():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7'), ('hearts', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


def test_session6_play_poker_cards_output_high_card_3_cards():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '2'), ('diamonds', '7')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'high_card', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"        


def test_session6_play_poker_cards_output_royal_flush_4_cards():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', 'jack'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '7')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"    


def test_session6_play_poker_cards_output_royal_flush_3_cards():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', 'ace'), ('spades', 'king'), ('spades', 'queen')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'royal_flush', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"       


def test_session6_play_poker_cards_output_3_of_a_kind_4_cards():
    """Test squared_power function for extra positional arguments"""
    first_hand = [('spades', '9'), ('clubs', '9'), ('diamonds', '9'), ('hearts', '5')]
    second_hand = [('hearts', '4'), ('spades', '7'), ('spades', '8'), ('clubs', '5')]
    assert part1.play_poker(first_hand, second_hand)[0] == 'three_of_a_kind', "winner hand type is not correct"
    assert part1.play_poker(first_hand, second_hand)[1] == first_hand, "winner hand values are not correct"        