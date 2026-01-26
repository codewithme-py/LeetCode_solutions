from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Возвращает индексы двух чисел из nums, сумма которых равна target.
        Работает за O(n): проходит по списку один раз, запоминая числа
        и их позиции в словаре. Для каждого элемента проверяет,
        было ли уже число (target - текущее). Если да — возвращает пару индексов.
        Гарантируется, что решение существует и уникально.
        """
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        raise ValueError('Нет решения')