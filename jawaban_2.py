import random
#Marvin Gideon Purba
#13323062
# Class Robot
class Robot:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    def attack(self, opponent):
        damage = random.randint(5, self.__attack_power)
        opponent.__take_damage(damage)
        print(f"{self.__name} attacks {opponent.name} for {damage} damage!")

    def __take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def is_defeated(self):
        return self.__health == 0

# Class Battle
class Battle:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start_fight(self):
        print("Battle Start!")
        while not self.robot1.is_defeated() and not self.robot2.is_defeated():
            self.robot1.attack(self.robot2)
            if self.robot2.is_defeated():
                print(f"{self.robot2.name} is defeated!")
                print(f"{self.robot1.name} wins!")
                break
            self.robot2.attack(self.robot1)
            if self.robot1.is_defeated():
                print(f"{self.robot1.name} is defeated!")
                print(f"{self.robot2.name} wins!")
                break

# Class Game
class Game:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def start_game(self):
        print("Choose robots for the battle:")
        for i, robot in enumerate(self.robots, start=1):
            print(f"{i}. {robot.name}")
        
        # Memilih dua robot untuk bertarung
        choice1 = int(input("Select the first robot: ")) - 1
        choice2 = int(input("Select the second robot: ")) - 1
        
        robot1 = self.robots[choice1]
        robot2 = self.robots[choice2]
        
        # Memulai pertarungan
        battle = Battle(robot1, robot2)
        battle.start_fight()

# Uji Program
if __name__ == "__main__":
    game = Game()

    # Membuat beberapa objek Robot dengan berbagai atribut
    robot1 = Robot("RoboOne", 100, 30)
    robot2 = Robot("RoboTwo", 100, 25)
    robot3 = Robot("RoboThree", 100, 35)

    # Menambahkan robot-robot tersebut ke dalam game
    game.add_robot(robot1)
    game.add_robot(robot2)
    game.add_robot(robot3)

    # Memulai game
    game.start_game()
