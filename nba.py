from datetime import datetime, timezone
from dateutil import parser
import json
import discord
from discord.ext import tasks
from nba_api.live.nba.endpoints import scoreboard

# Replace with your actual channel IDs
CHANNEL_ID_GAME_NOT_STARTED = 123456789
CHANNEL_ID_GAME_STARTED = 987654321

# Discord client setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
intents.guilds = True
client = discord.Client(command_prefix=",", intents=intents)


async def send_message(status, home_team, away_team, home_team_score, away_team_score, home_team_tricode, away_team_tricode, home_city, away_city, game_clock, game_time_utc):
    """
    Sends a message to the Discord channel with the game status.
    """
    channel_id = CHANNEL_ID_GAME_STARTED
    game_start_time = parser.parse(game_time_utc)
    
    embed = discord.Embed(title=f'{home_team} v {away_team}', description=status, color=0xFA8072)

    if datetime.now(timezone.utc) < game_start_time:
        embed.add_field(name='Status', value="Game has not started yet ...")
        channel_id = CHANNEL_ID_GAME_NOT_STARTED
    else:
        if not game_clock:
            game_clock = "..."

        embed.add_field(name='Home', value=home_city)
        embed.add_field(name='Away', value=away_city)
        embed.add_field(name='Game Clock', value=game_clock)
        embed.add_field(name='Score', value=f'{home_team_tricode} {home_team_score}\n{away_team_tricode} {away_team_score}')

    embed.set_footer(text='Updated: ' + str(datetime.now())[:10])
    await client.get_channel(channel_id).send(embed=embed)

@client.event
async def on_ready():
    """
    Event handler for when the Discord client is ready.
    """
    print(f'Logged in as {client.user}')
    await client.wait_until_ready()
    game_update_loop.start()

@tasks.loop(seconds=120)
async def game_update_loop():
    """
    Regularly updates game information.
    """
    try:
        games_data = scoreboard.ScoreBoard().get_data()
        games = games_data['scoreboard']['games']
        for game in games:
            await send_message(game['gameStatusText'], 
                               game['homeTeam']['teamName'], game['awayTeam']['teamName'], 
                               game['homeTeam']['score'], game['awayTeam']['score'], 
                               game['homeTeam']['teamTricode'], game['awayTeam']['teamTricode'], 
                               game['awayTeam']['teamCity'], game['homeTeam']['teamCity'], 
                               game['gameClock'], game['gameTimeUTC'])

    except Exception as e:
        print(f'Error updating game data: {e}')

# Run the Discord bot (Replace with your actual token)
client.run('YOUR_DISCORD_BOT_TOKEN')

# Here is NBA scoreboard JSON for your reference. 
# Hey, you, go follow me on instagram for more free stuff: @hiimmichael_
# I mean, you're using my code, support me a little bit. Don't be a dick.

# print(games_json['scoreboard'])

# "games": [
# {
# "gameId": "0022200211", 
# "gameCode": "20221116/INDCHA", 
# "gameStatus": 2, 
# "gameStatusText": "Q1 06:54", 
# "period": 1, 
# "gameClock": "PT06M54.00S", 
# "gameTimeUTC": "2022-11-17T00:00:00Z", 
# "gameEt": "2022-11-16T19:00:00-05:00", 
# "regulationPeriods": 4, 
# "ifNecessary": false, 
# "seriesGameNumber": "", 
# "seriesText": "", 
# "homeTeam": 
#   {"teamId": 1610612766, 
#   "teamName": "Hornets", 
#   "teamCity": "Charlotte", 
#   "teamTricode": "CHA", 
#   "wins": 4, 
#   "losses": 11,
#   "score": 8, 
#   "seed": null, 
#   "inBonus": "0", 
#   "timeoutsRemaining": 6, 
# "periods": [
#   {"period": 1, "periodType": "REGULAR", "score": 8}, 
#   {"period": 2, "periodType": "REGULAR", "score": 0}, 
#   {"period": 3, "periodType": "REGULAR", "score": 0}, 
#   {"period": 4, "periodType": "REGULAR", "score": 0}]},
# "awayTeam": 
#   {"teamId": 1610612754, 
#   "teamName": "Pacers", 
#   "teamCity": "Indiana", 
#   "teamTricode": "IND", 
#   "wins": 6, 
#   "losses": 6, 
#   "score": 12, 
#   "seed": null, 
#   "inBonus": "0", 
#   "timeoutsRemaining": 7, 
#   "periods": [
#       {"period": 1, "periodType": "REGULAR", "score": 12}, 
#       {"period": 2, "periodType": "REGULAR", "score": 0}, 
#       {"period": 3, "periodType": "REGULAR", "score": 0}, 
#       {"period": 4, "periodType": "REGULAR", "score": 0}]}, 
# "gameLeaders": 
#   {"homeLeaders": 
#       {"personId": 203486, 
#       "name": "Mason Plumlee", 
#       "jerseyNum": "24", 
#       "position": "C", 
#       "teamTricode": "CHA", 
#       "playerSlug": "mason-plumlee", 
#       "points": 6, 
#       "rebounds": 2, 
#       "assists": 0}, 
#   "awayLeaders": 
#       {"personId": 1629614, 
#       "name": "Andrew Nembhard", 
#       "jerseyNum": "2", 
#       "position": "GF", 
#       "teamTricode": "IND", 
#       "playerSlug": "andrew-nembhard", 
#       "points": 4, 
#       "rebounds": 1, 
#       "assists": 0}}, 
# "pbOdds": 
#   {"team": null, 
#   "odds": 0.0, 
#   "suspended": 0}}, 
