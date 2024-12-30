import pygame
from init.settings import WIDTH, HEIGHT, WHITE, BLACK, RED, GREEN, NAME_WINDOW
from init.display import Display, Button

class GameProc:
    def __init__(self):
        self.Play = True
        self.tick_rate = 30
        self.dict_of_buttons: dict[Button, list] = {}
    
    def start_menu(self) -> int:
        """
        отображать главное меню с кнопками одиночная игра, сетевая игра, опции, выход
        """
        # Инициализация Pygame
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(NAME_WINDOW)
        self.add_start_buttons()
        # Главный цикл программы
        while self.Play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameProc.exit_game()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for btn in self.dict_of_buttons:
                        if btn.check_click(mouse_pos):
                            btn.function_btn()
                            if btn.text == "Выход":
                                return 0
    
            # Очищаем экран
            screen.fill(WHITE)
            
            self.display_objects(screen)
            
            # Обновляем экран
            pygame.display.flip()
    
    
    def display_objects(self, screen: pygame.surface.Surface):
        # Рисуем кнопку
        for btn in self.dict_of_buttons:
            Display.draw_button(screen, btn)
    
    def add_start_buttons(self):
        # Шрифт для текста на кнопке
        font = pygame.font.Font(None, 36)
        list_parameters = [300, 350, 100, 80, "Выход", font, GREEN, BLACK, GameProc.exit_game]
        self.dict_of_buttons[Button(*list_parameters)] = list_parameters
    
    @staticmethod
    def print_hello():
        print("Hello, world!")
    
    @staticmethod
    def exit_game():
        print("Программа завершила выполнение")
        
        pygame.display.flip()
        # Завершение работы Pygame
        pygame.quit()

    @staticmethod
    def function_btn():
        print("Кнопка нажата!")
    
    def update(self):
        pass
    