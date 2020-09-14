"""
Программа для переноса даты на определенныое количество дней, месяцев и годов с учетом високосности.
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
    def max_day_in_month(self, year, month):
        return self.DAY_OF_MONTH[self.is_leap_year(year)][month-1]

    def is_valid_date(self, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 12 >= month > 0:
            raise ValueError("month must be in range 1 - 12")
        if not self.max_day_in_month(year, month) >= day > 0:
            raise ValueError(f"day must be in range 1 - {self.max_day_in_month(year, month)}")

    def add_year(self, adding_year):
        if not isinstance(adding_year, int):
            raise TypeError('year must be int')

        current_year = self._year
        current_day = self._day
        future_month = self._month
        future_year = current_year + adding_year
        max_day_in_future_month = self.max_day_in_month(future_year, future_month)

        if current_day <= max_day_in_future_month:
            self._year += adding_year
        else:
            self._day = current_day - max_day_in_future_month
            self._month += 1
            self._year += adding_year

    def add_month(self, adding_month):
        if not isinstance(adding_month, int):
            raise TypeError('month must be int')

        current_month = self._month
        current_year = self._year
        current_day = self._day
        future_month = (current_month + adding_month - 1) % 12 + 1
        future_year = current_year + (current_month + adding_month) // 12
        max_day_in_future_month = self.max_day_in_month(future_year, future_month)

        if adding_month <= 12 - current_month and current_day <= max_day_in_future_month:    # В декаборе 31 день
            self._month += adding_month

        elif adding_month < 12 - current_month and current_day > max_day_in_future_month:
            self._month += adding_month + 1
            self._day = current_day - max_day_in_future_month

        elif adding_month > 12 - current_month and current_day <= max_day_in_future_month:
            self._year += (current_month + adding_month) // 12
            self._month = (current_month + adding_month - 1) % 12 + 1

        elif adding_month > 12 - current_month and current_day > max_day_in_future_month:
            self._year += (current_month + adding_month) // 12
            self._month = (current_month + adding_month) % 12 + 1
            self._day = current_day - max_day_in_future_month

    def add_day(self, adding_dat):
        if not isinstance(adding_dat, int):
            raise TypeError('day must be int')

        current_day = self._day
        current_month = self._month
        current_year = self._year
        max_day_in_current_month = self.max_day_in_month(current_year, current_month)

        while adding_dat > 0:
            if adding_dat + current_day <= max_day_in_current_month:
                self._day += adding_dat
                adding_dat = 0
            else:
                adding_dat -= (max_day_in_current_month - current_day + 1)
                self._day = 1

                if current_month == 12:
                    self._month = 1
                    self._year += 1
                self._month += 1
            return self.add_day(adding_dat)


# date = Date(2020, 3, 31)
date = Date(2020, 2, 29)
print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")
print(f"--------- ")

date.add_day(337)
date.add_month(227)
date.add_year(1)

print(f"{date} // ({date._year} год високосный?: {date.is_leap_year(date._year)})")


# date1 = Date(2018, 11, "Thirty two")
# print(date1)
# print(f"Год: {date1.year}, Месяц: {date1.month}, День: {date1.day}")

# date2 = Date(2018, 11, 34)
# print(date2)
# print(f"Год: {date2.year}, Месяц: {date2.month}, День: {date2.day}")

# date1 = Date(2030, 2, 28)
# print(date1)
# print(date1.NEW_DATES)