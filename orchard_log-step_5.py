# === Stage 5: Генерация идентификаторов ===
# Project: OrchardLog
import re
from datetime import datetime


PROJECT_PREFIX = "orchardlog"


def sanitize(value):
    if value is None:
        return ""
    return re.sub(r"[^0-9a-zA-Z._-]+", "_", str(value)).strip("_")


def make_unique(base, counter):
    unique = base
    suffix = 0
    while not is_available(unique, counter):
        suffix += 1
        unique = f"{base}-{sanitize(suffix)}"
    return unique


def is_available(candidate, counter):
    for key, value in counter.items():
        if value == candidate:
            return False
    return True


def generate_id(name, counter):
    base = f"{PROJECT_PREFIX}:{sanitize(name)}"
    return make_unique(base, counter)


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
