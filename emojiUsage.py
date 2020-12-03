class EmojiUsage():
    def __init__(self, id, author, channel, time, emoji, server):
        self.id = id
        self.author = author
        self.channel = channel
        self.time = time
        self.emoji = emoji
        self.server = server
        print('All good')
        print(self.channel,self.author,self.time, self.emoji)