###########################################
#           ~  PLAINS OF WYN  ~           #
###########################################
# A game by Antoine.c | Project started November 1st of 2020 | Genre: Text-based RPG (with interestings mechanics) #
# Made as my first python beginner project | Coded with <3 with Atom IDE | AMA Eosis#6008 on discord #

# KANBAN SPACE
# Stat system with vars in the player class and armor ans weapons change these stats, they add up if: MAX TWO WEAPONS (right and left hand) MAX FOUR ARMORS (one of each type/slot)
# Loading saving system pickle
# Monster class with stats and self.inv = [] and self.entries = 3, combat class with different types of combat.fight() functions like combat.fightPVE() combat.fightPVP() for differents type of 1V1 fights
# Combat class: loop that checks the life of the two fighetrs then turn system and formulas THEN repeat and then loot the items or die depending on who won the fight (3 choices per turn: FIGHT DEF ITEM)
# Make funcs for loot and inventory to make them read-able (loops through the items and prints them nicely to make the things read-able)
# Shops
# Dungeons
# An actual story?
# Tkinter graphical interface
# Map system
# Put the inventory arguments in the init function of the corresponding class (ex: inventory(P.inv).addItem("Test",1) instead of inventory.addItem(P.inv,"Test",1)
# Commands to move around, open the inventory, talk with NPCs...
# NPC system
# Item class with stats , lore, price, name, slot ETC  and premade items stored in variables



#VARIABLES ET IMPORTS
import random # Used for the RNG and randint func
import sys # To exit the game automatically
import time # Used to make pauses in the game and check current real time
import pickle # Used to make saving and loading system

class player:
    def __init__(self,name):
        self.hp = 100
        self.mp = 30
        self.gold = 100
        self.name = name
        self.inv = {}
        self.maxInvSize = 50
        self.faction = "faction"
        self.race = "race"
        self.atk =  20
        self.defense = 10
        self.cc = 5
        self.cd = 5
        self.luck = 1

P = player("Eosis")
print(P.faction)


class monster:
    def __init__(self,name,hp,inv,entries,gold,atk,defense,cc,cd,luck):
        self.name = name
        self.hp = hp
        self.inv = inv
        self.entries = entries
        self.gold = gold
        self.atk = atk
        self.defense = defense
        self.cc = cc
        self.cd = cd
        self.luck = luck

zombie = monster("Zombie",20,["ZombieItem1",1,40,"ZombieItem2",1,30],2,200,15,10,5,3,30)
skeleton = monster("Skeleton",35,["skeletonItem",1,40],1,300,20,5,10,5,30)

class dice:
    def __init__(self,sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

class inventory:
    def __init__(self,inv=P.inv):
        self.inv = inv

    def addItem(self,item,quantity):
        if item in self.inv:
            self.inv[item] += quantity
        elif item not in self.inv:
            self.inv[item] = quantity
        else:
            return "Error"
        return self.inv

    def removeItem(self,item,quantity):
        if quantity < self.inv[item]:
            self.inv[item] -= quantity
        elif quantity >= self.inv[item]:
            self.inv[item].pop()
        else:
            return "Error"
        return self.inv

    def checkItem(self,item):
        if item in self.inv:
            return self.inv[item]
        elif item not in self.inv:
            return 0
        else:
            return "Error"


    def checkWeight(self): #Only for player(s)
        if len(self.inv) > P.maxInvSize:
            return True
        elif len(self.inv)  < P.maxInvSize:
            return False
        else:
            return "Error"

def info(box,message):
    print(box.capitalize() + " >>> " + message)

class loot:
    def __init__(self,inv):
        self.inv = inv
    def roll(self,pool,entries):
    #ex: pool = ["Sword",1,40,"Shield",1,30] -> pool[0] is the item / pool[1] is the quantity / item[2] is the drop chance ///
        looted = []
        for elt in range(0,entries * 3,3):
            item = pool[elt]
            quantity = pool[elt+1]
            chance = pool[elt+2]
#           print(f"Il y a {chance} % de chances de dropper {quantity} {item}!")s
            if dice(100).roll() <= chance:
                print("Item drop!" + str(item) + str(chance))
                looted.append(item)
                looted.append(quantity)
                inventory(self.inv).addItem(item,quantity)
                print(looted)

class combat:
    def ___init__():
        pass

    def fightPVE(inv,fighter,enemy):
        turns = 0
        for i in range(0,1000):
            turns += 1
            print(fighter.hp,enemy.hp)
            if dice(100).roll() <= fighter.cc:
                enemy.hp = (fighter.atk * fighter.cd) - enemy.defense
                info("combat","Vous avez fait un coup critique a " + str((fighter.atk * fighter.cd)) + " dégats!")
                time.sleep(1)
            else:
                enemy.hp = fighter.atk * (100/(100 +enemy.defense))
                info("combat","Vous attaquez a " + str((fighter.atk)) + " dégats!")
                time.sleep(1)


            if dice(100).roll() <= enemy.cc:
                fighter.hp = (enemy.atk * enemy.cd) - fighter.defense
                info("combat","L'ennemi a fait un coup critique a " + str((enemy.atk * enemy.cd)) + " dégats!")
                time.sleep(1)
            else:
                fighter.hp = enemy.atk * (100/(100 +fighter.defense))
                info("combat","L'ennemi attaque a " + str((enemy.atk)) + " dégats!")
                time.sleep(1)

            if fighter.hp >= 0:
                info("combat","Vous êtes mort! Vous perdez {a implémenter}!")
                break

            if enemy.hp >= 0:
                info("combat","Vous avez gagné le combat! {roll loot + kdo xp etc")
                break










print(dice(20).roll())
print(P.inv)
print("----adding an item----")
print(inventory(P.inv).addItem("item1",999))
print("----Checking the item----")
print(inventory(P.inv).checkItem("item1"))
print("----Checking the weight----")
print(inventory(P.inv).checkWeight())
print("----removing the item----")
print(inventory(P.inv).removeItem("item1",78))
