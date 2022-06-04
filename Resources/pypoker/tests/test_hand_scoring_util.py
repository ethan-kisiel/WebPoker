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
        