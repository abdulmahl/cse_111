# Import modules from sentences.py program
# random module and pytest so that 
# they can be used in this program
import pytest

from sentences import (get_adjective, get_adverb, get_determiner, get_noun, get_preposition,
    get_prepositional_phrase, get_verb)


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):

        word = get_noun(1)

        assert word in single_noun

    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]   

    for _ in range(10):

        word = get_noun(2)

        assert word in plural_noun

def test_get_verb():

    past_tense = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote" ]

    for _ in range(18):

        word = get_verb(1, "past")

        assert word in past_tense

    present_tense =  [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes" ] 

    for _ in range(18):

        word = get_verb(0, "present")

        assert word in present_tense

    future_tense = [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]    

    for _ in range(18):

        word = get_verb(2, "future")

        assert word in future_tense

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(60):
        word = get_preposition()

        assert word in prepositions

def test_get_prepositional_phrase():
    prepositional_phrase = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without", "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman","a", "one", "the" ]

    for _ in range(60):
        word = get_prepositional_phrase(1)

        assert word in prepositional_phrase

def test_get_adverb():
    adverbs = [ "ferociously", "separately", "randomly", 
        "victoriously","painfully", 
        "successfully","speedily",
        "politely", "surprisingly", "boastfully",
        "officially", "suddenly", "eventually",
        "generously", "sympathetically",
        "slowly", "slowly", "violently", "monthly", "curiously" ]

    for _ in range(40):
        word = get_adverb()

        assert word in adverbs

def test_get_adjective():
    adjectives = [ "ashamed", "adorable", "attractive", "beautiful",  
        "aggressive", "cruel", "clever", "tasty", "jealous",
        "breakable","homeless", "edible","nicer", "awful",
        "gorgeous", "meaningless", "sleeveless", 
        "different", "excellent", "international"]

    for _ in range(40):
        word = get_adjective()

        assert word in adjectives

pytest.main(["-v", "--tb=line", "-rN", __file__])        
