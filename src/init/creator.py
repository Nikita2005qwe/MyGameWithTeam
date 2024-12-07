from objects.creature import Creature
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class Creator:
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
