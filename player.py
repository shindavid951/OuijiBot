import discord
class Player(object):
    def __init__(self, member: discord.Member):
        self.member = member
        self.hand = []
        self.field = []
        self.spirits = 0