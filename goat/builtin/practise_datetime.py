from datetime import datetime, timezone, timedelta

if __name__ == '__main__':
    # 获取当前时间
    now = datetime.now()
    print('now --> {}'.format(now))
    print('type(now) --> {}'.format(type(now)))

    # 获取制定时间
    my_date_time = datetime(1999, 12, 6, 10, 33)
    print('my_date_time --> {}'.format(my_date_time))

    # datetime 2 timestamp
    datetime_202501061609 = datetime(2025, 1, 6, 16, 9)
    timestamp_202501061609 = datetime_202501061609.timestamp()
    print('timestamp_202501061609 --> {}'.format(timestamp_202501061609))

    # timestamp 2 datetime
    timestamp_1736150940 = 1736150940.0
    datetime_1736150940 = datetime.fromtimestamp(timestamp_1736150940)
    datetime_1736150940_utc = datetime.fromtimestamp(timestamp_1736150940, tz=timezone.utc)
    print('datetime_1736150940 --> {}'.format(datetime_1736150940))
    print('datetime_1736150940_utc --> {}'.format(datetime_1736150940_utc))

    # str 2 datetime
    date_str = '2025-01-06 16:18:00'
    date_format = '%Y-%m-%d %H:%M:%S'
    str_date = datetime.strptime(date_str, date_format)
    print("str_date --> {} , type --> {}".format(str_date, type(str_date)))
    date_format = '%Y/%m/%d-%H:%M:%S'
    # datetime 2 str
    date = str_date.strftime(date_format)
    print("date --> {}, type --> {}".format(date, type(date)))

    # datetime 加减指定时间
    now = datetime.now()
    print('now --> {}'.format(now))
    new_datetime = now + timedelta(hours=10)
    print('new_datetime --> {}'.format(new_datetime))
    new_datetime = now - timedelta(days=2)
    print('new_datetime --> {}'.format(new_datetime))
    new_datetime = now - timedelta(weeks=3)
    print('new_datetime --> {}'.format(new_datetime))

    # 时区 utc-8
    tz_utc_8 = timezone(timedelta(hours=8))
    now = datetime.now()
    print('now --> {}'.format(now))
    dt = now.replace(tzinfo=tz_utc_8)
    print('dt --> {}, tzinfo --> {}'.format(dt, tz_utc_8))

    # 拿到utc时间，并强制设置时区为 utc+0:00
    utc_dt = datetime.datetime.now(datetime.timezone.utc)
    print('utc_dt --> {}'.format(utc_dt))
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print('bj_dt --> {}'.format(bj_dt))
