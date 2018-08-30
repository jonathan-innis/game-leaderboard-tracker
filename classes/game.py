class Game:
    """A record of a game, the game's name, the players who play the game, etc.
    
    Contains all of the information pertinent to the game including the game id, the game
    name, the players who play the game, and the victories associated with the game

    Attributes:
        id: An int corresponding to the game id
        name: A string containing the game name
        players: A list of player ids containing all of the players who play the game
        victories: A dictionary in the format {victory_id: Victory()} containing the mapping
            between the victory id and the actual victory object
    """

    def __init__(self, id, name):
        """Inits the id and name provided and provides empty structures for players and victories""" 
        self.id = id
        self.name = name
        self.players = []
        self.victories = {}
    
    def add_player(self, player_id):
        """Adds player id to the list of players who play the game"""
        self.players.append(player_id)
    
    def add_victory(self, victory_id, victory):
        """Adds the victory to the dictionary of victories assigned to the game"""
        self.victories[victory_id] = victory
