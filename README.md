# NBA Score Tracker

## Description
The NBA Score Tracker is a Python-based application designed to provide real-time updates on NBA scores directly to your Discord server. Utilizing a simple yet powerful shell script (`start.sh`), the tracker offers an easy and efficient way to stay updated with the latest scores from the NBA.

## Features
- Real-time NBA score updates
- Easy setup and execution
- Graceful handling of script interruptions
- Discord integration for live notifications

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Discord Bot Token (refer to Discord's bot setup guide)
- Required Python packages: `discord.py`, `nba_api`, `python-dateutil`

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the necessary Python packages:
   ```
   pip install discord.py nba_api python-dateutil
   ```

## Configuration
1. Create a Discord bot and obtain your token.
2. In the `nba.py` script, replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual bot token.

## Usage
To start the NBA Score Tracker, follow these steps:
1. Open your terminal.
2. Change directory to your script's location:
   ```
   cd path/to/your/script
   ```
3. Make `start.sh` executable (if not already done):
   ```
   chmod +x start.sh
   ```
4. Run the script:
   ```
   ./start.sh
   ```

To stop the script, press `Ctrl+C`. The script ensures a clean and safe shutdown.

## Contributing
Contributions to the NBA Score Tracker are welcome. Feel free to reach out!

## Contact
Your Name - contact@hiimmichael.com

## Acknowledgements
- NBA API: https://github.com/swar/nba_api
- Discord.py: https://github.com/Rapptz/discord.py
- All Contributors