import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class Creature:
    """
    Класс существ
    """
    def __init__(self, gold: int, rewarding_exp: int):
        """
        Класс инициализации существ
        """
        self.gold = gold
        self.rewarding_exp = rewarding_exp
        
    #def move(self):


class CreatureLogic:
    @staticmethod
    def create_creator(entity, **kwargs) -> Creature:
        """
        Метод создаёт объекты типа Creature
        логирует в консоли создание объектов
        """
        # Создаём
        obj_entity = entity(**kwargs)
        # Логируем
        logging.info(f"{obj_entity} Создан")
        return obj_entity
