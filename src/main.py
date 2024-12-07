from objects.creature import Creature
from objects.player import Player
from init.creator import Creator


def main() -> None:
    """
    Game Logic - игровая логика, получив спецификацию должен работать как нужно в нашей игре
    Game Proc
    Formal Spec - данные (математическое описание нашей игры) устройства логики мира в некоторой математической нотации
    """
    start_place = "город"
    creat = Creator.create_creator(entity=Creature)
    player = Creator.create_creator(entity=Player, start_place = start_place)
    player.move("деревня")
    print("Hello, world!")


if __name__ == "__main__":
    main()
