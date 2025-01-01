import pygame
from init.settings import WIDTH, HEIGHT, WHITE, NAME_WINDOW, list_of_buttons_parameters, list_of_start_buttons_parameters
from init.display import Display, Button
from init.GameProces import GameProcess
import sys

class StartGameProc:
    def __init__(self):
        self.Play = True
        self.tick_rate = 30
        self.screen = None
        self.dict_of_buttons: dict[Button, list] = {}
        self.list_of_enter_buttons_functions: list[callable] = [self.next_list_in_menu,
                                                                self.open_options,
                                                                Display.exit_game]
        
        self.list_of_start_buttons_functions: list[callable] = [self.start_game, self.back]
    
    def start_menu(self) -> None:
        """
        отображать главное меню с кнопками одиночная игра, сетевая игра, опции, выход
        """
        # Инициализация Pygame
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen = screen
        pygame.display.set_caption(NAME_WINDOW)
        self.add_buttons(list_of_buttons_parameters, self.list_of_enter_buttons_functions)
        # Главный цикл программы
        while self.Play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Display.exit_game()
                
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for btn in self.dict_of_buttons:
                        if btn.check_for_put(mouse_pos):
                            btn.put = True
                        else:
                            btn.put = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for btn in self.dict_of_buttons:
                        if btn.check_for_put(mouse_pos):
                            btn.is_pressed = True
                            
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for btn in self.dict_of_buttons:
                        if btn.check_for_put(mouse_pos) and btn.is_pressed:
                            btn.is_pressed = False
                            btn.function_btn()
                            
            # Очищаем экран
            self.screen.fill(WHITE)
            
            self.display_objects()
            
            # Обновляем экран
            pygame.display.flip()

            clock.tick(self.tick_rate)
            
    def display_objects(self):
        # Рисуем фон экрана в меню
        Display.draw_screen_font(self.screen, 1)
        # Рисуем кнопку
        for btn in self.dict_of_buttons:
            Display.draw_button(self.screen, btn)
    
    def add_buttons(self, buttons_parameters: list, buttons_functions: list):
        """
        Добавление кнопок на экран
        """
        for list_parameters, function in zip(buttons_parameters, buttons_functions):
            list_parameters.append(function)
            self.dict_of_buttons[Button(*list_parameters)] = list_parameters
            list_parameters.pop()
     
    def go_load_animation(self):
        """
        Запускает анимацию загрузки
        
        Найти или создать анимацию загрузки
        """
        pass
    
    def clear_menu(self):
        """
        Очищает меню
        """
        self.dict_of_buttons: dict[Button, list] = {}

    def back(self):
        """
        Возвращается на меню входа в игру
        """
        self.clear_menu()
        self.add_buttons(list_of_buttons_parameters, self.list_of_enter_buttons_functions)

    def next_list_in_menu(self):
        """
        Переключает на новую страницу после нажатия на Одиночная игра
        """
        self.clear_menu()
        self.add_buttons(list_of_start_buttons_parameters, self.list_of_start_buttons_functions)
    
    def start_game(self):
        """
        Функция вызывающая начало игры
        Смотрит какой персонаж выбран и передаёт его имя в параметры GameProcess
        """
        self.go_load_animation()
        self.clear_menu()
        Game = GameProcess(self.screen, "Nikita")
        Game.game()
    
    @staticmethod
    def open_options():
        """
        Функция отвечающая за опции
        
        разрешение экрана, установить, применить и сохранить для следующего запуска
        
        """
        print("Options")
