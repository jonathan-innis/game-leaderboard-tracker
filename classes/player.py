class Player:
    """A record of a player, the games they play, friends, etc.
    
    Contains all of the information pertinent to the player including the player_id,
    player_name, games the player plays, friends, and their victories associated with
    the games that they play

    Attributes:
        id: An int corresponding to the player id
        name: A string containing the player name
        scores: A dictionary in the format {game_id: game_score} containing a mapping between
            the game and the total of all the victory scores achieved in that game
        gamerscore: An int corresponding to the total score the player has achieved
        plays: A dictionary in the format {game_id: gamer_tag} containing a mapping
            between the gamer tag with the game the player plays with that tag
        friends: A list of player ids containing the ids of the player's friends
        victories: A dictionary in the format {game_id: [victory_id]} containing a mapping
            between the game the player plays and the victories that they have achieved
            in that game
    """

    def __init__(self, id, name):
        """Inits the id and name provided, and initializes gamerscore with 0 as well as provides empty 
        structures for plays, friends, and victories, and scores"""
        self.id = id
        self.name = name
        self.scores = {}
        self.gamerscore = 0
        self.plays = {}
        self.friends = []
        self.victories = {}

    def add_play(self, game_id, player_ign):
        """Add play to the plays dictionary given the game id and gamer tag"""
        self.plays[game_id] = player_ign
    
    def add_friend(self, friend_id):
        """Add friend to the list of friends"""
        self.friends.append(friend_id)
    
    def add_victory(self, game_id, victory_id, victory_score):
        """Adds victory to the victories dictionary given the game id 
        and adds the victory id to the list of victories assigned to the game id. 
        It creates a new list of victories if a victory has never been achieved in
        the game before. It also adds the score to the scores dictionary and adds to
        the total gamerscore"""

        if game_id not in self.victories.keys():
            self.victories[game_id] = [victory_id]
            self.scores[game_id] = victory_score
        else:
            self.victories[game_id].append(victory_id)
            self.scores[game_id] += victory_score
        
        self.gamerscore += victory_score

    def get_victories(self, game_id):
        """Returns the list of victories assigned to the game if that player
        has achieved a victory in the game, otherwise return an empty list"""

        if game_id not in self.victories.keys():
            return []
        else:
            return self.victories[game_id]
    
    def get_score(self, game_id):
        """Gets the total score of all the victories that the player has achieved
        in that particular game"""

        return self.scores[game_id]