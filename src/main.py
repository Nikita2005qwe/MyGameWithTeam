from init.processing_of_living_entities.entities.CreatureLogic import Creature, CreatureLogic
from init.processing_of_living_entities.entities.PlayerLogic import PlayerLogic, Player
from init.GameProc import GameProc


def main() -> None:
    """
    Game Logic - игровая логика, получив спецификацию должен работать как нужно в нашей игре
    Game Proc
    Formal Spec - данные (математическое описание нашей игры) устройства логики мира в некоторой математической нотации
    """
    start_place = "город"
    creat = CreatureLogic.create_creator(entity=Creature, gold=10, rewarding_exp=5)
    player = CreatureLogic.create_creator(entity=Player, start_place=start_place, gold=0, experience=0)
    player.move("деревня")
    exp = 10
    print(f"Текущий опыт: {exp}")
    PlayerLogic.add_experience(player, exp)
    print(f"До следующего уровня: {player.exp_for_lvl_up}")
    print("Hello, world!")

    game = GameProc()

    game.start_menu()


if __name__ == "__main__":
    main()
