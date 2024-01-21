"""
Application for comparing two lists of numbers
"""
from numbers import Number


class MyApp:
    """
    Class for receiving two lists of numbers, computing means and comparing its
    """
    def __init__(self, list1, list2):
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Программа работает только со списками чисел")
        if (not all(isinstance(i, Number) for i in list1)
                or not all(isinstance(i, Number) for i in list2)):
            raise TypeError("Программа работает только с числами")
        self.list1 = list1
        self.list2 = list2
        self.list1_mean = None
        self.list2_mean = None

    def mean_compute(self):
        """
        Mean computing method
        :return: mean of first list, mean of second list
        """
        if len(self.list1) == 0 or len(self.list2) == 0:
            raise ZeroDivisionError("Оба списка должны содержать числа")
        self.list1_mean = sum(self.list1) / len(self.list1)
        self.list2_mean = sum(self.list2) / len(self.list2)
        return self.list1_mean, self.list2_mean

    def list_compare(self):
        """
        Comparing means of numbers lists method
        :return: Message about which mean larger
        """
        if self.list1_mean > self.list2_mean:
            return "Первый список имеет большее среднее значение"
        if self.list1_mean < self.list2_mean:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
