from typing import Dict

class Card():
    def __init__(self, name, cost, color, image):
        self.name = name
        self.cost = cost
        self.color = color
        self.image = image

class FateCard(Card):
    def __init__(self, name, cost, color, image, effect):
        super().__init__(name, cost, color, image)
        self.effect = effect

class UnitCard(Card):
    def __init__(self, name, cost, color, image, attacks: Dict[range, tuple], effects=None, stars=0, status=None):
        super().__init__(name, cost, color, image)
        self.attacks = attacks
        self.effects = effects
        self.stars = stars
        self.status = status

class AssuredCancer(FateCard):
    def __init__(self):
        effectText = "Choose a Unit. That Unit cannot Perish this turn, regardless of any other effects."
        super().__init__("Assured Cancer", 1, "Sapphire", "./card_images/AssuredCancer.png", effectText)

class BlazingAries(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Pyromancy", "Ruby", 40),
            range(40, 65): ("Great Ritual", "Ruby", 60),
            range(65, 100): ("Spark", "Ruby", 10)
        }
        super().__init__("Blazing Aries", 1, "Ruby", "./card_images/BlazingAries.png", attacks)

class BurstingAquarius(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Pouring River", "Sapphire", 20),
            range(40, 60): ("Thundering Pour", "Sapphire", 40),
            range(60, 100): ("Gain a Spirit. Discard a card", "Orange", 0)
        }
        super().__init__("Bursting Aquarius", 1, "Sapphire", "./card_images/BurstingAquarius.png", attacks)

class CalmRabbitFestival(UnitCard):
    def __init__(self):
        attacks = {
            range(45): ("Night of Rebuke", "Emerald", 70),
            range(45, 90): ("Poisonous Bloom", "Purple", 50),
            range(90, 100): ("Miss", "White", 0)
        }
        effects = {
            range(45, 90): "Poisoned"
        }
        super().__init__("Calm Rabbit Festival", 3, "Emerald", "./card_images/CalmRabbitFestival.png", attacks, effects)

class CapricornAssistance(FateCard):
    def __init__(self):
        effectText = "Return a Unit you control to your hand. Remove all status effects, stars, and card effects from that card. Gain 1 Spirit."
        super().__init__("Capricorn Assitance", 1, "Emerald", "./card_images/CapricornAssitance.png", effectText)

class CrushingEmperor(UnitCard):
    def __init__(self):
        attacks = {
            range(60): ("Harbored Strike", "Ruby", 50),
            range(60, 90): ("Miss", "White", 0),
            range(90, 100): ("Perish either Unit in the LL", "Orange", 0)
        }
        super().__init__("The Crushing Emperor", 1, "Ruby", "./card_images/CrushingEmperor.png", attacks)

class CuriousMonkeys(UnitCard):
    def __init__(self):
        attacks = {
            range(20): ("Screech", "Ruby", 43),
            range(20, 55): ("Pickpocket", "Sapphire", 38),
            range(55, 80): ("Summon Gang", "Emerald", 34),
            range(80, 100): ("Miss", "White", 0)
        }
        super().__init__("Curious Monkeys", 1, "Amethyst", "./card_images/CuriousMonekys.png", attacks)

class DayOfSheep(FateCard):
    def __init__(self):
        effectText = "Skip the Combat Phase of this turn. You may lose a Spirit. If you do, draw a card."
        super().__init__("Day of Sheep", 1, "Amethyst", "./card_images/DayOfSheep.png", effectText)

class DeathLingerer(UnitCard):
    def __init__(self):
        attacks = {
            range(70): ("Black Flag", "Ruby", 80),
            range(70, 100): ("Miss", "White", 0)
        }
        super().__init__("Death Lingerer", 2, "Ruby", "./card_images/DeathLingerer.png", attacks)

class DevilDeposit(UnitCard):
    def __init__(self):
        attacks = {
            range(50): ("Devil Delight", "Emerald", 50),
            range(50, 90): ("Shunned", "Purple", 0),
            range(90, 100): ("Miss", "White", 0)
        }
        effects = {
            range(50, 90): "Depressed"
        }
        super().__init__("Devil Deposit", 2, "Emerald", "./card_images/DevilDeposit.png", attacks, effects)

class ElusiveHermit(UnitCard):
    def __init__(self):
        attacks = {
            range(80): ("Quiet Light", "Sapphire", 50),
            range(80, 100): ("If only Unit in play, gain 2 stars.", "Orange", 0)
        }
        super().__init__("Elusive Hermit", 1, "Sapphire", "./card_images/ElusiveHermit.png", attacks)

