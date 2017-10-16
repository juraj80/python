'''An effective algorithm to choose random word from histogram
1. Use keys to get a list of the words from histogram
2. Build a list that contains the cumulative sum of the word frequencies.
   The last item in the list is the total number of words in the dictionary, n.
3. Choose a random number from 1 to n. Use a bisection search to find the index
   where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.
'''
import random
from bisect import bisect

def random_word(hist):
    words = []
    freqs = []
    total_freq = 0
    for word,freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    x = random.randint(0,total_freq-1)
    
    #use bisection to returns an insertion point which comes after (to the right of) any existing entries of x in a.
    index = bisect(freqs,x) 
    return words[index]


def main():
    hist = hist = {'i': 3191,
        'in': 2188,
        'was': 2400,
        'be': 1976,
        'that': 1800,
        'as': 1437,
        'she': 2364,
        'a': 3130,
        'for': 1347,
        'her': 2483,
        'it': 2529,
        'had': 1626,
        'to': 5242,
        'and': 4897,
        'of': 4295,
        'he': 1811,
        'the': 5205,
        'not': 2151,
        'you': 1999,
        'but': 1441}


    print"\n\nHere are some random words from the hist"
    for i in range(5):
        print random_word(hist)


if __name__ == '__main__':
    main()
