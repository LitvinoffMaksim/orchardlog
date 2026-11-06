# === Stage 2: Проверка полей ===
# Project: OrchardLog
from datetime import date


def normalize_text(value):
    text = value.strip()
    if not text:
        raise ValueError("Поле не может быть пустым.")
    return text


def normalize_date(value):
    text = value.strip()
    if not text:
        raise ValueError("Укажите дату в формате ДД.ММ.ГГГГ.")
    parts = text.split(".")
    if len(parts) != 3:
        raise ValueError("Укажите дату в формате ДД.ММ.ГГГГ.")
    day, month, year = parts
    if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
        raise ValueError("Неверные значения дня или месяца.")
    try:
        return date(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Такой даты не существует.")


def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Название должно быть текстом.")
    normalized = normalize_text(name)
    if len(normalized) < 2:
        raise ValueError("Название слишком короткое.")
    if len(normalized) > 50:
        raise ValueError("Название слишком длинное.")
    return normalized


def validate_variety(variety):
    if not isinstance(variety, str):
        raise TypeError("Сорт должен быть текстом.")
    normalized = normalize_text(variety)
    if len(normalized) < 2:
        raise ValueError("Сорт слишком короткий.")
    if len(normalized) > 50:
        raise ValueError("Сорт слишком длинный.")
    return normalized


def validate_age(age):
    normalized = normalize_text(age)
    try:
        value = int(normalized)
    except ValueError:
        raise ValueError("Возраст должен быть целым числом.")
    if value <= 0:
        raise ValueError("Возраст не может быть отрицательным или нулём.")
    if value > 300:
        raise ValueError("Возраст слишком большой.")
    return value


def validate_plot(plot):
    if not isinstance(plot, str):
        raise TypeError("Участок должен быть текстом.")
    normalized = normalize_text(plot)
    if len(normalized) < 2:
        raise ValueError("Участок слишком короткий.")
    if len(normalized) > 50:
        raise ValueError("Участок слишком длинный.")
    return normalized


def validate_tree(name, variety, age, plot):
    return {
        "name": validate_name(name),
        "variety": validate_variety(variety),
        "age": validate_age(age),
        "plot": validate_plot(plot),
    }
