import random

class Entity:
    def __init__(self, name, hp, damage):
        self.name = name
        self.Player_class = Player_class
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
    def attack(self, target):
            print(f"{self.name} атакував {target.name}...")
            target.taken_damage(self.damage)
    def taken_damage(self, taken_damage):
        self.hp -= taken_damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} отримав {taken_damage} шкоди. Залишилося {self.hp} життя!")

class Enemy(Entity):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        super().__init__(name, hp, damage)
    def drop_Item(self):
        chance = random.randint(1, 100)
        item_counter = 0
        if chance < 5:
            item_counter = 3
        elif chance < 25:
            item_counter = 2
        elif chance < 50:
            item_counter = 1
        if item_counter > 0:

            print(f" оГо ВаМ ВиПаЛо {item_counter} ШТуК!")
            for i in range (item_counter):
                class_Item = random.randint(0, 1)
                if class_Item == 0:
                    dropped_Item = random.choice(list_of_weapon)
                else:
                    dropped_Item = random.choice(list_of_armor)
                print(f"ВаШа ШТуКеНЦія: {dropped_Item.name}!\n"
                      f"\tБонусна шкода: {dropped_Item.bonus_damage}\n"
                      f"\tБонусна броня: {dropped_Item.bonus_armor}\n"
                      f"\tБонусе хп: {dropped_Item.bonus_hp}\n"
                      f"ВЗяТи(1) чи ПЛюНУТи (КЛаЦай Шо ХоЧеШ)? ")
                user_answer = input("ВиБиРай( 1 чи 2):")
                if user_answer == 1:
                    my_hero.equip_weapon(dropped_Item) if class_Item == 0 else my_hero.equip_armor(dropped_Item)
                else:
                    print("у ВаС ДіРяВі РуКи {dropped_Item.name}")

class Player(Entity):
    def __init__(self, name, Player_class, maxhp, damage):
        self.name = name
        self.Player_class = Player_class
        self.hp = maxhp
        self.max_hp = maxhp
        self.weapon = None
        self.armor = None
        self.accessories = None
        self.damage = damage
    def Player_info(self):
        print(f"--{self.name}--\n"
              f"клас:{self.Player_class}\n"
              f"життя{self.hp}\n"
              f"шкода{self.damage}\n")
    def equip_weapon(self, item):
        if item.item_class != self.Player_class:
            print(f"Ти Що ЗаБуВ ХТо Ти, Це Не ТоБі {item.name}")
            return
        self.weapon = item
        self.damage += item.bonus_damage
        print(f"у ТеБе ТеПеР є Ця ШТуКеНЦія - {item.
              name}")
    def equip_armor(self, Item):
        if Item.item_class != self.Player_class:
            print(f"Ти Що ЗаБуВ ХТо Ти, Це Не ТоБі {Item.name}")
            return
        self.armor = Item
        self.max_hp += Item.bonus_hp
        self.armor += Item.bonus_armor
        print(f"у ТеБе ТеПеР є Ця ШТуКеНЦія - {Item.name}, ВаШе хп СТаЛо оГо На {Item.bonus_hp} ВаШа БРоНя ЗБіЛьШиЛаСя На {Item.bonus_armor} ")
    def equip_accessories(self, Item):
         self.armor = Item.armor
         self.max_hp += Item.bonus_hp
         self.damage += Item.bonus_damage
         self.accessories = Item
    def healing(self, procent):
        heal = (self.max_hp/100) * procent
        if self.hp + heal > self.max_hp:
            self.hp = self.max_hp
            print(f" Ти ЖиВий РаДій, Чи ТеБе ВБиТИ?")
        else:
            self.hp += heal
            print(f" Ти ЖиВий СВій {heal} хп! Ти ЖиВий На {self.hp} а Не На {self.max_hp} ")

class Item:
    def __init__(self, name, item_class, bonus_damage, bonus_hp, bonus_armor):
        self.name = name
        self.item_class = item_class
        self.bonus_damage = bonus_damage
        self.bonus_hp = bonus_hp
        self.bonus_armor = bonus_armor



