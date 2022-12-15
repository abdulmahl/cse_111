# Import random module 
# to use in this program
import random


def main():
    determ = get_determiner(1)
    noun = get_noun(1)
    tense = get_verb(0, "past")
    sentence = f"a. {determ.capitalize()} {noun} {tense}."
    print (sentence)

    determ = get_determiner(2)
    noun = get_noun(2)
    tense = get_verb(1, "present")
    sentence = f"b. {determ.capitalize()} {noun} {tense}."
    print (sentence)

    determ = get_determiner(1)
    noun = get_noun(1)
    tense = get_verb(0, "future")
    sentence = f"c. {determ.capitalize()} {noun} {tense}."
    print (sentence)
    
    determ = get_determiner(2)
    noun = get_noun(2)
    tense = get_verb(0, "past")
    sentence = f"d. {determ.capitalize()} {noun} {tense}."
    print (sentence)
    
    determ = get_determiner(1)
    noun = get_noun(1)
    tense = get_verb(2, "present")
    sentence = f"e. {determ.capitalize()} {noun} {tense}."
    print (sentence)

    determ = get_determiner(2)
    noun = get_noun(2)
    tense = get_verb(0, "future")
    sentence = f"f. {determ.capitalize()} {noun} {tense}"
    print(sentence)

    print()
    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(0, "past")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adverb()
    sentence = (f"a. {determ1.capitalize()} {noun1} {phrase} {determ1} {noun2} {tense} {phrase2} {phrase1} {determ1} {noun3}")
    print(sentence)

    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun0 = get_noun(0)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(2, "present")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adverb()
    phrase3 = get_adjective()
    sentence = (f"b. {determ1.capitalize()} {noun1} {phrase} {determ1} {noun2} {tense} {phrase2} {phrase1} {determ1} {noun3}")
    print(sentence)
    
    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun0 = get_noun(0)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(0, "future")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adjective()
    phrase3 = get_adverb()
    sentence = (f"c. {determ0.capitalize()} {noun0} {phrase} {determ1} {noun2} {tense} {phrase3} {phrase1} {determ1} {noun1}")
    print(sentence)
    
    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun0 = get_noun(0)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(0, "past")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adjective()
    phrase3 = get_adverb()
    sentence = (f"d. {determ1.capitalize()} {noun1} {phrase1} {determ1} {noun2} {tense} {phrase3} {phrase} {determ0} {noun0}")
    print(sentence)

    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun0 = get_noun(0)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(2, "present")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adjective()
    phrase3 = get_adverb()
    sentence = (f"e. {determ1.capitalize()} {noun1} {phrase1} {determ1} {noun3} {tense} {phrase3} {phrase} {determ0} {noun0}")
    print(sentence)
    
    determ0 = get_determiner(0)
    determ1 = get_determiner(1)
    noun0 = get_noun(0)
    noun1 = get_noun(1)
    noun2 = get_noun(1)
    noun3 = get_noun(1)
    tense = get_verb(0, "future")
    phrase = get_preposition()
    phrase1 = get_preposition()
    phrase2 = get_adjective()
    phrase3 = get_adverb()
    sentence = (f"f. {determ1.capitalize()} {noun1} {phrase} {determ1} {noun3} {tense} {phrase3} {phrase1} {determ0} {noun0}")
    print(sentence)
    print()



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        word = random.choice(words)
        return word

    elif tense == "present" and quantity == 1:
        words =   [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write" ]
        word = random.choice(words)
        return word

    elif tense == "present":
        words = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes" ]
        
        word = random.choice(words)
        return word

    else:
        if tense == "future":
            words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
            word = random.choice(words)
            return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition."""
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    quantity == 1
    words = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without", "a", "one", "the", "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    word = random.choice(words) 
    return word


def get_adverb():
    '''Return a randomly chosen adverb from this list
    of adverbs:
        "ferociously", "separately", "randomly", 
        "victoriously","painfully", 
        "successfully","speedily",
        "politely", "surprisingly", "boastfully",
        "officially", "suddenly", "eventually",
        "generously", "sympathetically"
        "slowly", "slowly", "violently", "monthly", "curiously"    

    Return randomly chosen adverb.'''
    words = ["ferociously", "separately", "randomly", 
        "victoriously","painfully", 
        "successfully","speedily",
        "politely", "surprisingly", "boastfully",
        "officially", "suddenly", "eventually",
        "generously", "sympathetically",
        "slowly", "slowly", "violently", "monthly", "curiously" ]

    word = random.choice(words)
    return word  
        

def get_adjective():
    '''Return a randomly chosen adjective from this 
    list of adjectives:
        "ashamed", "adorable", "attractive", "beautiful",  
        "aggressive", "cruel", "clever", "tasty", "jealous", 
        "breakable","homeless", "edible","nicer", "awful",
        "gorgeous", "meaningless", "sleeveless", 
        "different", "excellent", "international"
    
    
    Return a randomly chosen adjective.'''

    words = [ "ashamed", "adorable", "attractive", "beautiful",  
        "aggressive", "cruel", "clever", "tasty", "jealous",
        "breakable","homeless", "edible","nicer", "awful",
        "gorgeous", "meaningless", "sleeveless", 
        "different", "excellent", "international"]
    word = random.choice(words)
    return word    



if __name__ == "__main__":
    main()
