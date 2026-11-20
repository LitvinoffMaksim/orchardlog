# === Stage 8: Теги ===
# Project: OrchardLog
from __future__ import annotations


class Tag:
    """Идентификатор тега: имя и список деревьев, к нему привязанных."""

    __slots__ = ("name", "_trees")

    def __init__(self, name: str) -> None:
        self.name = name
        self._trees: dict[str, "Tree"] = {}

    def add(self, tree: "Tree") -> None:
        self._trees[tree.name] = tree

    def remove(self, tree: "Tree") -> None:
        self._trees.pop(tree.name, None)

    def contains(self, tree: "Tree") -> bool:
        return tree.name in self._trees

    def trees(self) -> list["Tree"]:
        return list(self._trees.values())


class TagIndex:
    """Индекс тегов для дерева: добавление, удаление и поиск по тегу."""

    def __init__(self, tree: "Tree") -> None:
        self.tree = tree
        self.tags: dict[Tag, None] = {}

    def add(self, name: str) -> Tag:
        tag = self.tags.get(Tag(name))
        if tag is None:
            tag = Tag(name)
            self.tags[name] = tag
        tag.add(self.tree)
        return tag

    def remove(self, name: str) -> None:
        tag = self.tags.get(name)
        if tag is not None:
            tag.remove(self.tree)
            if not tag.trees():
                del self.tags[name]

    def search(self, name: str) -> list[Tag]:
        return [tag for tag in self.tags.values() if tag.name == name]

    def has(self, name: str) -> bool:
        return name in self.tags


class Tree:
    """Дерево с именем, сортом, возрастом, участком и индексом тегов."""

    def __init__(self, name: str, variety: str, age: int, plot: str) -> None:
        self.name = name
        self.variety = variety
        self.age = age
        self.plot = plot
        self.tags = TagIndex(self)

    def tag_names(self) -> list[str]:
        return list(self.tags.tags.keys())
