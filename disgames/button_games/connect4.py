import discord

class Connect4Modal(discord.ui.Modal, title='Connect4'):
	def __init__(self, button):
		super().__init__()
		self.button = button

	inp = discord.ui.TextInput(
		label='Index',
		placeholder='Type your index here... (1-7)'
	)

	async def on_submit(self, interaction):
		inp = self.inp.value
		view = self.button.view

		if interaction.user != view.turns[view.turn]:
			return await interaction.response.send_message(content="It's not your turn", ephemeral=True)
		if inp.isdigit() and int(inp)-1 in range(7):
			done = view.move(int(inp)-1)
			if not done:
				return await interaction.response.send_message(content=f"Can't put in that column anymore", ephemeral=True)
			won = view.has_won()
			if won != None:
				for child in view.children:
					child.disabled = True
				if won == False:
					embed = discord.Embed(title='Connect4', description=f'Turn: {view.turns[view.turn].mention}\n'+view.format_board(), color=drawn_game_color)
					await interaction.response.edit_message(content='Tie!', embed=embed, view=view)
					view.winner = None
					view.stop()
					return
				else:
					embed = discord.Embed(title='Connect4', description=f'Turn: {view.turns[view.turn].mention}\n'+view.format_board(), color=won_game_color)
					await interaction.response.edit_message(content=f'{view.turns[view.turn].mention} connected 4 {won[1]}', embed=embed, view=view)
					view.winner = interaction.user
					view.stop()
					return
			view.turn = 'b' if view.turn == 'r' else 'r'
			embed = discord.Embed(title='Connect4', description=f'Turn: {view.turns[view.turn].mention}\n'+view.format_board(), color=ongoing_game_color)
			await interaction.response.edit_message(embed=embed, view=view)
		else:
			return await interaction.response.send_message(content=f"{inp} is not a valid move", ephemeral=True)

class Connect4(discord.ui.View):
	def __init__(self, ctx, *, red, blue, format_dict={}):
		super().__init__()

		from .. import ongoing_game_color, lost_game_color, won_game_color, drawn_game_color
		global ongoing_game_color, lost_game_color, won_game_color, drawn_game_color

		self.ctx = ctx
		self.board = [[' ' for _ in range(7)] for _ in range(6)]
		self.turn = 'r'
		self.turns = {'r':red,'b':blue}
		self.format_dict = format_dict
		self.default_format_dict = {
								"r": "🔴",
								"b": "🔵",
								" ": "⬛",
								"R": "♦️",
								"B": "🔷"
		}

	@discord.ui.button(label='Play move!', style=discord.ButtonStyle.blurple)
	async def play_move(self, interaction, button):
		await interaction.response.send_modal(Connect4Modal(button))

	async def end_game(self, interaction):
		self.winner = self.turns['r'] if interaction.user == self.turns['b'] else self.turns['b']
		self.stop()
		for child in self.children:
			child.disabled = True
		embed = discord.Embed(title='Connect4', description=f'Game ended by: {interaction.user.mention}\n'+self.format_board(), color=lost_game_color)
		await interaction.response.edit_message(content='Game ended', embed=embed, view=self)

	async def interaction_check(self, interaction):
		if interaction.user not in list(self.turns.values()):
			await interaction.response.send_message(content="You're not playing in this game", ephemeral=True)
		else:
			return True

	def format_board(self):
		lst = []
		for row in self.board:
			lst.append(''.join([self.format_dict.get(i, self.default_format_dict.get(i,i)) for i in row]))
		return '\n'.join(lst)+'\n1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣'

	def move(self, index):
		if self.board[0][index] != ' ':
			return None
		for y in range(0, 6):
			if self.board[5-y][index] == ' ':
				self.board[5-y][index] = self.turn
				break
		return True

	def has_won(self):
		height = 6
		width = 7
		for x in range(height):
			for y in range(width - 3):
				if (self.board[x][y] == self.board[x][y + 1] and self.board[x][y] == self.board[x][y + 2] and self.board[x][y] == self.board[x][y + 3] and self.board[x][y] != " "):
					self.board[x][y] = self.board[x][y].upper()
					self.board[x][y + 1] = self.board[x][y].upper()
					self.board[x][y + 2] = self.board[x][y].upper()
					self.board[x][y + 3] = self.board[x][y].upper()
					return True, "in a horizontal row"
		for x in range(height - 3):
			for y in range(width):
				if (self.board[x][y] == self.board[x + 1][y] and self.board[x][y] == self.board[x + 2][y] and self.board[x][y] == self.board[x + 3][y] and self.board[x][y] != " "):
					self.board[x][y] = self.board[x][y].upper()
					self.board[x + 1][y] = self.board[x][y].upper()
					self.board[x + 2][y] = self.board[x][y].upper()
					self.board[x + 3][y] = self.board[x][y].upper()
					return True, "in a vertical row"
		for x in range(height - 3):
			for y in range(width - 3):
				if (self.board[x][y] == self.board[x + 1][y + 1] and self.board[x][y] == self.board[x + 2][y + 2] and self.board[x][y] == self.board[x + 3][y + 3] and self.board[x][y] != " "):
					self.board[x][y] = self.board[x][y].upper()
					self.board[x + 1][y + 1] = self.board[x][y].upper()
					self.board[x + 2][y + 2] = self.board[x][y].upper()
					self.board[x + 3][y + 3] = self.board[x][y].upper()
					return True, "on a \ diagonal"
		for x in range(height - 3):
			for y in range(3, width):
				if (self.board[x][y] == self.board[x + 1][y - 1] and self.board[x][y] == self.board[x + 2][y - 2] and self.board[x][y] == self.board[x + 3][y - 3] and self.board[x][y] != " "):
					self.board[x][y] = self.board[x][y].upper()
					self.board[x + 1][y - 1] = self.board[x][y].upper()
					self.board[x + 2][y - 2] = self.board[x][y].upper()
					self.board[x + 3][y - 3] = self.board[x][y].upper()
					return True, "in a / diagonal"
		if not sum([row.count(' ') for row in self.board]):
			return False
		return None

	async def start(self, *, end_game_option=False):
		if end_game_option:
			button = discord.ui.Button(emoji='⏹', style=discord.ButtonStyle.danger)
			button.callback = self.end_game
			self.add_item(button)
		embed = discord.Embed(title='Connect4', description = f'Turn: {self.turns[self.turn].mention}\n'+self.format_board(), color=ongoing_game_color)
		self.msg = await self.ctx.send(embed=embed, view=self)
		await self.wait()
		return self.winner
