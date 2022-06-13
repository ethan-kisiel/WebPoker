from pypoker.utilities.utils import HandScoringUtil as hsu
from pypoker.game_items.default_objects import Card, Deck

def test_scoring_methods():
    royal_flush = ['s_A', 's_K', 's_Q', 's_J', 's_10', 'd_7', 'd_5', 'd_K']
    for i in range(len(royal_flush)):
        curr_card = Card(0,0,royal_flush[i])
        royal_flush[i] = curr_card
        
    hsu.merge_sort(royal_flush)
    print()
        
    straight_flush = ['s_10', 's_9', 's_8', 's_7', 's_6', 's_5', 's_4']
    for i in range(len(straight_flush)):
        curr_card = Card(0,0,straight_flush[i])
        straight_flush[i] = curr_card

    print(hsu.score_straight_flush(straight_flush))
    assert hsu.score_royal_flush(royal_flush) == 1000
    
def test_five_high_straight():
    straight = ['s_2', 's_3', 's_4', 's_5', 's_A', 'd_7', 'd_K']
    for i in range(len(straight)):
        curr_card = Card(0,0,straight[i])
        straight[i] = curr_card
    
    print('straight?')
    print(hsu.is_straight(straight))

def test_oak():
    pair = ['s_2', 'd_2', 'd_A', 'c_K', 'c_10', 'd_8']
    three_oak = ['s_9', 'd_9', 'c_9', 'd_A', 'c_K', 'c_10', 'd_8']
    for i, card in enumerate(pair):
        pair[i] = Card(0,0, card)
    
    for i, card in enumerate(three_oak):
        three_oak[i] = Card(0,0,card)
    
    four_oak = ['d_A', 'd_10', 'd_9', 'c_10', 'h_10', 'c_A', 'h_A', 's_A']
    
    for i in range(len(four_oak)):
        curr_card = Card(0,0, four_oak[i])
        four_oak[i] = curr_card
    print(hsu.score_four_oak(four_oak))

    print(hsu.score_pair(pair))
    print(hsu.score_three_oak(three_oak))