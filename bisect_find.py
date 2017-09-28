import bisect

def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list,word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    """
    if len(word_list)==0:
        return False
    m = len(word_list)/2
    if word == word_list[m]:
        return True
    elif word < word_list[m]:
        return in_bisect(word_list[:m],word)
    elif word > word_list[m]:
        return in_bisect(word_list[m+1:],word)


def in_bisect_cheat(word_list,word):
    i = bisect.bisect_left(word_list,word) # returns location point of word in word_list
    if i == len(word_list): # handles empty list when i == 0
       return False
    return word_list[i] == word

    
if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print word, 'in list', in_bisect(word_list,word)

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print word, 'in list', in_bisect_cheat(word_list,word)


