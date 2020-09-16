"""
Программа для переноса на определенное количество дней, месяцев и годов с учетом високосности
и (или) изменения текущего дня, месяца, года.
"""

class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # Month_of_Year
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # Month_of_Leap_Year

    def __init__(self, year, month, day):
        self.is_valid_date(year, month, day)
        self._year = year
        self._month = month
        self._day = day

    def __str__(self):
        return f"Год: {self._year}, Месяц: {self._month}, День: {self._day}"

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        return False

    @classmethod
    def max_day_in_month(cls, year, month):
        return cls.DAY_OF_MONTH[cls.is_leap_year(year)][month-1]

    def is_valid_date(self, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('Month must be int')
        if not isinstance(day, int):
            raise TypeError('Day must be int')

        if not 12 >= month > 0:
            raise ValueError("Month must be in range 1 - 12")
        if not year > 0:
            raise ValueError("Year must be > 0")
        if not self.max_day_in_month(year, month) >= day > 0:
            raise ValueError(f"Day must be in range 1 - {self.max_day_in_month(year, month)}")

    def add_year(self, adding_year):
        if not isinstance(adding_year, int):
            raise TypeError('Year must be int')

        if self._day <= self.max_day_in_month(self._year + adding_year, self._month):
            self._year += adding_year
        else:
            self._day -= self.max_day_in_month(self._year + adding_year, self._month)
            self._month += 1
            self._year += adding_year

    def add_month(self, adding_month):
        if not isinstance(adding_month, int):
            raise TypeError('Month must be int')

        future_month = (self._month + adding_month - 1) % 12 + 1
        future_year = self._year + (self._month + adding_month - 1) // 12
        max_day_in_future_month = self.max_day_in_month(future_year, future_month)

        if adding_month <= 12 - self._month and self._day <= max_day_in_future_month:
            self._month += adding_month

        elif adding_month < 12 - self._month and self._day > max_day_in_future_month:
            self._month += adding_month + 1
            self._day = max_day_in_future_month

        elif adding_month > 12 - self._month and self._day <= max_day_in_future_month:
            self._year += future_year
            self._month = future_month

        elif adding_month > 12 - self._month and self._day > max_day_in_future_month:
            self._year += future_year
            self._month = future_month
            self._day = max_day_in_future_month

    def add_day(self, adding_day):
        if not isinstance(adding_day, int):
            raise TypeError('Day must be int')

        while adding_day > 0:
            if adding_day + self._day <= self.max_day_in_month(self._year, self._month):
                self._day += adding_day
                adding_day = 0
            else:
                adding_day -= (self.max_day_in_month(self._year, self._month) - self._day + 1)
                self._day = 1

                if self._month == 12:
                    self._month = 1
                    self._year += 1
                else:
                    self._month += 1
            return self.add_day(adding_day)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('Year must be int')
        if not year >= 0:
            raise TypeError('Year must be >= 0')

        if self._day < self.max_day_in_month(year, self._month):
            print(f"Setting year to {year}")
            self._day = self.max_day_in_month(year, self._month)
            self._year = year
        else:
            print(f"Setting year to {year}")
            self._year = year

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError('Month must be int')
        if not 12 >= month > 0:
            raise TypeError('Month must be in [1, 12] interval')

        # if next_month == february and current_day > max_day_in_february => 29.02
        if self._day <= self.max_day_in_month(self._year, month):
            print(f"Setting month to {month}")
            self._month = month
        else:
            print(f"Setting month to {month}")
            self._day = self.max_day_in_month(self._year, month)
            self._month = month

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):

        if not isinstance(day, int):
            raise TypeError('Day must be int')
        if not self.max_day_in_month(self._year, self._month) >= day > 0:
            raise TypeError(f"Day must be in [1, {self.max_day_in_month(self._year, self._month)}] interval")

        print(f"Setting day to {day}")
        self._day = day


date = Date(884, 2, 29)

print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
print(f"------------------------------------------------------------------------ ")

date.add_day(5)
print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
date.add_day(366)
print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
date.add_month(29)
print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
# date.add_year(1)
# date.year = 2502
# date.month = 2
# print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
# date.day = 29
# print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")

# date1 = Date(2018, 11, "Thirty two")
# print(date1)
# print(f"Год: {date1.year}, Месяц: {date1.month}, День: {date1.day}")

# date2 = Date(2018, 11, 34)
# print(date2)
# print(f"Год: {date2.year}, Месяц: {date2.month}, День: {date2.day}")

# date1 = Date(2030, 2, 28)
# print(date1)
# print(date1.NEW_DATES)
