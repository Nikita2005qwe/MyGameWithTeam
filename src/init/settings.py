# Настройки окна
WIDTH, HEIGHT = 640, 480

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BASE_COLOUR_FOR_BUTTON = (0, 0, 0, 0)

NAME_WINDOW = "test_window"

# Задать размер и расположение кнопок на главном меню
my_font = (None, 36)
scale: float = 141 / 333
size: int = 240
interval_between_buttons: int = 10
y_for_btn_0: int = 130
x_for_btn_0: int = 40


def calculate_btn_coords_y(index_button: int) -> int:
    """
    Считает координату y по вводимому индексу кнопки
    """
    return y_for_btn_0 + index_button * (size * scale + interval_between_buttons)


list_parameters_for_btn_start = [x_for_btn_0, calculate_btn_coords_y(0),
                                 size, size * scale,
                                 "Одиночная\nигра", "init/img/btns/btn1",
                                 my_font, BASE_COLOUR_FOR_BUTTON, BLACK]

list_parameters_for_btn_options = [x_for_btn_0, calculate_btn_coords_y(1),
                                   size, size * scale,
                                   "Опции", "init/img/btns/btn1",
                                   my_font, BASE_COLOUR_FOR_BUTTON, BLACK]

list_parameters_for_btn_exit = [x_for_btn_0, calculate_btn_coords_y(2),
                                size, size * scale,
                                "Выход", "init/img/btns/btn1",
                                my_font, BASE_COLOUR_FOR_BUTTON, BLACK]

list_of_buttons_parameters = [list_parameters_for_btn_start, list_parameters_for_btn_options,
                              list_parameters_for_btn_exit]

list_parameters_for_btn_enter_world = [x_for_btn_0, calculate_btn_coords_y(0),
                                       size, size * scale,
                                       "Войти в мир", "init/img/btns/btn1",
                                       my_font, BASE_COLOUR_FOR_BUTTON, BLACK]
list_parameters_for_btn_back = [x_for_btn_0, calculate_btn_coords_y(1),
                                size, size * scale,
                                "Назад", "init/img/btns/btn1",
                                my_font, BASE_COLOUR_FOR_BUTTON, BLACK]

list_of_start_buttons_parameters = [list_parameters_for_btn_enter_world, list_parameters_for_btn_back]
