from pypoker.utilities.utils import HandScoringUtil as hsu
from pypoker.game_items.default_objects import Card, Deck

def test_pair():
    two_pair = ['s_2', 's_2', 's_Q', 's_J', 's_10', 'd_7', 'd_5', 'd_K']
    five_pair = ['s_5', 's_5', 's_Q', 's_J', 's_10', 'd_7', 'd_5', 'd_K']
    ace_pair = ['s_A', 'c_A', 's_Q', 's_J', 's_10', 'd_7', 'd_5', 'd_K']

    for i in range(len(two_pair)):
        two_pair[i] = Card(0,0,two_pair[i])
        five_pair[i] = Card(0,0,five_pair[i])
        ace_pair[i] = Card(0,0,ace_pair[i])

    two_score = hsu.score_pair(two_pair)
    five_score = hsu.score_pair(five_pair)
    ace_score = hsu.score_pair(ace_pair)

    scores_text = f'''
    TWO PAIR SCORE: {two_score};
    FIVE PAIR SCORE: {five_score};
    ACE PAIR SCORE: {ace_score}
    '''
    print(scores_text)

    assert(two_score < five_score)
    assert(five_score < ace_score)