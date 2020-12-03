import discord
import time
import emojiUsage
import databaseConnection


class MyClient(discord.Client):
    initialised = False
    keyword = 'counter'

    validEmojis = (':zeepledome:', ':william:', ':tories:', ':suvek:', ':subscribe:', ':stressfolky:', ':stephen:',
                   ':smoljoe:', ':simp:', ':shrek:', ':shegan:', ':schlattpog:', ':rj:', ':pogchamp:', ':pepecross:',
                   ':parkourkidpog:', ':nathan:', ':morganfreewoman:', ':mehtab:', ':matthew:', ':longalex:', ':like:',
                   ':kermit:', ':joe:', ':jesus:', ':jamie:', ':jack:', ':hydration:', ':hollow:', ':henry:',
                   ':harold:', ':gru:', ':george:', ':farmermichael:', ':disgrace:', ':devil:', ':dad:', ':dab:',
                   ':chef:', ':cccs:', ':borispog:', ':boris:', ':bigwill:', ':BeardedGeorge:', ':baldwilbur:',
                   ':antipog:', ':alex:')

    countList = []

    def __init__(self,path):
        super().__init__()
        self.database = databaseConnection.Database(
            path)
        self.load_data()

    def load_data(self):
        self.countList = self.database.load_data()


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    def save_data(self):
        for i in self.countList:
            if i.id is None:
                self.database.add_data(i.author, i.channel, i.time, i.emoji, i.server)
        self.load_data()


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == self.user:
            return

        # for role in message.author.roles:
        #     print(role)
        # if message.content == "init" and self.initialised is False:
        #     await message.channel.send("Counter tied to this channel")
        #     self.initialised = True
        #     self.channelId = message.channel.id
        #     print(self.channelId)

        if self.initialised is False and message.content.startswith('counter init'):
            self.keyword = message.content.split(' ')[2]
            self.initialised = True
            await message.channel.send('Set new keyword')

        # Bot commands
        if message.content.startswith(self.keyword):
            commands = message.content.split(' ')[1:]
            print(message.content)
            itemCount = 0

            if commands[0] == 'count':
                for i in self.validEmojis:
                    if i in commands[1]:
                        emojiToFind = i
                if len(commands) == 2:
                    for i in self.countList:
                        if i.emoji == emojiToFind and i.server == str(message.guild):
                            itemCount += 1
                    await message.channel.send(commands[1] + ' was used ' + str(itemCount) + ' times')
                    return

                elif len(commands) == 3:
                    if '@' in commands[2]:
                        for i in self.countList:
                            if ((i.emoji == emojiToFind) and (str(i.author) in commands[2])) and i.server == str(message.guild):
                                itemCount += 1
                        await message.channel.send(
                            commands[1] + ' was used ' + str(itemCount) + ' times by ' + str(commands[2]))
                        return

                    else:
                        print(commands[2])
                        for i in self.countList:
                            if ((i.emoji == emojiToFind) and (str(i.channel) in commands[2])) and i.server == str(message.guild):
                                itemCount += 1
                        await message.channel.send(
                            commands[1] + ' was used ' + str(itemCount) + ' times in ' + str(commands[2]))
                        return

            elif commands[0] == 'save':
                self.save_data()
                await message.channel.send('Data saved and reloaded')

        elif message.content == '!event':
            await message.channel.send('Something that Will is gonna do idk')

        # Emoji counter:
        if ':' in message.content:
            for i in self.validEmojis:
                if i in message.content:
                    self.countList.append(
                        emojiUsage.EmojiUsage(
                            None, message.author.id, message.channel.id, str(time.localtime()), str(i), str(message.guild)))


file = open('DiscordUserSecret.txt','r')
UserSecret = file.read()
file.close()

file = open('DatabasePath.txt','r')
path = file.read()
file.close()

client = MyClient(path)
client.run(UserSecret)
