# === Stage 7: Текстовый поиск ===
# Project: OrchardLog
def highlight_match(text: str, needle: str, marker: str = "~~") -> str:
    """Возвращает строку text с подсветкой вхождения needle (без учёта регистра)."""
    if not needle:
        return text
    lower_text = text.lower()
    lower_needle = needle.lower()
    result = []
    start = 0
    while True:
        index = lower_text.find(lower_needle, start)
        if index == -1:
            break
        result.append(text[start:index])
        result.append(marker)
        result.append(text[index:index + len(needle)])
        result.append(marker)
        start = index + len(needle)
    result.append(text[start:])
    return "".join(result)


class OrchardSearch:
    """Поиск деревьев по текстовым полям без учёта регистра."""

    TEXT_FIELDS = ("name", "variety", "section")

    def __init__(self, trees):
        self._trees = list(trees)

    def find(self, query: str):
        """Возвращает список деревьев, поля которых содержат query (без учёта регистра)."""
        needle = query.strip()
        if not needle:
            return []
        lowered = needle.lower()
        matches = []
        for tree in self._trees:
            for field in self.TEXT_FIELDS:
                value = getattr(tree, field, "")
                if lowered in str(value).lower():
                    matches.append(tree)
                    break
        return matches

    def render(self, query: str) -> str:
        """Формирует текстовый вывод с подсветкой совпадений в строковых полях."""
        needle = query.strip()
        if not needle:
            return ""
        lines = [f"Поиск: {needle}"]
        matches = self.find(needle)
        if not matches:
            lines.append("Ничего не найдено.")
            return "\n".join(lines)
        for tree in matches:
            rendered = "\n".join(
                f"{field}: {highlight_match(str(getattr(tree, field, '')), needle)}"
                for field in self.TEXT_FIELDS
            )
            lines.append(rendered)
        return "\n".join(lines)


if __name__ == "__main__":
    class Tree:
        def __init__(self, name, variety, section, age):
            self.name = name
            self.variety = variety
            self.section = section
            self.age = age

    demo_trees = [
        Tree("Яблоня", "Антоновка", "Север", 5),
        Tree("Груша", "Конференция", "Юг", 3),
        Tree("Яблоня", "Богатырь", "Запад", 7),
    ]
    searcher = OrchardSearch(demo_trees)
    print(searcher.render("яблоня"))
    print()
    print(searcher.render("БОГАТЫРЬ"))
