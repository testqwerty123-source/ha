from abc import ABC, abstractmethod
import random

class Game(ABC):
    def __init__(self, name, players):
        self.name = name
        self.players = players

    @abstractmethod
    def play(self):
        print(f"\n--- Початок гри '{self.name}' ({self.players} гравців) ---")
        pass
    
    def display_rules(self):
        print(f"Правила для {self.name}: Мета — виграти.")

class Chess(Game):
    def __init__(self):
        super().__init__("Шахи", 2)
        self.board = [[" "]*8 for _ in range(8)]

    def play(self):
        super().play()
        print("-> Налаштування шахової дошки 8x8.")
        print("-> Гра почалася. Білі роблять перший хід (e2-e4).")

class DiceGame(Game):
    def __init__(self, players):
        super().__init__("Гра в кості", players)
    
    def play(self):
        super().play()
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_roll = dice1 + dice2
        print(f"-> Кидаємо кості: {dice1} + {dice2}")
        print(f"-> Результат кидка: **{dice_roll}**.")
        
# --- Виконання ---

chess_game = Chess()
chess_game.display_rules()
chess_game.play()

dice_game = DiceGame(players=4)
dice_game.display_rules()
dice_game.play()
