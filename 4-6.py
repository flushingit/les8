# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

import datetime


class DiapError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    _max_space: int
    stuff_in: list
    stuff_out: list
    _space: list

    @staticmethod
    def validate(num, rang, txt):
        try:
            num = int(num)
            if num < 1 or num > rang:
                raise DiapError(f"{txt} {rang}")
            else:
                return int(num)

        except ValueError:
            print("Вы ввели не число")
        except DiapError as err:
            print(err)

    def __init__(self, max_space):
        self._max_space = max_space
        self._space = []
        self.stuff_in = []
        self.stuff_out = []
        for x in range(self._max_space):
            self._space.append(0)

    def loading(self):

        while True:
            t = input("Что вы хотите отправить на склад? \n Принтер(1), Сканер(2) или Ксерокс(3), х для выхода ")
            if t == 'x':
                return
            if self.validate(t, 3, 'Введите число от 1 до'):
                break

        cla = eval(Technics.t_list[int(t) - 1])
        print("Какую модель вы хотите добавить? Для новой модели нажмите \"n\", для выхода \"х\"")

        for x in range(len(cla.table)):
            print(f"{x + 1} {cla.table[x]}")
        while True:
            mod = input()
            if mod == 'x':
                return
            elif mod == 'n':
                b = input("Введите брэнд ")
                m = input("Введите модель ")
                p = input("Введите цену ")
                h = cla(b, m, p)
                return

            else:
                if self.validate(mod, len(cla.table), 'Введите число от 1 до'):
                    break

        stock_num = input(f"Сколько единиц вы хотите добавить? На складе свободно {self._space.count(0)} мест ")
        if self.validate(stock_num, self._space.count(0), 'Невозможно впихнуть невпихуемое, свободных мест на складе '):
            stock_num = int(stock_num)
            for x in range(stock_num):
                self._space[self._space.index(0)] = cla.table[int(mod) - 1].prop
            dt = datetime.date.today().strftime("%d-%m-%Y")

            self.stuff_in.append([dt, cla.table[int(mod) - 1].prop, stock_num])

    def unloading(self):
        if self._space.count(0) == len(self._space):
            print("Склад пуст. Загрузите что-нибудь")
            return
        print("На складе есть")
        for count, value in enumerate(self._space):
            print(f"{count + 1}) {value} ")
        while True:
            pos = input("Какую позицию вы хотите забрать? х для выхода ")
            if pos == 'x':
                return
            if self.validate(pos, len(self._space), 'Введите число от 1 до'):

                pos = int(pos)
                if self._space[pos-1] == 0:
                    print("Нельзя забрать пустую позицию")
                else:
                    print("Куда вы хотите её отправить? для выхода \"х\"")

                    for x in range(len(Branch.table)):
                        print(f"{x + 1} {Branch.table[x]}")
                    while True:
                        wh = input()
                        if wh == 'x':
                            return
                        else:
                            if self.validate(wh, len(Branch.table), 'Введите число от 1 до'):
                                break
                    wh = int(wh)
                    print(f"Позиция {pos} отправлена в {Branch.table[wh-1]}")
                    dt = datetime.date.today().strftime("%d-%m-%Y")

                    self.stuff_out.append([dt, self._space[pos-1], Branch.table[wh-1].prop.get('name')])
                    self._space[pos-1] = 0
                    return


class Branch:
    name: str
    stock: list
    table = []

    def __init__(self, name):
        self.name = name
        Branch.table.append(self)
    def __str__(self):
        return f"{self.name}"

    @property
    def prop(self):
        return vars(self)


class Technics:
    hw_type: str
    price: int
    t_list = ["Printer", "Scanner", "Xerox"]

    def __init__(self, hw_type, price):
        self.hw_type = hw_type
        self.price = price

    @property
    def prop(self):
        return vars(self)

    def __str__(self):
        return f"{self.hw_type} {self.brand} {self.model} {self.price}"

    def __repr__(self):
        return str(self)


class Printer(Technics):
    model: str
    brand: str
    table = []

    def __init__(self, brand, model, price):
        self.model = model
        self.brand = brand
        super().__init__(Printer.__name__, price)
        Printer.table.append(self)


class Scanner(Technics):
    model: str
    brand: str
    table = []

    def __init__(self, brand, model, price, ):
        self.model = model
        self.brand = brand
        super().__init__(Scanner.__name__, price)
        Scanner.table.append(self)


class Xerox(Technics):
    model: str
    brand: str
    table = []

    def __init__(self, brand, model, price):
        self.model = model
        self.brand = brand
        super().__init__(Xerox.__name__, price)
        Xerox.table.append(self)


s1 = Scanner('HP', "ScanJet", 10000)
s2 = Scanner('HP', "ScanJet+", 15000)
p1 = Printer('HP', 'LaserJet', 5000)
p2 = Printer('HP', 'LaserJet+', 10000)
x1 = Xerox('Apple', 'iXerox', 500000000000)
b1 = Branch('Кремль')
b2 = Branch('Мавзолей')
w1 = Warehouse(5)
print("Добро пожаловать на склад!")
while True:
    print("Что вы хотите? Разместить товар (1), Забрать товар (2) или посмотреть приход/ уход товара(3), х для выхода ")
    while True:
        t = input()
        if t == 'x':
            break
        if Warehouse.validate(t, 3, 'Введите число от 1 до'):

            print(t)
            if int(t) == 1:
                w1.loading()
            elif int(t) == 2:
                w1.unloading()
            elif int(t) == 3:
                print("Журнал поступлений (1), журнал отгрузок (2), назад (b)")
                while True:
                    t1 = input()
                    if t1 == 'b':
                        break
                    if Warehouse.validate(t1, 2, 'Введите число от 1 до'):
                        t1 = int(t1)
                        if t1 == 1:
                            print(*w1.stuff_in, sep='\n')
                        elif t1 == 2:
                            print(*w1.stuff_out, sep='\n')
                        break
        break
    if t == 'x':
        break

