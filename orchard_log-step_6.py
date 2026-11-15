# === Stage 6: Фильтрация записей ===
# Project: OrchardLog
from dataclasses import dataclass, field
from datetime import date


@dataclass
class OrchardEntry:
    """Запись о работе в саду."""
    date: date
    tree_name: str
    variety: str
    notes: str = ""
    tags: list = field(default_factory=list)


class OrchardLog:
    def __init__(self):
        self.entries: list = []

    def add(self, date, tree_name, variety, notes="", tags=None):
        entry = OrchardEntry(
            date=date,
            tree_name=tree_name,
            variety=variety,
            notes=notes,
            tags=tags or [],
        )
        self.entries.append(entry)
        return entry

    def sort_by_date(self):
        self.entries.sort(key=lambda e: e.date)
        return self.entries

    def filter_by_variety(self, variety):
        return [e for e in self.entries if e.variety == variety]

    def filter_by_date_range(self, start, end):
        return [e for e in self.entries if start <= e.date <= end]

    def filter_by_variety_and_date_range(self, variety, start, end):
        return [
            e
            for e in self.entries
            if e.variety == variety and start <= e.date <= end
        ]
