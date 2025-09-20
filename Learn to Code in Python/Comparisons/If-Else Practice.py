"""
Assignment
Complete the check_high_score function. 
If the player_name matches the high score name, return the string:
high
Otherwise, if it's the low scorer, return the string:
low
Otherwise, return the string:
neither
"""

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
