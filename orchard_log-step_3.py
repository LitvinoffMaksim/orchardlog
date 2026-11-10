# === Stage 3: Хранилище в памяти ===
# Project: OrchardLog
from datetime import date


class OrchardError(Exception):
    """Общая ошибка модуля хранилища деревьев."""


class TreeNotFoundError(OrchardError):
    """Дерево с указанным идентификатором не найдено."""


class Tree:
    def __init__(self, tree_id, name, variety, age, section):
        self.tree_id = tree_id
        self.name = name
        self.variety = variety
        self.age = age
        self.section = section

    def __repr__(self):
        return (
            f"Tree(tree_id={self.tree_id!r}, name={self.name!r}, "
            f"variety={self.variety!r}, age={self.age!r}, "
            f"section={self.section!r})"
        )


class TreeStore:
    def __init__(self):
        self._trees = {}

    def add(self, tree):
        if not isinstance(tree, Tree):
            raise OrchardError("Добавлено не дерево")
        if tree.tree_id in self._trees:
            raise OrchardError(f"Дерево {tree.tree_id!r} уже существует")
        self._trees[tree.tree_id] = tree

    def get(self, tree_id):
        if tree_id not in self._trees:
            raise TreeNotFoundError(f"Дерево {tree_id!r} не найдено")
        return self._trees[tree_id]

    def list_trees(self):
        return list(self._trees.values())


if __name__ == "__main__":
    store = TreeStore()

    apple_tree = Tree(
        tree_id=1,
        name="Яблоня у калитки",
        variety="Боровинка",
        age=date(2021, 10, 15),
        section="Северный",
    )
    pear_tree = Tree(
        tree_id=2,
        name="Груша в углу",
        variety="Конференция",
        age=date(2019, 5, 20),
        section="Западный",
    )

    store.add(apple_tree)
    store.add(pear_tree)

    print("Все деревья:")
    for tree in store.list_trees():
        print(f"  {tree.name} ({tree.variety}), участок {tree.section}")

    print("Дерево 1:")
    print("  ", store.get(1))

    print("Дерево 3:")
    try:
        store.get(3)
    except TreeNotFoundError as error:
        print("  ", error)
