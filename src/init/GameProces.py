from init.processing_of_living_entities.entities.CreatureLogic import Creature, CreatureLogic
from init.processing_of_living_entities.entities.PlayerLogic import PlayerLogic, Player
from init.processing_of_living_entities.entities.player_level_table.json_function import read_inf
from init.settings import WHITE
from init.display import Display, Button
import pygame


class GameProcess:
    def __init__(self, screen: pygame.surface.Surface, name: str):
        self.tick_rate = 30
        self.screen = screen
        self.player = self.player_preparation(name)
        self.MOVING_UP = False
        self.MOVING_DOWN = False
        self.MOVING_LEFT = False
        self.MOVING_RIGHT = False
    
    @staticmethod
    def player_preparation(name: str):
        """
        Подготовка для игры
        Инициализация игрока и карты
        """
        data_players_dict: dict[str, dict] = read_inf("init/processing_of_living_entities/entities/data_player/data_player.json")
        data_player_dict: dict[str, str | int] = data_players_dict[name]
        start_place = data_player_dict["start_place"]
        player_gold = data_player_dict["gold"]
        player_experience = data_player_dict["experience"]
        player_coords = data_player_dict["coords"]
        player_characteristics = data_player_dict["characteristics"]
        player = CreatureLogic.create_creator(entity=Player, start_place=start_place,
                                              characteristics=player_characteristics,
                                              gold=player_gold, experience=player_experience,
                                              coords=player_coords)
        return player

    
    def game(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.MOVING_UP = True
                    elif event.key == pygame.K_s:
                        self.MOVING_DOWN = True
                    elif event.key == pygame.K_a:
                        self.MOVING_LEFT = True
                    elif event.key == pygame.K_d:
                        self.MOVING_RIGHT = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.MOVING_UP = False
                    elif event.key == pygame.K_s:
                        self.MOVING_DOWN = False
                    elif event.key == pygame.K_a:
                        self.MOVING_LEFT = False
                    elif event.key == pygame.K_d:
                        self.MOVING_RIGHT = False
            # Очищаем экран
            self.screen.fill(WHITE)
    
            #self.display_objects(screen)
            # Движение персонажа
            if self.MOVING_UP:
                self.player.move(1, 0)
                print(self.player.coords)
            if self.MOVING_DOWN:
                self.player.move(-1, 0)
                print(self.player.coords)
            if self.MOVING_LEFT:
                self.player.move(0, -1)
                print(self.player.coords)
            if self.MOVING_RIGHT:
                self.player.move(0, 1)
                print(self.player.coords)
            # Обновляем экран
            pygame.display.flip()
    
            clock.tick(self.tick_rate)
            