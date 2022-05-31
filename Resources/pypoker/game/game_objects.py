from  pypoker.game_items.default_objects import *

def get_split_pairs(hb_combined: str) -> dict:
    '''
    Takes a string of "face_value,"
    '''
    first_split = hb_combined.split(',')
    cards = dict()
    for i, c in enumerate(first_split):
        cur_key, cur_val = f'card{i}', c.split('_')
        cards[cur_key] = cur_val
    return cards

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
        hb_combined = f'{board},{self.get_hand()}'
        if self.get_hand() == '':
            return 0
        print(get_split_pairs(hb_combined))

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