list_of_enemy = [
    Enemy("Rat", 20, 3),
    Enemy("Wild Rat", 25, 4),
    Enemy("Cave Bat", 22, 4),
    Enemy("Small Spider", 18, 5),
    Enemy("Goblin", 30, 6),
    Enemy("Goblin Scout", 35, 7),
    Enemy("Forest Snake", 28, 6),
    Enemy("Angry Wolf", 40, 8),
    Enemy("Bandit", 45, 9),
    Enemy("Bandit Archer", 35, 10),

    Enemy("Skeleton", 50, 9),
    Enemy("Zombie", 60, 7),
    Enemy("Dark Bat", 38, 8),
    Enemy("Poison Spider", 35, 11),
    Enemy("Orc Grunt", 70, 10),
    Enemy("Orc Raider", 75, 11),
    Enemy("Wild Boar", 65, 9),
    Enemy("Cave Lizard", 55, 10),
    Enemy("Thief", 40, 12),
    Enemy("Dark Mage Apprentice", 50, 13),

    Enemy("Orc Warrior", 85, 12),
    Enemy("Orc Archer", 70, 13),
    Enemy("Stone Golem", 120, 8),
    Enemy("Ice Wolf", 90, 14),
    Enemy("Fire Imp", 60, 15),
    Enemy("Shadow Thief", 75, 16),
    Enemy("Dark Knight", 110, 14),
    Enemy("Skeleton Captain", 100, 13),
    Enemy("Zombie Brute", 130, 11),
    Enemy("Swamp Monster", 140, 12),

    Enemy("Boss Goblin King", 180, 18),
    Enemy("Boss Orc Chief", 220, 20),
    Enemy("Boss Giant Spider", 160, 22),
    Enemy("Boss Dark Mage", 150, 25),
    Enemy("Boss Stone Titan", 300, 15),

    Enemy("Fire Elemental", 120, 18),
    Enemy("Ice Elemental", 110, 17),
    Enemy("Thunder Spirit", 100, 20),
    Enemy("Shadow Beast", 140, 19),
    Enemy("Cursed Knight", 150, 18),

    Enemy("Boss Dragon Whelp", 200, 24),
    Enemy("Boss Ancient Golem", 280, 20),
    Enemy("Boss Vampire Lord", 170, 26),
    Enemy("Boss Demon Brute", 260, 22),
    Enemy("Boss Lich King", 190, 27),

    Enemy("Dark Assassin", 95, 21),
    Enemy("War Troll", 160, 16),
    Enemy("Cave Ogre", 180, 17),
    Enemy("Ghost Warrior", 120, 18),
    Enemy("Boss Shadow Dragon", 350, 30)
]
list_of_weapon = [
    Item("Rusty Sword", "Воїн", 6, 0, 0),
    Item("Iron Sword", "Воїн", 9, 0, 0),
    Item("Steel Sword", "Воїн", 12, 0, 0),
    Item("Battle Axe", "Воїн", 15, 0, 0),
    Item("Dragon Slayer", "Воїн", 20, 0, 0),

    Item("Heavy Mace", "Захисник", 6, 0, 0),
    Item("War Hammer", "Захисник", 8, 0, 0),
    Item("Guardian Hammer", "Захисник", 10, 0, 0),
    Item("Titan Hammer", "Захисник", 12, 0, 0),
    Item("Fortress Breaker", "Захисник", 15, 0, 0),

    Item("Pitchfork", "Фермер", 5, 0, 0),
    Item("Iron Pitchfork", "Фермер", 7, 0, 0),
    Item("Harvest Scythe", "Фермер", 9, 0, 0),
    Item("Golden Scythe", "Фермер", 12, 0, 0),
    Item("Legendary Farmer Scythe", "Фермер", 15, 0, 0),

    Item("Wooden Staff", "Чарівник", 8, 0, 0),
    Item("Magic Staff", "Чарівник", 12, 0, 0),
    Item("Crystal Wand", "Чарівник", 15, 0, 0),
    Item("Arcane Staff", "Чарівник", 18, 0, 0),
    Item("Ancient Mage Staff", "Чарівник", 22, 0, 0)
]
list_of_armor = [
    Item("Leather Armor", "Воїн", 0, 25, 6),
    Item("Iron Armor", "Воїн", 0, 35, 8),
    Item("Steel Armor", "Воїн", 0, 45, 10),
    Item("Knight Armor", "Воїн", 0, 60, 14),
    Item("Dragon Scale Armor", "Воїн", 0, 80, 18),

    Item("Wooden Shield Armor", "Захисник", 0, 50, 15),
    Item("Guardian Plate", "Захисник", 0, 70, 18),
    Item("Heavy Defender Armor", "Захисник", 0, 90, 22),
    Item("Fortress Armor", "Захисник", 0, 120, 26),
    Item("Titan Defender Armor", "Захисник", 0, 150, 30),

    Item("Farmer Jacket", "Фермер", 0, 40, 5),
    Item("Thick Farmer Coat", "Фермер", 0, 60, 7),
    Item("Village Guard Coat", "Фермер", 0, 80, 9),
    Item("Harvest Protector", "Фермер", 0, 110, 12),
    Item("Golden Harvest Armor", "Фермер", 0, 150, 15),

    Item("Cloth Robe", "Чарівник", 0, 15, 3),
    Item("Magic Robe", "Чарівник", 0, 20, 4),
    Item("Enchanted Robe", "Чарівник", 0, 30, 5),
    Item("Archmage Robe", "Чарівник", 0, 40, 6),
    Item("Ancient Arcane Robe", "Чарівник", 0, 55, 8)
]
list_of_accessories = [
    Item("Сталеве Кільце", "Universal", 0, 0, 15),
    Item("Медальйон Сили", "Universal", 20, 0, 0),
    Item("Пояс Витривалості", "Universal", 0, 50, 0),
    Item("Рубіновий Кулон", "Universal", 0, 100, 0),
    Item("Заточений Камінь", "Universal", 15, 0, 0),
    Item("Пластинчасті Наручі", "Universal", 0, 0, 25),
    Item("Намисто Регенерації", "Universal", 0, 30, 5),
    Item("Важкий Наплічник", "Universal", -5, 0, 40),
    Item("Еліксир Люті", "Universal", 35, -20, 0),
    Item("Брошка Охоронця", "Universal", 0, 30, 10),
    Item("Кристал Стійкості", "Universal", 0, 150, 0),
    Item("Бойовий Прапор", "Universal", 18, 0, 0),
    Item("Рукавиці Майстра", "Universal", 12, 0, 8),
    Item("Підкова Удачі", "Universal", 10, 20, 5),
    Item("Залізний Ланцюг", "Universal", 0, 0, 18),
    Item("Гравійована Пряжка", "Universal", 7, 0, 7),
    Item("Серце Велетня", "Universal", 0, 250, 0),
    Item("Стародавня Руна", "Universal", 45, 0, 0),
    Item("Шипований Пояс", "Universal", 10, 0, 10),
    Item("Сфера Гармонії", "Universal", 15, 50, 15)
]


