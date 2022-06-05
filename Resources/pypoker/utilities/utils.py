from pypoker.game_items.default_objects import Card

class HandScoringUtil:
    
    # Sorting
    def merge_sort(array: list) -> None:
        if len(array) < 2:
            return
        
        midpoint = int(len(array) / 2)
        left = array[:midpoint]
        right = array[midpoint:]
        
        HandScoringUtil.merge_sort(left)
        HandScoringUtil.merge_sort(right)
        
        HandScoringUtil.merge(array, left, right)

    def merge(array: list, left: list, right: list) -> None:
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

    def sort_out_faces(array: list[Card]) -> dict:
        sorted_cards = {'c': [], 'd': [], 'h': [], 's': []}
        for card in array:
            sorted_cards[card.get_face()].append(card)

        return sorted_cards

    def walk_array(array: list[Card], size: int):
        '''
        Given an array, return sets of "size" cards
        starting from the last element backwards
        '''
        
        arrays = []
        length = len(array) - (size - 1)
        for i in range(length):
            start = (i+size) * -1
            stop = i * -1
            if i == 0:
                arrays.append(array[start:])
            else:
                arrays.append(array[start:stop])
                
        return arrays
                
    # Scoring
    def score_simple(card_score: int, tier: int) -> int:
        return ((card_score/13) * 100) + (tier * 100)
    
    def score_bidir(card_score: tuple[int,int], tier: int) -> int:
        smaller, larger = card_score
        return ((smaller/13) + (larger - 1)) + (tier * 100)

    def is_straight(array: list[Card]) -> int:
        '''
        Takes list[Card] with length of 5
        returns -1 if array does not represent
        a straight
        returns last element in array if
        it represents a straight
        '''
        values_range = array[-1] - array[0]

        if values_range == 4:
            if len(set(array)) == 5:
                return array[-1].get_points_value()

        return 0
    
    def is_flush(array: list[Card]) -> int:
        '''
        Takes an array of 5 Card(s)
        returns -1 if not flush, otherwise
        '''
        for card in array:
            if card.get_face() != array[0].get_face():
                return 0

        return array[-1].get_points_value()
    
    def score_royal_flush(array: list[Card]) -> int:
        HandScoringUtil.merge_sort(array)
        sep_array = HandScoringUtil.sort_out_faces(array)
        for face in sep_array.keys():
            array = sep_array[face]
            if len(array) >= 5:
                straight_score = HandScoringUtil.is_straight(array)
                if straight_score == 13:
                    return 1000
        return 0

    def score_straight_flush(array: list[Card]) -> int:
        HandScoringUtil.merge_sort(array)
        sep_array = HandScoringUtil.sort_out_faces(array)
        for face in sep_array.keys():
            array = sep_array[face]
            if len(array) >= 5:
                for array in HandScoringUtil.walk_array(array, 5):
                    straight_score = HandScoringUtil.is_straight(array)
                    if straight_score:
                        return HandScoringUtil.score_simple(straight_score, 8)
        return 0

    def score_four_oak(array: list[Card]) -> int:
        HandScoringUtil.merge_sort(array)
        searches = HandScoringUtil.walk_array(array, 4)

        for search in searches:
            if len(set(search)) == 1:
                score = search[0].get_points_value()
                return HandScoringUtil.score_simple(score, 7)
        return 0

    def score_full_house():
        # check for pair & 3 of a kind
        # return bidir(lowcard, highcard)
        pass