class weapon():

    def __init__(self, clip, rate, range, name = 'Unknown'): # магазин, скорострельность, дальность
        self.max_clip = clip
        self.clip = clip
        self.rate = rate  # выстрелов в минуту
        self.range = range
        self.name = name

    def empty_clip(self):  # время опустошения магазина в секундах
        return round(self.clip / self.rate * 60, 1)

    def rate_to_range(self):  # соотношение частоты к дальности
        return round(self.rate / self.range, 4)


# штурмовая винтовка
class assault_rifle(weapon): # AK-12 https://kalashnikovgroup.ru


    def reload(self, bullets):  # перезарядка магазина
        self.clip = 0

        if 0 <= bullets <= self.max_clip:
            self.clip += bullets
            print('Перезарядка... заряжено ', bullets, 'патрон')
            return self.clip
        else:
            return

    def print_assault(self):   # вывод на экран для штурмовой винтовки
        print('Штурмовая винтовка: ' + self.name)
        print('Время разрядки: ', self.empty_clip(), 'секунды')
        print('Отношение частоты к дальности: ', self.rate_to_range())
        self.reload(5)
        print('Время разрядки: ', self.empty_clip(), 'секунды', '\n')


# снайперская винтовка
class sniper_rifle(assault_rifle):

    # Barret M82
    def __init__(self, clip = 10, rate = 30, range = 1800, name = 'Unknown'):
        self.time = 0
        self.max_clip = clip
        self.clip = clip
        self.rate = rate  # shots per minute
        self.range = range
        self.name = name

    def aiming_time(self, aim_range):  # добавляем время прицеливания в зависимости от дальности
        self.time += round((aim_range / 100), 1)
        return self.time

    def print_sniper(self):   # вывод на экран для снайперской винтовки
        print('Снайперская винтовка: ' + self.name)
        print('Время разрядки: ', self.empty_clip(), 'секунды')
        print('Отношение частоты к дальности: ', self.rate_to_range())
        self.reload(7)
        print('Время разрядки: ', self.empty_clip(), 'секунды')
        print('Время прицеливания: ', self.aiming_time(1500), '\n')



x = assault_rifle(30, 700, 800, 'AK-12')
x.print_assault()

y = sniper_rifle(10, 30, 1800,'M82')
y.print_sniper()











