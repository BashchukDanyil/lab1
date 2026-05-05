class Date:
    @staticmethod
    def _high_year(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    @staticmethod
    def _check_year(year):
        if year >= 1900 and year <= 2200:
            return True
        else:
            return False
    @staticmethod
    def _check_month(month):
        if month >= 1 and month <= 12:
            return True
        else:
            return False
    def _max_day(self, month, year):
        if month % 2 == 1 and month <= 7 or month % 2 == 0 and month > 7:
            return 31
        if month % 2 == 0 and month > 2 and month <= 7 or month % 2 == 1 and month > 7:
            return 30
        if month == 2 and self._high_year(year):
            return 29
        if month == 2 and not(self._high_year(year)):
            return 28
    def _check_day(self, year,month,day):
            if day >= 1 and day <= self._max_day(month, year):
                return True
            else:
                return False
    def __init__(self, day, month = None, year = None):
        if isinstance(day, Date):
            self._year = day.year
            self._month = day.month
            self._day = day.day
        else:
            self._year = int(year)
            self._month = int(month)
            self._day = int(day)
        assert self._check_year(self._year) and self._check_month(self._month) and self._check_day(self.year, self.month, self._day)
    @property
    def year(self):
        return self._year
    @property
    def month(self):
        return self._month
    @property
    def day(self):
        return self._day
    @year.setter
    def year(self, year):
        assert self._check_year(year)
        self._year = year
    @month.setter
    def month(self, month):
        assert self._check_month(month)
        self._month = month
    @day.setter
    def day(self, day):
        assert self._check_day(self._year, self._month, day)
        self._day = day
    def equal(self, date):
        if date._year == self._year and date._month == self._month and date._day == self._day:
            return True
        else:
            return False
    def bigger(self, date):
        if date._year > self._year:
            return False
        if date._year < self._year:
            return True
        if date._year == self._year:
            if date._month > self._month:
                return False
            if date._month < self._month:
                return True
            if date._month == self._month:
                if date._day > self._day:
                    return False
                else:
                    return True
    def plus(self, a : int):
        if a == 0:
            pass
        if a > 0:
            while a > 0:
                if self._check_day(self._year, self._month, self._day + a):
                    self._day += a
                    a = 0
                elif self._check_month(self._month + 1):
                    a -= (self._max_day(self._month, self.year) - self._day)
                    self._month += 1
                    self._day = 0
                elif self._check_year(self.year + 1):
                    a -= self._max_day(self._month, self.year) - self._day
                    self._year += 1
                    self._month = 0
        if a < 0:
            while a < 0:
                if self._check_day(self._year, self._month, self._day + a):
                    self._day += a
                    a = 0
                elif self._check_month(self._month - 1):
                    a += self._day
                    self._month -= 1
                    self._day = self._max_day(self._month, self.year)
                elif self._check_year(self.year + 1):
                    a += self._day
                    self._year -= 1
                    self._month = 12
    def days(self, last_date):

        years = 0
        for i in  range(self.year + 1, last_date.year):
            if self._high_year(i):
                years += 366
            else:
                years += 365
        month = 0
        if self.year == last_date.year:
            for i in range(self.month + 1, last_date.month):
                month += self._max_day(i, self.year)
        else:
            for i in range(self.month + 1, 13):
                month += self._max_day(i, self.year)
            for i in range(1, last_date.month):
                month += self._max_day(i, last_date.year)
        day = self._max_day(self.month, self.year) - self.day + 1 + last_date.day
        return years + month + day


    def __str__(self):
        if self._day < 10:
            day = f"0{self._day}"
        else:
            day = f"{self._day}"
        if self._month < 10:
            month = f"0{self._month}"
        else:
            month = f"{self._month}"
        return f"{day}:{month}:{self._year}"
class Guest:
    def __init__(self, name : str, start_date : Date, last_date : Date):
        self.name = name
        self.start_date = start_date
        self.last_date = last_date
class Room:
    def __init__(self, num : int, money : int, guest = None):
        self.num = num
        self.money = money
        self.guest = guest
    def open(self, s_date : Date, l_date : Date):
        if self.guest == None:
            return True
        if self.guest.start_date.bigger(l_date) or s_date.bigger(self.guest.last_date):
            return True
        return False
    def pay(self, s_date : Date, l_date : Date):
        return self.money * s_date.days(l_date)

class Hotel:
    def __init__(self, *rooms : Room):
        self.rooms = rooms
    def count_empty(self, s_date : Date, l_date : Date):
        count = 0
        for room in self.rooms:
            if room.open(s_date, l_date):
                count += 1
        return count
    def empty(self, s_date : Date, l_date : Date):
        r = set()
        for room in self.rooms:
            if room.open(s_date, l_date):
                r.add(room)
        if len(r) == 0:
            return "Всі кімнати зайняті"
        return r
    def add(self, name, num, money, s_date : Date, l_date : Date):
        self.rooms += [Room(num, money, guest=Guest(name, s_date, l_date))]
    def pay(self, s_date : Date, l_date : Date):
        sum = 0
        for room in self.rooms:
            sum += room.pay(s_date, l_date)
        return sum
    def look(self, name, s_date : Date, l_date : Date):
        for room in self.rooms:
            if room.guest.name == name and not(room.open(s_date, l_date)):
                return num
g1 = Guest("Guest1", Date("02", "04", "2026"), Date("02", "05", "2026"))
d1 = Date("02", "04", "2026")
d2 = Date("02", "05", "2026")
r = Room(12, 12, g1)
print(r.open(d1, d2))
print(d1.days(d2))
