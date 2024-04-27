import discord
from typing import List
from card import *
class Player(object):
    def __init__(self, member: discord.Member):
        self.member = member
        self.hand: List[Card] = []
        self.field: List[UnitCard] = [None, None, None]
        self.spirits = 0