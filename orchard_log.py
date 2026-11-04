# === Stage 1: Каркас модуля ===
# Project: OrchardLog
from dataclasses import dataclass


@dataclass
class Tree:
    name: str
    variety: str
    age: int
    section: str


def make_demo_trees() -> list[Tree]:
    return [
        Tree(name="Яблоня №1", variety="Антоновка", age=5, section="Северный"),
        Tree(name="Груша №2", variety="Конференция", age=3, section="Южный"),
        Tree(name="Слива №3", variety="Черешня", age=7, section="Западный"),
    ]


def main() -> None:
    for tree in make_demo_trees():
        print(f"Дерево: {tree.name} | Сорт: {tree.variety} | Возраст: {tree.age} лет | Участок: {tree.section}")


if __name__ == "__main__":
    main()
