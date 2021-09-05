# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}i"

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return ComplexNumber(((self.a * other.a) - (self.b * other.b)), (self.b * other.a) + (self.a * other.b))


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(3, 4)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)