def fight_with_enemy():
    enemy = random.choice(list_of_enemy)

    print(f"уВаГа! На Вас НаПаЛи {enemy.name}")

    while True:
        print("\n\n")
        my_hero.attack(enemy)
        if enemy.hp <= 0:
            print(f"{enemy.name} Ви йоГо ПеРеМоГЛи!")
            enemy.drop_Item()
            break

        print("\n\n")

        enemy.attack(my_hero)
        if my_hero.hp <= 0:
            print(f"{my_hero.name} Ви ЗДоХЛи ВіД {enemy.name}!")
            break
def WoW_found_a_tresure ():
    my_chance = random.randint(1, 100)

    if my_chance <= 20:
        user_choice = input("оГо Ви ЗНайШЛи ВеЛиЧеЗНу КаКуЛьКу ДаВайТе її ВіДКРиїМо"
                            "ВіДКРиТи(1) Чиии ВіДКРиТи(2)")

        if user_choice == 2:
            print("а ЧоГо Не 1?")
        if user_choice == 1:
            print("а ЧоГо Не 2?")
            treasure = random.choice(list_of_accessories)
            print(f"ВаШа ШТуКеНЦія: {treasure.name}!\n"
                  f"\tБонусна шкода: {treasure.bonus_damage}\n"
                  f"\tБонусна броня: {treasure.bonus_armor}\n"
                  f"\tБонусе хп: {treasure.bonus_hp}\n"
                  f"ВЗяТи(1) чи ПЛюНУТи (КЛаЦай Шо ХоЧеШ)? ")
            user_answer = input()
            if user_answer == "1":
                my_hero.equip_accessories(treasure)
            else:
                return

    elif my_chance <= 40:
        pass
    elif my_chance <= 60:
        pass
    elif my_chance <= 80:
        pass


print("Вітаюмо вас у світі ТЦКулька \nДавайте створимо ваш аватар!")
Player_name = input("ведіть ім'я вашого аватара:")
print(f"Чудовий вибір {Player_name}")

# Мій ЧуБаПеЛіК
my_hero = None
while my_hero is None:


    Player_class = input("оберіть ваш клас. Введіть цифру. щоб підтвердити вибір:\n"
                         "1) Воїн(100 hp, 10 шкоди)\n"
                         "2) Захисник(200 hp,5 шкоди)\n "
                         "3) Фермер(300 hp,4 шкоди)\n "
                         "4) Чарівник(75 hp,15 шкоди)\n ")

    if Player_class == "1":
        my_hero = Player(Player_name, "Воїн", 100, 10)
    elif Player_class == "2":
        my_hero = Player(Player_name, "Захисник", 200, 5)
    elif Player_class == "3":
        my_hero = Player(Player_name, "Фермер", 300, 4)
    elif Player_class == "4":
        my_hero = Player(Player_name, "Чарівник", 75, 15)
    else:
        print("Будь ласка, зроьвить правельний вибір")

weapon = random.choice(list_of_weapon)
armor = random.choice(list_of_armor)
my_hero.Player_info()
my_hero.equip_weapon(weapon)
my_hero.equip_armor(armor)
my_hero.Player_info()
input()

situation_list = ["ворог", "відпочинок", "скарб"]
while my_hero.hp > 0:
    situation = random.choice(situation_list)
    if situation == "ворог":
        fight_with_enemy()
    elif situation == "відпочинок":
        my_hero.healing(random.randint(20, 80))
    elif situation == "скарб":
        WoW_found_a_tresure()
    input("Для наступного кроку натисніть Ентер!")