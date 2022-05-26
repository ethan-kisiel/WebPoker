from random import randint as ri
FACES = ('c', 'd', 'h', 's')
VALUES = ( '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class Card:
    def __init__(self, face: int, value: int):
        self.__face = FACES[face]
        self.__value = VALUES[value]

    def __str__(self):
        return f'{self.__face}_{self.__value}'
    
    def __repr__(self):
        return f'{self.__face}_{self.__value}'
    
class Deck:
    def __init__(self):
        self.__cards = []
        for f in range(len(FACES)):
            for v in range(len(VALUES)):
                self.__cards.append(Card(f, v))
                
    def get_cards(self):
        '''
        Returns array of string representations
        of self.__cards
        '''
        cards = []
        for card in self.__cards:
            cards.append(str(card))
        return cards
    
    def r_draw_card(self) -> Card:
        '''
        Removes and returns random card
        '''
        stop = len(self.__cards) -1
        return self.__cards.pop(ri(0, stop))
    
    def r_draw_cards(self, amount) -> Card:
        '''
        Draws and removes amount
        number of random cards
        '''
        
        cards = []
        for _ in range(amount):
            stop = len(self.__cards) -1
            card = self.__cards.pop(ri(0, stop))
            cards.append(card)

        return cards
    
    def draw_card(self, index: int) -> Card:
        '''
        Removes and returns card at designated index;
        if error, returns 0
        '''
        try:
            return self.__cards.pop(index)
        except:
            return 0

    def draw_cards(self, index: int, amount: int) -> list:
        '''
        Removes and returns list of cards starting at index,
        ending with index + amount (inclusively)
        '''
        return
    
    def reset(self):
        self.__init__(self)
        
    def __repr__(self):
        cards = ''
        cards.join(self.get_cards())
        return cards