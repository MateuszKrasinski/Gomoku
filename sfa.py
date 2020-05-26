import collections

GameSettings = collections.namedtuple("GameSettings", "player1 player2 game_mode")
GameSettings.game_mode = "Standard"
GameSettings.player1 = "Gracz1"
GameSettings.player2 = "Gracz2"
print(GameSettings.game_mode)