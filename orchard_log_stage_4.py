# === Stage 4: Удаление и восстановление ===
# Project: OrchardLog
from datetime import datetime


class Tree:
    def __init__(self, name, variety, age, section):
        self.id = None
        self.name = name
        self.variety = variety
        self.age = age
        self.section = section
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.now().isoformat()

    def restore(self):
        self.deleted = False
        self.deleted_at = None


class Orchard:
    def __init__(self):
        self._trees = {}
        self._counter = 0

    def add_tree(self, tree):
        self._counter += 1
        tree.id = self._counter
        self._trees[tree.id] = tree
        return tree

    def get_tree(self, tree_id):
        return self._trees.get(tree_id)

    def delete_tree(self, tree_id):
        tree = self._trees.get(tree_id)
        if tree is not None:
            tree.soft_delete()
            return True
        return False

    def restore_tree(self, tree_id):
        tree = self._trees.get(tree_id)
        if tree is not None:
            tree.restore()
            return True
        return False

    def list_trees(self):
        return [t for t in self._trees.values() if not t.deleted]

    def list_deleted_trees(self):
        return [t for t in self._trees.values() if t.deleted]
