from webex_bot.webex_bot import WebexBot
from gpt import gpt

bot = WebexBot("NDlhNzQxNjktODk3My00MGJhLTg1MWQtZTAzMWRkMjc1Y2EwZDlhNzkyZDItNmE3_P0A1_edb06b55-c800-4c42-83d8-f014369a7fd3")
bot.commands.clear()
bot.add_command(gpt())
bot.help_command = gpt()
bot.run()
