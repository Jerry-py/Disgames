from disgames import register_commands
from discord.ext import commands

bot = commands.Bot("!", help_command=None, case_insensitive=True)
register_commands(bot)
assert len(bot.commands) == 11  # chess, madlib, ttt, hangman, etc
