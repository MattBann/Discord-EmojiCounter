import discord
import time
import emojiUsage
import databaseConnection


class MyClient(discord.Client):
    keyword = 'counter'

    # List of valid emojis (to be moved into seperate file/database for ease of change)
    validEmojis = (':zeepledome:', ':william:', ':tories:', ':suvek:', ':subscribe:', ':stressfolky:', ':stephen:',
                   ':smoljoe:', ':simp:', ':shrek:', ':shegan:', ':schlattpog:', ':rj:', ':pogchamp:', ':pepecross:',
                   ':parkourkidpog:', ':nathan:', ':morganfreewoman:', ':mehtab:', ':matthew:', ':longalex:', ':like:',
                   ':kermit:', ':joe:', ':jesus:', ':jamie:', ':jack:', ':hydration:', ':hollow:', ':henry:',
                   ':harold:', ':gru:', ':george:', ':farmermichael:', ':disgrace:', ':devil:', ':dad:', ':dab:',
                   ':chef:', ':cccs:', ':borispog:', ':boris:', ':bigwill:', ':BeardedGeorge:', ':baldwilbur:',
                   ':antipog:', ':alex:')

    countList = []

    # On start connect to database and load data
    def __init__(self,path):
        super().__init__()
        self.database = databaseConnection.Database(
            path)
        self.load_data()

    def load_data(self):
        self.countList = self.database.load_data()

    # Disord event when it has logged in
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Save contents of count to the database and reload data
    def save_data(self):
        for i in self.countList:
            if i.id is None:
                self.database.add_data(i.author, i.channel, i.time, i.emoji, i.server)
        self.load_data()

    # Discord event when a message is sent from a channel in a guild it is in
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # Ignore own messages
        if message.author == self.user:
            return

        # Initialisation (note always uses 'counter' keyword)
        if message.content.startswith('counter keyword'):
            self.keyword = message.content.split(' ')[2]
            await message.channel.send('Set new keyword')

        # Bot commands
        if message.content.startswith(self.keyword):
            commands = message.content.split(' ')[1:]
            print(message.content)
            itemCount = 0

            if commands[0] == 'count':
                
                # Check the emoji to find is valid and get its simplified form
                for i in self.validEmojis:
                    if i in commands[1]:
                        emojiToFind = i

                # For simple emoji counts:
                if len(commands) == 2:
                    for i in self.countList:
                        if i.emoji == emojiToFind and i.server == str(message.guild):
                            itemCount += 1
                    await message.channel.send(commands[1] + ' was used ' + str(itemCount) + ' times')
                    return

                # For more complex commands:
                elif len(commands) == 3:

                    # User specific command
                    if '@' in commands[2]:
                        for i in self.countList:
                            if ((i.emoji == emojiToFind) and (str(i.author) in commands[2])) and i.server == str(message.guild):
                                itemCount += 1
                        await message.channel.send(
                            commands[1] + ' was used ' + str(itemCount) + ' times by ' + str(commands[2]))
                        return
                    
                    # Channel specific command:
                    else:
                        print(commands[2])
                        for i in self.countList:
                            if ((i.emoji == emojiToFind) and (str(i.channel) in commands[2])) and i.server == str(message.guild):
                                itemCount += 1
                        await message.channel.send(
                            commands[1] + ' was used ' + str(itemCount) + ' times in ' + str(commands[2]))
                        return

            # Save command and confirmation message
            elif commands[0] == 'save':
                self.save_data()
                await message.channel.send('Data saved and reloaded')

        # Emoji counter:
        if ':' in message.content:
            for i in self.validEmojis:
                if i in message.content:
                    self.countList.append(
                        emojiUsage.EmojiUsage(
                            None, message.author.id, message.channel.id, str(time.localtime()), str(i), str(message.guild)))


# Get discord secret and database path
file = open('DiscordUserSecret.txt','r')
UserSecret = file.read()
file.close()

file = open('DatabasePath.txt','r')
path = file.read()
file.close()

client = MyClient(path)
client.run(UserSecret)
