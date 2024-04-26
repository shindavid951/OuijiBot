import discord
from typing import List
from card import Card
class Player(object):
    def __init__(self, member: discord.Member):
        self.member = member
        self.hand: List[Card] = []
        self.field: List[Card] = []
        self.spirits = 0