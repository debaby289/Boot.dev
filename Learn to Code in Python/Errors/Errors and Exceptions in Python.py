"""
Assignment
One of the calls to get_player_record is raising a player id not found exception. Change the code in the main function to safely make all four calls within one try-except block. If an exception is raised, print the exception instead.
"""

def main():
    print(get_player_record(1))
    print(get_player_record(2))
    print(get_player_record(3))
    
    try:
        print(get_player_record(4))
    except Exception:
      print("player id not found")


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")