class FoolishIndecisive(UnitCard):
    def __init__(self):
        attacks = {
            range(30): ("Ruby Riot", "Ruby", 30),
            range(30, 60): ("Sapphire Swindle", "Sapphire", 30),
            range(60, 90): ("Emerald Eve", "Emerald", 30),
            range(90, 100): ("Miss", "White", 0)
        }
        super().__init__("The Foolish Indecisive", 0, "Amethyst", "./card_images/FoolishIndecisive.png", attacks)

class GeminiPactsworns(UnitCard):
    def __init__(self):
        attacks = {
            range(50): ("Leftmost Sword", "Emerald", 50),
            range(50, 100): ("Rightmost Sword", "Emerald", 50)
        }
        super().__init__("Gemini Pactsworns", 2, "Emerald", "./card_images/GeminiPactsworns.png", attacks)

class GrandLibra(UnitCard):
    def __init__(self):
        attacks = {
            range(50): ("Forgiveness", "Ruby", 30),
            range(50, 95): ("Sudden Prosper", "Ruby", 70),
            range(90, 100): ("Enlightened Smite", "Ruby", 120)
        }
        super().__init__("Grand Libra", 2, "Ruby", "./card_images/GrandLibra.png", attacks)

class HangedMansWoe(UnitCard):
    def __init__(self):
        attacks = {
            range(50): ("Rushing Thought", "Emerald", 30),
            range(50, 90): ("Perish this Unit.", "Orange", 0),
            range(90, 100): ("Miss", 0)
        }
        effects = {
            range(50, 90): "Depressed"
        }
        super().__init__("Hanged Man's Woe", 1, "Emerald", "./card_images/HangedMan'sWoe.png", attacks, effects)

class HonestPig(UnitCard):
    def __init__(self):
        attacks = {
            range(80): ("Angry Snuffle", "Sapphire", 10),
            range(80, 100): ("Draw a card", "Orange", 0)
        }
        super().__init__("Honest Pig", 0, "Sapphire", "./card_images/HonestPig.png", attacks)

class JudgementYou(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Guilty", "Emerald", 100),
            range(40, 80): ("Innocent", "Sapphire", 50),
            range(80, 100): ("Retrial", "Ruby", 10)
        }
        super().__init__("Judgement, You", 3, "Amethyst", "./card_images/JudgementYou.png", attacks)

class JusticeOfNaught(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Righteous Blade", "Sapphire", 20),
            range(40, 80): ("To the Dungeon", "Purple", 0),
            range(80, 100): ("If opposing Unit has 1 star, it Perishes.", 0)
        }
        effects = {
            range(40, 80): "Forgotten"
        }
        super().__init__("Justice of Naught", 3, "Sapphire", "./card_images/JusticeOfNaught.png", attacks, effects)

class LaughingSnake(FateCard):
    def __init__(self):
        effectText = "Your opponent discards a card from their hand. If they cannot, a Unit you control gains 1 star."
        super().__init__("Laughing Snake", 1, "Emerald", "./card_images/LaughingSnake.png", effectText)

class LoneHighPriestess(UnitCard):
    def __init__(self):
        attacks = {
            range(75): ("Diplomacy", "Sapphire", 30),
            range(75, 100): ("Miss", "White", 0)
        }
        super().__init__("The Lone High Priestess", 0, "Sapphire", "./card_images/LoneHighPriestess.png", attacks)

class LoversBeneath(UnitCard):
    def __init__(self, attacksUsed=[False, False]):
        attacks = {
            range(40): ("Together the Same", "Sapphire", 30),
            range(40, 80): ("And So To Remain", "Sapphire", 30),
            range(80, 100): ("If both attacks have been used, draw a card.", "Orange", 0)
        }
        super().__init__("Lovers Beneath", 1, "Sapphire", "./card_images/LoversBeneath.png", attacks)
        self.attacksUsed = attacksUsed

class LoyalDog(UnitCard):
    def __init__(self):
        attacks = {
            range(80): ("Snarl", "Emerald", 20),
            range(80, 90): ("Opposing Unit loses 1 or 2 stars."),
            range(90, 100): ("Miss", 0)
        }
        super().__init__("Loyal Dog", 0, "Emerald", "./card_images/LoyalDog.png", attacks)

class LuckyDragon(UnitCard):
    def __init__(self):
        attacks = {
            range(30): ("Lucky Break", "Orange", 50),
            range(30, 90): ("Almighty Breath", "Purple", 100),
            range(90, 100): ("Miss", "White", 0)
        }
        effects = {
            range(30): ("For each star your opponent's Units have, draw a card.")
        }
        super().__init__("Lucky Dragon", 3, "Amethyst", "./card_images/LuckyDragon.png", attacks, effects)

class MimicHorse(FateCard):
    def __init__(self):
        effectText = "Copy the effects of another Fate Card in your hand to use as this card's effect."
        super().__init__("Mimic Horse", 1, "Ruby", "./card_images/MimicHorse.png", effectText)

