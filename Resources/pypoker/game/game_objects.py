from pypoker.game_items.default_objects import Card, Deck, Board

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
    
    def __str__(self) -> str:
        hand = self.__hand
        rep = f'{self.__chips},({hand[0]};{hand[1]})'
        btn_rep = f'{rep},{self.button}'
        return btn_rep if self.button else rep