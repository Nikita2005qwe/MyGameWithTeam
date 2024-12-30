import pygame

class Button:
    def __init__(self, x: int, y: int, w: int, h: int, text: str, font: pygame.font.Font, color: tuple[int],
                 text_color: tuple[int], function: callable):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.font = font
        self.color = color
        self.text_color = text_color
        self.function = function
    
    def check_click(self, mouse_pos) -> bool:
        return self.x <= mouse_pos[0] <= self.x + self.w and self.y <= mouse_pos[1] <= self.y + self.h
    
    def function_btn(self) -> None:
        self.function()

class Display:
    @staticmethod
    def draw_button(screen: pygame.surface.Surface, button: Button) -> None:
        """
        Основная функция для отображения кнопки
        """
        # Рисуем прямоугольник
        pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))
    
        # Создаем поверхность с текстом
        text_surface = button.font.render(button.text, True, button.text_color)
    
        # Определяем координаты для центрирования текста
        text_rect = text_surface.get_rect(center=(button.x + button.w // 2, button.y + button.h // 2))
    
        # Отображаем текст на поверхности
        screen.blit(text_surface, text_rect)
  