from classes import *
import sys


# Simply create a new class with these functions ----------------------------------------

def add_player(player_id, player_name):
    players[player_id] = Player(player_id, player_name)

def add_game(game_id, game_name):
    games[game_id] = Game(game_id, game_name)

def add_victory(game_id, victory_id, victory_name, victory_points):
    victory = Victory(victory_id, game_id, victory_name, victory_points)
    games[game_id].add_victory(victory_id, victory)

#----------------------------------------------------------------------------------------

# These functions establish relationships and add to the classes information through functions

def add_play(player_id, game_id, player_ign):
    players[player_id].add_play(game_id, player_ign)
    games[game_id].add_player(player_id)

def add_friends(player_id_1, player_id_2):
    players[player_id_1].add_friend(player_id_2)
    players[player_id_2].add_friend(player_id_1)

def win_victory(player_id, game_id, victory_id):
    players[player_id].add_victory(game_id, victory_id)
    games[game_id].victories[victory_id].add_player(player_id)
    games[game_id].victories[victory_id].times_accomplished += 1

#----------------------------------------------------------------------------------------

def friends_who_play(player_id, game_id):
    player = players[player_id]
    game = games[game_id]

    for friend_id in player.friends:
        if friend_id in game.players:
            print ("Hi") #will update this to have actual output later

def compare_players(player_id_1, player_id_2, game_id):
    player_1 = players[player_id_1]
    player_2 = players[player_id_2]


    player_1_victory_ids = player_1.get_victories(game_id)
    player_2_victory_ids = player_2.get_victories(game_id)

    for player_1_victory in player_1_victory_ids:
        print (games[game_id].victories[player_1_victory]) #will update this to have actual output later
    for player_2_victory in player_2_victory_ids:
        print (games[game_id].victories[player_2_victory]) #will update this to have actual output later

def summarize_player(player_id):
    player = players[player_id]
    for friend_id in player.friends:
        print(players[friend_id])
    
    for game_id in player.plays.keys():
        print(games[game_id])
    
    total_game_score = 0
    for game_id in player.victories.keys():
        game = games[game_id]
        game_score = player.get_game_score(game, game_id)
        total_game_score += game_score

    print(total_game_score) 

def summarize_game(game_id):
    game = games[game_id]
    for player_id in game.players:
        print(players[player_id])

    for victory_id in game.victories.keys():
        print(game.victories[victory_id])

def summarize_victory(game_id, victory_id):
    game = games[game_id]

    num_total_players = len(game.players)
    num_victories = game.victories[victory_id].times_accomplished

    for player_id in game.players:
        player = players[player_id]
        victories = player.get_victories(game_id)
        if victory_id in victories:
            print(player)
    
    print(num_total_players)
    print(num_victories)

def victory_ranking():
    ranking = {}
    for player in players.values():
        total_game_score = 0
        for game_id in player.victories.keys():
            game = games[game_id]
            game_score = player.get_game_score(game, game_id)
            total_game_score += game_score

        ranking[player.id] = total_game_score
    
    print(sorted(ranking.items(), key=lambda x:x[1]))



def main():
    players = {}
    games = {}

    for line in sys.stdin:
        line = line.strip().split(' ')
        if line[0] == '':
            print("Error")

        function_type = line[0]

        if function_type == 'AddPlayer':
            player_id = line[1]
            player_name = line[2].strip('"')
            add_player(player_id, player_name)
        elif function_type == 'AddGame':
            game_id = line[1]
            game_name = line[2].strip('"')
            add_game(game_id, game_name)
        elif function_type == 'AddVictory':
            game_id = line[1]
            victory_id = line[2]
            victory_name = line[3].strip('"')
            victory_points = line[4]
            add_victory(victory_id, game_id, victory_name, victory_points)
        elif function_type == 'Plays':
            player_id = line[1]
            game_id = line[2]
            player_ign = line[3].strip('"')
            add_play(player_id, game_id, player_ign)
        elif function_type == 'AddFriends':
            player_id_1 = line[1]
            player_id_2 = line[2]
            add_friends(player_id_1, player_id_2)
        elif function_type == 'WinVictory':
            player_id = line[1]
            game_id = line[2]
            victory_id = line[3]
            win_victory(player_id, game_id, victory_id)
        elif function_type == 'FriendsWhoPlay':
            player_id = line[1]
            game_id = line[2]
            friends_who_play(player_id, game_id)
        elif function_type == 'ComparePlayers':
            player_id_1 = line[1]
            player_id_2 = line[2]
            game_id = line[3]
            compare_players(player_id_1, player_id_2, game_id)
        elif function_type == 'SummarizePlayer':
            player_id = line[1]
            summarize_player(player_id)
        elif function_type == 'SummarizeGame':
            game_id = line[1]
            summarize_game(game_id)
        elif function_type == 'SummarizeVictory':
            game_id = line[1]
            victory_id = line[2]
            summarize_victory(game_id, victory_id)
        elif function_type == 'VictoryRanking':
            victory_ranking()
        else:
            print('Error')


if __name__ == "__main__":
    main()