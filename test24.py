class hero():

    def __init__(link,name,spell, hp=100):
        link.name = name
        link.spell = spell
        link.hp =hp

    def attack(link):
        print(link.name + " is attacking")

    def punch(link):
         print(link.name + " is punching")