class MoonlightEmbassy(UnitCard):
    def __init__(self):
        attacks = {
            range(100): ("All Encompassing Moon", "Sapphire", 50)
        }
        super().__init__("Moonlight Embassy", 2, "Sapphire", "./card_images/MoonlightEmbassy.png", attacks)

class NobleChariot(UnitCard):
    def __init__(self):
        attacks = {
            range(80): ("Fast Pierce", "Emerald", 20),
            range(80, 90): ("If this Unit has a star, gain 1 star.", "Orange", 0),
            range(90, 100): ("Miss", 0)
        }
        super().__init__("Noble Chariot", 1, "Emerald", "./card_images/NobleChariot.png", attacks)

class PageOfLostSword(FateCard):
    def __init__(self):
        effectText = "If you control a Sapphire Unit, draw 2 cards and roll a d6. If the result is a 6, all Units get the Forgotten status."
        super().__init__("Page of Lost Sword", 0, "Sapphire", "./card_images/PageOfLostSword.png", effectText)

class PageOfPentaclesGrace(FateCard):
    def __init__(self):
        effectText = "If you control a Ruby Unit, draw 2 cards and your opponent is a fucking idiot. Choose an enemy Unit. It gets the Depressed status."
        super().__init__("Page of Pentacles Grace", 0, "Ruby", "./card_images/PageOfPentaclesGrace", effectText)

class PageOfWandsAhold(FateCard):
    def __init__(self):
        effectText = "If you control an Emerald Unit, draw 2 cards. Choose an enemy Unit. It gets the Poisoned status."
        super().__init__("Page of Wands Ahold", 0, "Emerald", "./card_images/PageOfWandsAhold.png", effectText)

class PiscesPondLuck(FateCard):
    def __init__(self):
        effectText = "If you have only this card in your hand, draw 3 cards."
        super().__init__("Pisces Pond Luck", 1, "Sapphire", "./card_images/PiscesPondLuck.png", effectText)

class PoisonousMagician(UnitCard):
    def __init__(self):
        attacks = {
            range(25): ("Poison Bottle", "Purple", 0),
            range(25, 55): ("Blade of Grass", "Emerald", 20),
            range(55, 75): ("Miracle", "Emerald", 40),
            range(75, 100): ("Miss", "White", 0)
        }
        effects = {
            range(25): "Poisoned"
        }
        super().__init__("The Poisonous Magician", 0, "Emerald", "./card_images/PoisonousMagician.png", attacks, effects)

class SagittariusHunter(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Piercing Shot", "Sapphire", 50),
            range(40, 60): ("If the opposing Unit is Ruby, Perish it.", "Orange", 0),
            range(60, 80): ("If the opposing Unit is Sapphire, Perish it.", "Orange", 0),
            range(80, 100): ("If the opposing unit is Emerald, Perish it.", "Orange", 0)
        }
        super().__init__("Sagittarius Hunter", 2, "Sapphire", "./card_images/SagittariusHunter.png", attacks)

class ScorpioLethality(FateCard):
    def __init__(self):
        effectText = "Perish an enemy Unit or Poison an enemy Unit."
        super().__init__("Scorpio Lethality", 1, "Emerald", "./card_images/ScorpioLethality.png", effectText)

class StarMellowLight(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Essence Star", "Emerald", 80),
            range(40, 55): ("Last Drink", "Purple", 0),
            range(55, 70): ("Mud Drink", "Purple", 0),
            range(70, 85): ("Eclipse Drink", "Purple", 0),
            range(85, 100): ("Miss", "White", 0)
        }
        effects = {
            range(40, 55): "Depressed",
            range(55, 70): "Poisoned",
            range(70, 85): "Forgotten"
        }
        super().__init__("Star Mellow Light", 2, "Emerald", "./card_images/StarMellowLight.png", attacks, effects)

class StrengthAbove(UnitCard):
    def __init__(self):
        attacks = {
            range(30): ("Absolute Strength", "Ruby", 100),
            range(30, 100): ("Miss", "White", 0)
        }
        super().__init__("Strength Above", 1, "Ruby", "./card_images/StrengthAbove.png", attacks)

class SunsSteedLeo(FateCard):
    def __init__(self):
        effectText = "Choose a Unit. That Unit gets +20 Attack Power to each Attack it has until the end of the turn. If you chose a Ruby Unit, draw a card."
        super().__init__("The Sun's Steed, Leo", 1, "Ruby", "./card_image/Sun'sSteedLeo", effectText)

class SunOfSonglett(UnitCard):
    def __init__(self):
        attacks = {
            range(30): ("Life Reborn", "Ruby", 200),
            range(30, 65): ("Opposing Unit Perishes.", "Orange", 0),
            range(65, 100): ("Miss", "White", 0)
        }
        super().__init__("The Sun of Songlett", 2, "Ruby", "./card_images/SunOfSonglett.png", attacks)

