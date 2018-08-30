class Victory:
    """A record of a victory, the victory name, the game that that victory can be achieved in, etc.
    
    Contains all of the information pertinent to the game including the victory id, the game that the
    victory can be achieved in, the victory name, the points assigned to that victory, the number of 
    times the victory is accomplished, and the players who have achieved the victory

    Attributes:
        victory_id: An int corresponding to the victory id
        game_id: An int corresponding to the game id
        name: A string containing the victory name
        points: An int corresponding to the points achieved for achieving the victory
        times_accomplished: An int corresponding to the number of times that victory is accomplished
        players: A list of player ids corresponding to the players that have achieved the victory
    """

    def __init__(self, victory_id, game_id, name, points):
        """Inits the victory id, game id, name, and points provided and inits times_accomplished with 0 and players with an empty list"""
        self.victory_id = victory_id
        self.game_id = game_id
        self.name = name
        self.points = points
        self.times_accomplished = 0
        self.players = []
    
    def add_player(self, player_id):
        """Adds player to the list of the players who have achieved the victory"""
        self.players.append(player_id)