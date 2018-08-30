class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.plays = {}
        self.friends = []
        self.victories = {}

    def add_play(self, game_id, player_ign):
        self.plays[game_id] = player_ign
    
    def add_friend(self, friend_id):
        self.friends.append(friend_id)
    
    def add_victory(self, game_id, victory_id):
        if game_id not in self.victories.keys():
            self.victories[game_id] = [victory_id]
        else:
            self.victories[game_id].append(victory_id)

    def get_victories(self, game_id):
        if game_id not in self.victories.keys():
            return []
        else:
            return self.victories[game_id]
    
    def get_score(self, game, game_id):
        game_score = 0
        for victory_id in self.get_victories(game_id):
            game_score += game.victories[victory_id].points

        return game_score

class Game:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.players = []
        self.victories = {}
    
    def add_player(self, player_id):
        self.players.append(player_id)
    
    def add_victory(self, victory_id, victory):
        self.victories[victory_id] = victory
    
class Victory:
    def __init__(self, victory_id, game_id, name, points):
        self.victory_id = victory_id
        self.game_id = game_id
        self.name = name
        self.points = points
        self.times_accomplished = 0
        self.players = []
    
    def add_player(self, player_id):
        self.players.append(player_id)