class TaurusQuaker(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Wild Charge", "Emerald", 40),
            range(40, 60): ("Goring Press", "Emerald", 60),
            range(60, 100): ("Miss", "White", 0)
        }
        super().__init__("Taurus Quaker", 1, "Emerald", "./card_images/TaurusQuaker.png", attacks)

class TemperanceTriad(UnitCard):
    def __init__(self):
        attacks = {
            range(33): ("Drawn Water", "Sapphire", 30),
            range(33, 66): ("Raised Wing", "Sapphire", 50),
            range(66, 100): ("Doth Pass Over", "Sapphire", 80)
        }
        super().__init__("Temperance Triad", 2, "Sapphire", "./card_images/TemperanceTriad.png", attacks)

class TirelessRooster(UnitCard):
    def __init__(self):
        attacks = {
            range(20): ("Hard Work Pays Off", "Ruby", 70),
            range(20, 100): ("Miss", "White", 0)
        }
        super().__init__("Tireless Rooster", 0, "Ruby", "./card_images/TirelessRooster.png", attacks)

class TowerAbove(UnitCard):
    def __init__(self):
        attacks = {
            range(50): ("Stare Beyond", "Sapphire", 30),
            range(50, 75): ("Stone Life", "Emerald", 20),
            range(75, 100): ("Ferza Satum", "Ruby", 20)
        }
        super().__init__("The Tower Above", 2, "Amethyst", "./card_images/TowerAbove.png", attacks)

class UnmovingTigers(UnitCard):
    def __init__(self):
        attacks = {
            range(100): ("Artful Strike", "Sapphire", 90)
        }
        super().__init__("Unmoving Tigers", 3, "Sapphire", "./card_images/UnmovingTigers.png", attacks, None, 0, "Immune")

class VengefulEmpress(UnitCard):
    def __init__(self):
        attacks = {
            range(70): ("Harbored Strike", "Ruby", 40),
            range(70, 100): ("Miss", "White", 0)
        }
        super().__init__("The Vengeful Empress", 0, "Ruby", "./card_images/VengefulEmpress.png", attacks)

class VictorysOx(UnitCard):
    def __init__(self):
        attacks = {
            range(55): ("Grand Stomp", "Ruby", 60),
            range(55, 80): ("If opposing Unit is Emerald or Sapphire, Perish it, then draw a card.", "Orange", 0),
            range(80, 100): ("Miss", "White", 0)
        }
        super().__init__("Victory's Ox", 3, "Ruby", "./card_images/Victory'sOx.png", attacks)

class VirgosHarvest(FateCard):
    def __init__(self):
        effectText = "Remove a status effect from a Unit. If the chosen Unit Perishes an enemy Unit this turn, it gains 2 stars instead of 1."
        super().__init__("Virgo's Harvest", 1, "Ruby", "./card_images/Virgo'sHarvest.png", effectText)

class WealthyRat(FateCard):
    def __init__(self):
        effectText = "Lose any amount of Spirits. Draw cards equal to the number of Spirits spent."
        super().__init__("Wealthy Rat", 1, "Amethyst", "./card_images/WealthyRat.png", effectText)

class WheelOfFortune(UnitCard):
    def __init__(self, attacksUsed = [False, False, False]):
        attacks = {
            range(20): ("Bull Gore", "Ruby", 40),
            range(20, 40): ("Angel Ray", "Sapphire", 30),
            range(40, 60): ("Spinful Sin", "Emerald", 20),
            range(60, 80): ("If each attack has been used, gain 3 stars.", "Orange", 0),
            range(80, 100): ("Miss", "White", 0)
        }
        super().__init__("Wheel of Fortune", 1, "Ruby", "./card_images/WheelOfFortune.png", attacks)
        self.attacksUsed = attacksUsed

class WiseHierophant(UnitCard):
    def __init__(self):
        attacks = {
            range(40): ("Future Sight", "Emerald", 40),
            range(40, 55): ("Poisoned Drink", "Purple", 0),
            range(55, 75): ("Major Revelation", "Emerald", 60),
            range(75, 100): ("Miss", "White", 0)
        }
        effects = {
            range(40, 55): "Poisoned"
        }
        super().__init__("Wise Hierophant", 1, "Emerald", "./card_images/WiseHierophant.png", attacks, effects)

class WorldOfFinale(UnitCard):
    def __init__(self):
        attacks = {
            range(90): ("If an opposing Unit has 2 stars, gain 3 stars.", "Orange", 0),
            range(90, 100): ("Restart", "Ruby", 300)
        }
        super().__init__("The World of Finale", 3, "Amethyst", "./card_images/WorldOfFinale.png", attacks)