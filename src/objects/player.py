from objects.creature import Creature
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

class Player(Creature):
    """
    Класс игрок
    """
    def __init__(self, start_place: str):
        """
        Инициализация объекта Player
        """
        self.place = start_place

    def move(self, new_place: str):
        """
        Метода перемещающий пользователя в новую локацию
        """
        # Логируем
        logging.info(f"Пользователь переместился на место: {new_place}")
        # Перемещаемся
        self.place = new_place

    def get_current_place(self):
        """
        Метод который возвращает текущее местоположение пользователя
        """
        return self.place
    
    def start_fight(self, entity: Creature):
        """
        Игрок начинает бой
        """
        # Логируем
        logging.info(f"Пользователь начал бой с {entity}")
        # Пошаговый бой
        # награждение
    
    

