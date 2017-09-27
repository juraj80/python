"""
https://en.wikipedia.org/wiki/Birthday_problem

In probability theory, the birthday problem or birthday paradox concerns
the probability that, in a set of n randomly chosen people, some pair of
them will have the same birthday. By the pigeonhole principle, the probability
reaches 100% when the number of people reaches 367 (since there are only 366
possible birthdays, including February 29). However, 99.9% probability is reached
with just 70 people, and 50% probability with 23 people. These conclusions are based
on the assumption that each day of the year (except February 29) is equally probable
for a birthday.
"""


from random import randint

def random_birthday(num):
    """Returns sequence of randomly generated lists of lists [day,month].
    num: number of birthdays
    returns: list of lists
    """
    result=[]
    for i in range(0,num):
        day = randint(1,31)
        month = randint(1,12)
        result.append([day,month])
    return result        


def check_birthday(t):
    """Returns True if any element appears more then once in a sequence.
    t: list
    returns: bool
    """
    result = []
    for i in t:
       if i in result:
            return True
       else:
            result.append(i)
    return False


def runSimulation(num_of_trials,num_of_people):
    """Generates a sample of birthdays and counts duplicates.
    num_of_people: how many students in the group
    num_of_trials: how many trials to simulate
    returns: probability of matches

    """
    count=0
    for trial in range(0,num_of_trials):
        birthdays=random_birthday(num_of_people)
        if check_birthday(birthdays):
            count+=1
    return count/num_of_trials * 100
    

if __name__ == '__main__':
    num_of_trials = 1000
    num_of_people = 23
    probability = runSimulation(num_of_trials,num_of_people)
    print('After %d simulations' % num_of_trials)
    print('with %d students' % num_of_people)
    print('there were %d percent probability' % probability)
    print('that two or more students have the same birthday.')
    
    
