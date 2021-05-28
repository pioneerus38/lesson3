from datetime import datetime, timedelta

dt_now = datetime.now()
print(f"Сегодня: {dt_now.strftime('%d.%m.%Y')}")

delta = timedelta(days=1)
print(f"Вчерашняя дата: {(dt_now - delta).strftime('%d.%m.%Y')}")

delta = timedelta(days=30)
print(f"Дата 30 дней назад: {(dt_now - delta).strftime('%d.%m.%Y')}")

string = "01/01/25 12:10:03.234567"
dt = datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f')
print(f"Объект datetime: {dt}")