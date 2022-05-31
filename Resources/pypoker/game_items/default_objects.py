from random import randint as ri

FACES = ('c', 'd', 'h', 's')
VALUES = ( '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class Card:
    '''
    Playing card represented as "x_Y"
    where x = face, represented as the first letter
    of club, diamond, heart, spade and  Y = Value
    represented as a number value and capital first letter
    of Jack, Queen, King, Ace
    '''
    def __init__(self, face: int, value: int) -> None:
        try:
            self.__face = FACES[face]
            self.__value = VALUES[value]
        except:
            print("Could not instantiate Card")

    def sync(self, rep: str) -> None:
        '''
        Takes f_V representation of card
        sets self == to representation
        '''
        try:
            _ = rep.split('_')
            self.init(FACES.index(_[0], FACES.index(_[1])))

        except:
            print('Failed to sync')

    def __lt__(self, other) -> bool:
        if type(other) == Card:
            s_val, o_val = VALUES.index(self.__value), VALUES.index(other.get_value())
            return s_val < o_val
    
    def __le__(self, other) -> bool:
        if type(other) == Card:
            s_val, o_val = VALUES.index(self.__value), VALUES.index(other.get_value())
            return s_val <= o_val
    
    def __eq__(self, other) -> bool:
        if type(other) == Card:
            s_val, o_val = VALUES.index(self.__value), VALUES.index(other.get_value())
            return s_val == o_val
    
    def __gt__(self, other) -> bool:
        if type(other) == Card:
            s_val, o_val = VALUES.index(self.__value), VALUES.index(other.get_value())
            return s_val > o_val
    
    def __ge__(self, other) -> bool:
        if type(other) == Card:
            s_val, o_val = VALUES.index(self.__value), VALUES.index(other.get_value())
            return s_val >= o_val

    def get_value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return f'{self.__face}_{self.__value}'


class Deck:
    def __init__(self) -> None:
        self.__cards = []
        for f in range(len(FACES)):
            for v in range(len(VALUES)):
                self.__cards.append(Card(f, v))
                
    def get_cards(self) -> list:
        '''
        Returns array of string representations
        of self.__cards
        '''
        cards = []
        for card in self.__cards:
            cards.append(str(card) + ',')
        return cards
    
    def r_draw_card(self) -> Card:
        '''
        Removes and returns random card
        '''
        stop = len(self.__cards) -1
        return self.__cards.pop(ri(0, stop))
    
    def r_draw_cards(self, amount) -> list[Card]:
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
        (Debugging purposes only)
        '''
        try:
            return self.__cards.pop(index)
        except:
            return 0

    def reset(self) -> None:
        self.__init__()

    def __repr__(self) -> str:
        cards = ''
        cards.join(self.get_cards())
        return cards


class Board:
    def __init__(self) -> None:
        self.__board = {'flop': [None, None, None], 'turn': None, 'river': None}
        self.__phase = 0
        self.__pot = 0

    def incriment_phase(self) -> None:
        self.__phase += 1

    def draw_flop(self, deck: Deck) -> None:
        '''
        Burns a card from "deck" and
        sets flop to 3 random cards
        '''
        deck.r_draw_card()
        self.__board['flop'] = deck.r_draw_cards(3)

    def draw_turn(self, deck: Deck) -> None:
        deck.r_draw_card()
        self.__board['turn'] = deck.r_draw_card()

    def draw_river(self, deck: Deck) -> None:
        deck.r_draw_card()
        self.__board['river'] = deck.r_draw_card()

    def increase_pot(self, bet_size: float) -> None:
        self.__pot += bet_size

    def reset(self) -> None:
        self.__init__()

    def __str__(self) -> str:
        '''
        Returns string of "face_value," for every
        each game stage that is not None
        '''
        flop = self.__board['flop']
        card_one = flop[0]
        card_two = flop[1]
        card_three = flop[2]
        card_four = self.__board['turn']
        card_five = self.__board['river']

        if None in self.__board['flop']:
            return ''
        elif self.__board['turn'] is None:
            return f'{card_one},{card_two},{card_three}'
        elif self.__board['river'] is None:
            return f'{card_one},{card_two},{card_three},{card_four}'
        else:
            return f'{card_one},{card_two},{card_three},{card_four},{card_five}'