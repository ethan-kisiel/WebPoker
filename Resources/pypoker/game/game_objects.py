from bdb import Breakpoint
from  pypoker.game_items.default_objects import *

'''
def get_split_pairs(hb_combined: str) -> dict:
    '' '
    Takes a string of "face_value,"
    '' '
    first_split = hb_combined.split(',')
    cards = dict()
    for i, c in enumerate(first_split):
        cur_key, cur_val = f'card{i}', c.split('_')
        cards[cur_key] = cur_val
    return cards
'''

def merge_sort(array):
    if len(array) < 2:
        return
    
    midpoint = int(len(array) / 2)
    left = array[:midpoint]
    right = array[midpoint:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge(array, left, right)

def merge(array, left, right):
    i = 0
    while True:
        if len(left) + len(right) == 0:
            break
        try:
            if left[0] < right[0]:
                array[i] = left.pop(0)
            else:
                array[i] = right.pop(0)
        except:
            if len(left) == 0:
                array[i] = right.pop(0)
            else:
                array[i] = left.pop(0)
                
        i += 1

class Player:
    def __init__(self) -> None:
        self.__hand = (None, None)
        self.__chips = 0
        self.button = None

    def set_chips(self, chips: float) -> None:
        self.__chips = chips

    def set_hand(self, hand: tuple[Card] = None) -> None:
        if hand is None:
            self.__hand = (None, None)
        else:
            self.__hand = hand
            
    def set_button(self, button: str) -> None:
        # Create class for button?
        self.button = button
    
    def add_chips(self, chips: float) -> None:
        self.__chips += chips

    def place_bet(self, chips: float) -> None:
        self.__chips -= chips
    
    def get_chips(self) -> float:
        '''
        returns self.__chips
        for testing purposes
        '''
        return self.__chips
    
    def has_chips(self) -> bool:
        return self.__chips > 0

    def hand_value(self, board: Board) -> float:
        '''
        Calculates and returns value
        of hand paired with board
        '''
        hb_combined = board.get_board()
        hb_combined.append(self.__hand[0])
        hb_combined.append(self.__hand[1])
        for c in hb_combined:
            print(c)
        if self.get_hand() == '':
            return 0
        else:
            merge_sort(hb_combined)
        print('sorted: ')
        for c in hb_combined:
            print(c)
        return hb_combined
        #print(get_split_pairs(hb_combined))

    def get_hand(self) -> str:
        '''
        Returns string representation of
        current hand in compliance with "face_value," format
        '''
        if None in self.__hand:
            return ''
        return f'{self.__hand[0]},{self.__hand[1]}'

    def __repr__(self) -> str:
        hand = self.__hand
        rep = f'{self.__chips},({hand[0]};{hand[1]})'
        btn_rep = f'{rep},{self.button}'
        return btn_rep if self.button else rep


class Game:
    
    def __init__(self) -> None:
        self.__deck, self.board = Deck(), Board()  
    
    def reset(self) -> None:
        self.__deck.reset(), self.board.reset()