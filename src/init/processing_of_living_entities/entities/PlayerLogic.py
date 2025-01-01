from init.processing_of_living_entities.entities.player_level_table.json_function import read_inf
from init.processing_of_living_entities.entities.CreatureLogic import Creature
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class Player(Creature):
    """
    Класс игрок
    """
    def __init__(self, start_place: str, characteristics: dict[str, int], gold: int, experience: int, coords: list[int, int]):
        """
        Инициализация объекта Player
        """
        super().__init__(characteristics, gold, 0, coords)
        self.current_place = start_place
        self.experience = experience
        self.exp_for_lvl_up = None
        self.level_experience = PlayerLogic.get_level(self)
    
    def add_experience(self, exp) -> bool:
        self.experience += exp
        new_level = PlayerLogic.get_level(self)
        if self.level_experience != new_level:
            self.level_experience = new_level
            return True
        return False
    
    def get_current_place(self):
        """
        Метод который возвращает текущее местоположение пользователя
        """
        return self.current_place
    
    def start_fight(self, entity: Creature):
        """
        Игрок начинает бой
        """
        # Логируем
        logging.info(f"Пользователь начал бой с {entity}")
        # Пошаговый бой
        # награждение


class PlayerLogic:
    @staticmethod
    def add_experience(person: Player, exp: int):
        if person.add_experience(exp):
            logging.info(f"Уровень пользователя повышен до {person.level_experience}")
    
    @staticmethod
    def get_level(person: Player):
        """
        Метод вызываемый после получения опыта
        Повышает уровень игрока
        """
        # Лист с уровнями
        level_list: dict[str, int] = read_inf("init/processing_of_living_entities/entities/player_level_table/player_level_table.json")
        for num_level in level_list:
            difference_in_exp = level_list[num_level] - person.experience
            if difference_in_exp > 0:
                person.exp_for_lvl_up = difference_in_exp
                return num_level
        else:
            person.exp_for_lvl_up = 0
            return "10_level"
    
    def add_gold(self, amount):
        pass

