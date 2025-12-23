Chapter two will base its learning on a prcatical example of sorting email from spam.

2.1 Variable

Apparently we need two variables for this problem:
1. Spam: a binary variable that is true/false depending on 
    whether the email is spam or not.
2. Words (mathematically: W0, W1, ... , Wn): a set of binary variables that are true/false depending on whether a specific word is present in the email or not.

2.2 Probability

Given that a variable, say email, can have only one value at a given time,
so the value of Spam is either true or false, and that sometimes we cannot know which one of these values it has, we use probabilities to express knowledge about the information. 
P([Spam == false]) = 0.25% means that there is a 0.25% chance that the email is not spam. Consequnetly, P([Spam == true]) = 0.75%

2.3 The normalization postulate

The implication from 2.2 when a variable is either true/false is that it forces the sum of probabilities to always add up to 1.

P([Spam == true]) + P([Spam == false]) = 1