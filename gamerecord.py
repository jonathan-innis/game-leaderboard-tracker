from prettytable import PrettyTable
import helper

class GameRecord:
    """Records of all of the gaming relationships
    
    Contains all of the information surrounding storing the players, games, victories
    and the relationships between them (friendships, wins, etc.). 

    Attributes:
        players: A dictionary formatted as {player_id : Player()} containing all of the players on record
        games: A dictionary formatted as {game_id: Game()} containing all of the games on the record
    """

    def __init__(self):
        """Inits GameRecord with no players and no games"""
        self.players = {}
        self.games = {}
            
    # These functions add items to the record and create new classes

    def add_player(self, player_id, player_name):
        """Adds player to the players dictionary"""

        self.players[player_id] = helper.Player(player_id, player_name)
    
    def add_game(self, game_id, game_name):
        """Adds game to the games dictionary"""

        self.games[game_id] = helper.Game(game_id, game_name)
    
    def add_victory(self, victory_id, game_id, victory_name, victory_points):
        """Adds victory to the victory dictionary inside of the game object"""

        victory = helper.Victory(victory_id, game_id, victory_name, victory_points)
        self.games[game_id].add_victory(victory_id, victory)

    #----------------------------------------------------------------------------------------

    # These functions establish relationships and add to the classes information through functions

    def add_play(self, player_id, game_id, player_ign):
        """Adds the game and gamertag to the plays dictionary while also 
        adding the player_id to the list of players that play the game"""

        self.players[player_id].add_play(game_id, player_ign)
        self.games[game_id].add_player(player_id)

    def add_friends(self, player_id_1, player_id_2):
        """Adds the player_id of each player to the other player's friends list"""

        self.players[player_id_1].add_friend(player_id_2)
        self.players[player_id_2].add_friend(player_id_1)

    def win_victory(self, player_id, game_id, victory_id):
        """Adds the victory to the specified game to the player's victory dictionary, 
        adds the player_id to the list of players who achieved the victory, and increasing
        the number of times that victory was accomplished"""
        victory = self.games[game_id].victories[victory_id]

        self.players[player_id].add_victory(game_id, victory_id, victory.score)
        self.games[game_id].victories[victory_id].add_player(player_id)
        self.games[game_id].victories[victory_id].times_accomplished += 1

    #----------------------------------------------------------------------------------------

    def friends_who_play(self, player_id, game_id):
        """Creates a report showing which player's friends play the game given with the game_id"""

        player = self.players[player_id]
        game = self.games[game_id]

        print()
        print("Player: " + player.name)
        print("Game: " + game.name)
        print()

        pt = PrettyTable()
        pt.field_names = ["Friend", "Gamerscore"]

        #Checks if the friend in the list of friends has played the given game
        for friend_id in player.friends:
            if friend_id in game.self.players:
                friend = self.players[friend_id]
                pt.add_row([friend.name, friend.gamerscore])
        
        print(pt)

    #TODO finish this function!!!
    def compare_players(self, player_id_1, player_id_2, game_id):
        """Creates a report comparing player 1 and player 2's Victory 
        records and total Victory scores for the given game"""

        game = self.games[game_id]
        player_1 = self.players[player_id_1]
        player_2 = self.players[player_id_2]


        player_1_victory_ids = player_1.get_victories(game_id)
        player_2_victory_ids = player_2.get_victories(game_id)

        print()
        print("Game: " + game.name)
        print()

        #Player Comparison Table
        pt = PrettyTable()
        pt.field_names = ["Player", "Victory Record", "Total Points"]

        victory_percentage = str(len(player_1_victory_ids)) + "/" + str(len(game.victories.keys())) 
        pt.add_row([player_1.name, victory_percentage, player_1.get_score(game_id)])
        victory_percentage = str(len(player_2_victory_ids)) + "/" + str(len(game.victories.keys()))
        pt.add_row([player_2.name, victory_percentage, player_2.get_score(game_id)])

        print(pt)

    def summarize_player(self, player_id):
        """Creates a report of all of player's friends, games the
         player plays, and gamer point totals."""

        player = self.players[player_id]

        print()
        print("Player: " + player.name)
        print("Total Gamescore: " + str(player.gamerscore))
        print()

        #Friend Table
        pt = PrettyTable()
        pt.field_names = ["Friend", "Gamerscore"]

        for friend_id in player.friends:
            friend = self.players[friend_id]
            pt.add_row([friend.name, player.gamerscore])
        print(pt)
        
        #Games Table
        pt = PrettyTable()
        pt.field_names = ["Game", "Victories", "Gamerscore", "IGN"]

        for game_id in player.plays.keys():
            game = self.games[game_id]
            victory_percentage = str(len(player.get_victories(game_id))) + "/" + str(len(game.victories.keys()))
            pt.add_row([game.name, victory_percentage, player.get_score(game_id), player.plays[game_id]])
        print(pt)

    def summarize_game(self, game_id):
        """Creates a report of all players who play the specified game and the 
        number of times each of its victories have been accomplished"""

        game = self.games[game_id]

        #Player Table
        pt = PrettyTable()
        pt.field_names = ["Player", "Gamerscore", "IGN"]
        for player_id in game.players:
            player = self.players[player_id]
            pt.add_row([player.name, player.gamerscore, player.plays[game_id]])
        
        print(pt)

        #Victory Table
        pt = PrettyTable()
        pt.field_names = ["Victory", "Times Accomplished", "Points"]
        for victory_id in game.victories.keys():
            victory = game.victories[victory_id]
            pt.add_row([victory.name, victory.times_accomplished, victory.points])
        
        print(pt)
            

    def summarize_victory(self, game_id, victory_id):
        """Creates a report of all players who have achieved a Victory, and the 
        percentage of players who play that game who have the Victory"""

        game = self.games[game_id]

        num_total_players = len(game.players)
        num_victories = game.victories[victory_id].times_accomplished

        #Player Table
        pt = PrettyTable()
        pt.field_names = ["Player", "Gamerscore", "IGN"]

        #Goes through players who play the game and checks if the player has achieved the victory given 
        for player_id in game.players:
            player = self.players[player_id]
            victories = player.get_victories(game_id)
            if victory_id in victories:
                pt.add_row([player.name, player.gamerscore, player.plays[game_id]])
        print(pt)
        
        print("Victory Achieved: " + num_victories + "/" + num_total_players)

    def victory_ranking(self):
        """Creates a report showing the summary ranking all players by their total number of gamer points"""

        ranking = {}

        pt = PrettyTable()
        pt.field_names = ["Player", "Gamerscore"]

        #Gets the gamerscore for each player and orders them based on highest to lowest gamerscore
        for player_id in self.players.values():
            player = self.players[player_id]
            ranking[player.id] = player.gamerscore
        
        #Returns a descending sorted list of tuples by gamerscore in the format (player_id, gamerscore)
        sorted_ranking = sorted(ranking.items(), key=lambda x:x[1], reverse=True)

        for rank in sorted_ranking:
            player = self.players[rank[0]]
            pt.add_row([player.name, rank[1]])
        
        print(pt)

