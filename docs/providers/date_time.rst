date_time
=========

.. code-block:: python

    fake.am_pm()
    # 'AM'

    fake.century()
    # 'II'

    fake.date(pattern="%Y-%m-%d", end_datetime=None)
    # '1992-05-08'

    fake.date_between(start_date="-30y", end_date="today")
    # datetime.date(1996, 3, 11)

    fake.date_between_dates(date_start=None, date_end=None)
    # datetime.date(2019, 12, 17)

    fake.date_object(end_datetime=None)
    # datetime.date(1970, 4, 28)

    fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)
    # datetime.date(1974, 8, 27)

    fake.date_this_century(before_today=True, after_today=False)
    # datetime.date(2014, 3, 15)

    fake.date_this_decade(before_today=True, after_today=False)
    # datetime.date(2017, 7, 10)

    fake.date_this_month(before_today=True, after_today=False)
    # datetime.date(2019, 12, 5)

    fake.date_this_year(before_today=True, after_today=False)
    # datetime.date(2019, 3, 14)

    fake.date_time(tzinfo=None, end_datetime=None)
    # datetime.datetime(2009, 5, 31, 19, 30)

    fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)
    # datetime.datetime(717, 8, 11, 11, 16, 48)

    fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)
    # datetime.datetime(2005, 6, 14, 13, 37, 29)

    fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
    # datetime.datetime(2019, 12, 17, 15, 40, 47)

    fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
    # datetime.datetime(2001, 1, 5, 21, 12, 31)

    fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
    # datetime.datetime(2013, 11, 26, 18, 38, 11)

    fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
    # datetime.datetime(2019, 12, 2, 23, 26, 7)

    fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
    # datetime.datetime(2019, 10, 9, 20, 38, 9)

    fake.day_of_month()
    # '30'

    fake.day_of_week()
    # 'Thursday'

    fake.future_date(end_date="+30d", tzinfo=None)
    # datetime.date(2020, 1, 12)

    fake.future_datetime(end_date="+30d", tzinfo=None)
    # datetime.datetime(2020, 1, 3, 3, 48, 8)

    fake.iso8601(tzinfo=None, end_datetime=None)
    # '1985-06-24T10:08:04'

    fake.month()
    # '09'

    fake.month_name()
    # 'March'

    fake.past_date(start_date="-30d", tzinfo=None)
    # datetime.date(2019, 11, 29)

    fake.past_datetime(start_date="-30d", tzinfo=None)
    # datetime.datetime(2019, 12, 7, 0, 2, 27)

    fake.time(pattern="%H:%M:%S", end_datetime=None)
    # '06:57:15'

    fake.time_delta(end_datetime=None)
    # datetime.timedelta(0)

    fake.time_object(end_datetime=None)
    # datetime.time(14, 29, 53)

    fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
    # <generator object Provider.time_series at 0x7f3d78a484f8>

    fake.timezone()
    # 'Asia/Jerusalem'

    fake.unix_time(end_datetime=None, start_datetime=None)
    # 1437575659

    fake.year()
    # '1971'
