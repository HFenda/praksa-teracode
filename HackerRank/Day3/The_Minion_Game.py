
"""
Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Sample Input
BANANA

Sample Output
Stuart 12

"""

def minion_game(string):
    
    n = len(string)
    comb = ((n)*(n+1))/2
    kevinsCount = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    stuartsCount=int(comb-kevinsCount)

    if(stuartsCount>kevinsCount):
        print("Stuart "+str(stuartsCount))
    elif(stuartsCount<kevinsCount):
        print("Kevin "+str(kevinsCount))
    else:
        print("Draw")
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
