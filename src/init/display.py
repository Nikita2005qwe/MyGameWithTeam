from init.settings import WIDTH, HEIGHT, WHITE, BASE_COLOUR_FOR_BUTTON
import pygame
import sys

class Button:
    def __init__(self, x: int, y: int, w: int, h: int, text: str, path_to_picture: str,
                 font: tuple[str, int], color: tuple[int], text_color: tuple[int], function: callable):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.put = False
        self.is_pressed = False
        self.text = text
        self.font = pygame.font.Font(*font)
        self.color = color
        self.text_color = text_color
        self.picture = path_to_picture
        self.function = function
    
    def check_for_put(self, mouse_pos) -> bool:
        return self.x <= mouse_pos[0] <= self.x + self.w and self.y <= mouse_pos[1] <= self.y + self.h
    
    def function_btn(self) -> None:
        self.function()

class Display:
    @staticmethod
    def draw_screen_font(screen: pygame.surface.Surface, number_font: int) -> None:
        """
        Функция для отрисовки фона в главном меню
        """
        # Рисуем прямоугольник
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
        image = pygame.image.load(f"init/img/menu_font/menu{number_font}.jpg")
        scaled_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(scaled_image, (0, 0))

    @staticmethod
    def draw_button(screen: pygame.surface.Surface, button: Button) -> None:
        """
        Основная функция для отображения кнопки
        """
        # Рисуем прямоугольник
        #pygame.draw.rect(screen, color=BASE_COLOUR_FOR_BUTTON, rect=(button.x, button.y, button.w, button.h))

        # Создание полупрозрачной поверхности
        transparent_surface = pygame.Surface((button.w, button.h), pygame.SRCALPHA)
        transparent_surface.fill(button.color)

        # Отображение полупрозрачного прямоугольника
        screen.blit(transparent_surface, (button.x, button.y))
        
        # Загрузка изображения
        if button.picture is not None:
            if button.put:
                image = pygame.image.load(button.picture + "_put.png")
            else:
                image = pygame.image.load(button.picture + "_neutral.png")
            if button.is_pressed:
                image = pygame.image.load(button.picture + "_pressed.png")
            scaled_image = pygame.transform.scale(image, (button.w, button.h))
            screen.blit(scaled_image, (button.x, button.y))

        # Создаем поверхность с текстом
        text_surface = button.font.render(button.text, True, button.text_color)
    
        # Определяем координаты для центрирования текста
        text_rect = text_surface.get_rect(center=(button.x + button.w // 2, button.y + button.h // 2))
    
        # Отображаем текст на поверхности
        screen.blit(text_surface, text_rect)

    @staticmethod
    def exit_game():
        print("Программа завершила выполнение")
        # Завершение работы Pygame
        pygame.quit()
        sys.exit()
  