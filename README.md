# Discord-EmojiCounter
A discord.py bot that counts emoji usage and stores information in an SQLite database

# Getting started
To have your own instance of the bot, you must create a discord application at https://discord.com/developers/applications, add a bot and put its token into a file named DiscordUserSecret.txt
You must also tell the program where you want the database to be stored. Place the directory path followed by the chosen file name (I recommend counterdata.db) into a file named DatabasePath.txt
These are both in the project root. Not making these will create an error.

After creating and linking the bot, you must add it to a server with relevant permissions. These are:
* View channels
* Send messages
* Mention everyone

# Usage
The default keyword is 'counter', though this can be changed by typing 'counter init {new keyword}'. Note that the keyword resets when the script stops.

The program automically counts usage in the background. Statistics can be obtained using these commands:

* count :emoji_name: - Gets overall count for this emoji
* count :emoji_name: @username - Gets count for this emoji from this user
* count :emoji_name: #channel-name - Gets count for this emoji from this channel

* count save - Saves current data to database and reloads (it automatically loads when you start the script)

eg: counter count :grinning: #general

Made by Matthew Bannock
