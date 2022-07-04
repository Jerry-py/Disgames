## Button games documentation!
---
# Akinator
The Akinator class takes 1 arg and 2 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- child_mode (If set to `True` then the bot will only ask sfw questions, otherwise it will ask nsfw questions. `True` by default)
	- language (Decides what language the bot will be asking the questions in. `"en"` by default)

The start function of the Akinator class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Checkers
The Checkers class takes 1 arg and 3 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- red (The red player)
	- blue (The blue player)
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{"r": "🔴", "b": "🔵", " ": "⬛", "rk": "♦", "bk": "🔷"}` by default)

The start function of the Checkers class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Chess
The Chess class takes 1 arg and 4 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- white (The white player)
	- black (The black player)
	- fen (The starting fen of the board. `'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'` by default)
	- chess960 (An integer from 0-959 which will give a "shuffled" position depending on the integer. `None` by default)

The start function of the Chess class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Connect4
The Connect4 class takes 1 arg and 3 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- red (The red player)
	- blue (The blue player)
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{"r": "🔴","b": "🔵"," ": "⬛","R": "♦️","B": "🔷"}` by default)

The start function of the Connect4 class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Hangman
The Hangman class takes 1 arg and 3 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- min (The minimum length of the word. `3` by default)
	- max (The maximum length of the word. `7` by default)
	- word (The word to be used. `None` by default, Note: if a word is provided it will be used even if a min/max are provided)

The start function of the Hangman class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Minesweeper
The Minesweeper class takes 1 arg and 2 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- chance (A float smaller than `1` which determines whether to put a bomb or not. `.17` by default, Note: `.17` does not necessarily mean that there will be 17 bombs)
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{"b": "💣","f": "🚩"," ": "🟦","0": "⬛","10": "🔟","x":"❌",'B':"💥"}` by default)

The start function of the Minesweeper class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)


# Snake
The Snake class takes 1 arg and 2 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{'a':'🍎', 'h':'😳', 'b':'🟡', ' ':'⬛'}` by default)
	- board_size (The size of the snake board. `10` by default)

The start function of the Snake class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# Soko
The Soko class takes 1 arg and 3 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- play_forever (A bool which determines if a new board should be created if the user wins. `False` by default)
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{'p':'😳','tp':'😳','t':'❎','b':'🟫','bt':'✅',' ':'⬛','w':'⬜'}` by default)
	- board (If provided, it will attempt to create a game board out of the nested list which should look something like `[['w','w','w','w','w'],['w','p','b','t','w'],['w','w','w','w','w']]`. `None` by default, Note: You're responsible for making sure that the board is playable/winable (p > 0, t <= b))

The start function of the Soko class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)

# TicTacToe
The TicTacToe class takes 1 arg and 3 kwargs
- Args
	- ctx (The command's context)
- kwargs
	- x (The person playing as x)
	- o (The person playing as o)
	- format_dict (This dict will be used to format the board the player sees by replacing the key with the value. `{' ':'⬛','x':'❌','o':'⭕'}` by default)

The start function of the TicTacToe class takes 0 args and 0 kwargs

# Wordle
The Wordle class takes 1 arg and 2 kwargs
- Args
	- ctx (The command's context)
- Kwargs
	- word (A string which is expected to be 5 letters long that will be used as the wordle word. `None` by default)
	- image (A bool which decides whether to display the game as an image or not. `False` by default)

The start function of the Worlde class takes 0 args and 1 kwargs
- Kwargs
	- end_game_option (If set to `True` an additional button will be added, when pressed the game will end. `False` by default)
---
## Note:
- Since most classes are subclassed from `discord.ui.View` you could add a button to them if you wish, just know that not **all** classes subclass `discord.ui.View`. Such inconsistency will be removed in the future