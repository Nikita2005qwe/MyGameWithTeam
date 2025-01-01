from init.StartGameProc import StartGameProc


def main() -> None:
    """
    Game Logic - игровая логика, получив спецификацию должен работать как нужно в нашей игре
    Game Proc
    Formal Spec - данные (математическое описание нашей игры) устройства логики мира в некоторой математической нотации
    """
    game = StartGameProc()

    game.start_menu()


if __name__ == "__main__":
    main()
