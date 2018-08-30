import gamerecord
import shlex
import sys

def main():
    record = gamerecord.GameRecord()

    for line in sys.stdin:
        line = shlex.split(line)
        if len(line) == 0 or line[0] == '':
            continue

        function_type = line[0]

        if function_type == 'AddPlayer':
            player_id = int(line[1])
            player_name = line[2].strip('"')
            record.add_player(player_id, player_name)
        elif function_type == 'AddGame':
            game_id = int(line[1])
            game_name = line[2].strip('"')
            record.add_game(game_id, game_name)
        elif function_type == 'AddVictory':
            game_id = int(line[1])
            victory_id = int(line[2])
            victory_name = line[3].strip('"')
            victory_points = int(line[4])
            record.add_victory(victory_id, game_id, victory_name, victory_points)
        elif function_type == 'Plays':
            player_id = int(line[1])
            game_id = int(line[2])
            player_ign = line[3].strip('"')
            record.add_play(player_id, game_id, player_ign)
        elif function_type == 'AddFriends':
            player_id_1 = int(line[1])
            player_id_2 = int(line[2])
            record.add_friends(player_id_1, player_id_2)
        elif function_type == 'WinVictory':
            player_id = int(line[1])
            game_id = int(line[2])
            victory_id = int(line[3])
            record.win_victory(player_id, game_id, victory_id)
        elif function_type == 'FriendsWhoPlay':
            player_id = int(line[1])
            game_id = int(line[2])
            record.friends_who_play(player_id, game_id)
        elif function_type == 'ComparePlayers':
            player_id_1 = int(line[1])
            player_id_2 = int(line[2])
            game_id = int(line[3])
            record.compare_players(player_id_1, player_id_2, game_id)
        elif function_type == 'SummarizePlayer':
            player_id = int(line[1])
            record.summarize_player(player_id)
        elif function_type == 'SummarizeGame':
            game_id = int(line[1])
            record.summarize_game(game_id)
        elif function_type == 'SummarizeVictory':
            game_id = int(line[1])
            victory_id = int(line[2])
            record.summarize_victory(game_id, victory_id)
        elif function_type == 'VictoryRanking':
            record.victory_ranking()
        else:
            raise RuntimeError('You did not provide a valid function type as input')


if __name__ == "__main__":
    main()