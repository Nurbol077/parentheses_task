from functools import lru_cache


# Мемоизация для ускорения работы
@lru_cache(None)
def countWellFormedParenthesis(nCouples: int) -> int:
    # Проверка на отрицательное значение
    if nCouples < 0:
        raise ValueError("Количество пар скобок не может быть отрицательным")

    # Базовый случай: для 0 пар скобок
    if nCouples == 0:
        return 1

    result = 0
    for i in range(nCouples):
        left = countWellFormedParenthesis(i)
        right = countWellFormedParenthesis(nCouples - 1 - i)
        result += left * right

    return result