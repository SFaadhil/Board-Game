import random

def grid(n):
    grid = []
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                grid.append((i + 1, j + 1))
        else:
            for j in range(n-1,-1,-1):
                grid.append((i+1,j+1))
    return grid


def players(nop):
    players = []
    for i in range(nop):
        players.append({"id" : i +1, 
                        "roll_history" : [], 
                        "position_history" : [0], 
                        "position_history_2D" : [0,0], 
                        "win_status" : 0})
    return players

def roll():
    return random.randint(1,6)

def move(player, players, droll, grid, n):
    curr_pos = player["position_history"][-1]
    new_pos = curr_pos + droll
    
    if new_pos >= len(grid):
        new_pos = len(grid) - 1

    for x in players:
        if x["id"] != player["id"] and x["position_history"][-1] == new_pos:
            print(f"\nPlayer {player['id']} killed Player {x['id']} at position {grid[new_pos]}\n")
            x["position_history"].append(0)
            x["position_history_2D"].append((0, 0))
    
    player["roll_history"].append(droll)
    player["position_history"].append(new_pos)
    player["position_history_2D"].append(grid[new_pos])

    if new_pos == len(grid) - 1:
        player["win_status"] = 1
        print(f"Player {player['id']} has won the game!\n")
        return True 
    return False


def summary(players):
    print("Game Summary: \n")
    for p in players:
        print(f"Player {p['id']}")
        print(f"Roll History: {p['roll_history']}")
        print(f"Position History: {p['position_history']}")
        print(f"Position History 2D: {p['position_history_2D']}")
        if p["win_status"] == 1:
            print("This player has won!\n")
        else:
            print("This player has lost\n")
        
def play(n,nop):
    grid_used = grid(n)
    players_playing = players(nop)
    winner = False
    turn = 0

    while winner == False:
        player = players_playing[turn]
        droll = roll()
        print(f"Player {player['id']} rolls a {droll} !")
        winner = move(player,players_playing,droll,grid_used,n)
        turn = (turn+1)%nop
    
    summary(players_playing)


n = int(input("Enter size of grid : "))
nop = int(input("Enter number of players : "))

print("Grid Layout : \n")

play(n,nop)




    
