import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class Creature:
    """
    Класс существ
    """
    def __init__(self, characteristics: dict[str, int], gold: int, rewarding_exp: int, coords: list[int, int]):
        """
        Класс инициализации существ
        """
        self.characteristics = characteristics
        self.gold = gold
        self.rewarding_exp = rewarding_exp
        self.coords = coords

    def move(self, up: int, right: int):
        """
        Метод перемещающий существо по локации
        """
        self.coords[0] += right * self.characteristics["speed"]
        self.coords[1] += up * self.characteristics["speed"]

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
