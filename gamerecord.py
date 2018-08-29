from prettytable import PrettyTable
from helper import *

class GameRecord:
    def __init__(self):
        self.players = {}
        self.games = {}

    def get_gamer_score(self, player):
        total_score = 0

        for game_id in player.plays.keys():
            game = games[game_id]
            total_score += player.get_score(game, game_id)
        return total_score
            
    # These functions add items to the record and create new classes

    def add_player(self, player_id, player_name):
        self.players[player_id] = Player(player_id, player_name)
    
    def add_game(self, game_id, game_name):
        self.games[game_id] = Game(game_id, game_name)
    
    def add_victory(self, victory_id, game_id, victory_name, victory_points):
        victory = Victory(victory_id, game_id, victory_name, victory_points)
        self.games[game_id].add_victory(victory_id, victory)

    #----------------------------------------------------------------------------------------

    # These functions establish relationships and add to the classes information through functions

    def add_play(self, player_id, game_id, player_ign):
        self.players[player_id].add_play(game_id, player_ign)
        self.games[game_id].add_player(player_id)

    def add_friends(self, player_id_1, player_id_2):
        self.players[player_id_1].add_friend(player_id_2)
        self.players[player_id_2].add_friend(player_id_1)

    def win_victory(self, player_id, game_id, victory_id):
        self.players[player_id].add_victory(game_id, victory_id)
        self.games[game_id].victories[victory_id].add_player(player_id)
        self.games[game_id].victories[victory_id].times_accomplished += 1

    #----------------------------------------------------------------------------------------

    def friends_who_play(self, player_id, game_id):
        player = self.players[player_id]
        game = self.games[game_id]

        for friend_id in player.friends:
            if friend_id in game.self.players:
                print ("Hi") #will update this to have actual output later

    def compare_players(self, player_id_1, player_id_2, game_id):
        player_1 = self.players[player_id_1]
        player_2 = self.players[player_id_2]


        player_1_victory_ids = player_1.get_victories(game_id)
        player_2_victory_ids = player_2.get_victories(game_id)

        for player_1_victory in player_1_victory_ids:
            print (self.games[game_id].victories[player_1_victory]) #will update this to have actual output later
        for player_2_victory in player_2_victory_ids:
            print (self.games[game_id].victories[player_2_victory]) #will update this to have actual output later

    def summarize_player(self, player_id):
        player = self.players[player_id]
        print()
        print("Player: " + player.name)
        print("Total Gamescore: " + str(self.get_gamer_score(player)))
        print()

        pt = PrettyTable()
        pt.field_names = ["Friend", "Gamerscore"]
        for friend_id in player.friends:
            friend = self.players[friend_id]
            pt.add_row([friend.name, friend.get_])
        print(pt)
        
        pt = PrettyTable()
        pt.field_names = ["Game", "Victories", "Gamerscore", "IGN"]
        for game_id in player.plays.keys():
            game = self.games[game_id]
            pt.add_row([game.name, 20, player.get_score(game, game_id), player.plays[game_id]])
        print(pt)
        
        total_game_score = 0
        for game_id in player.victories.keys():
            game = self.games[game_id]
            game_score = player.get_score(game, game_id)
            total_game_score += game_score

    def summarize_game(self, game_id):
        game = self.games[game_id]
        for player_id in game.self.players:
            print(self.players[player_id])

        for victory_id in game.victories.keys():
            print(game.victories[victory_id])

    def summarize_victory(self, game_id, victory_id):
        game = self.games[game_id]

        num_total_self.players = len(game.self.players)
        num_victories = game.victories[victory_id].times_accomplished

        for player_id in game.self.players:
            player = self.players[player_id]
            victories = player.get_victories(game_id)
            if victory_id in victories:
                print(player)
        
        print(num_total_self.players)
        print(num_victories)

    def victory_ranking(self):
        ranking = {}
        for player in self.players.values():
            total_game_score = 0
            for game_id in player.victories.keys():
                game = self.games[game_id]
                game_score = player.get_score(game, game_id)
                total_game_score += game_score

            ranking[player.id] = total_game_score
        
        print(sorted(ranking.items(), key=lambda x:x[1]))
