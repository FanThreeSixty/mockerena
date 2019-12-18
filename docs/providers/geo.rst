geo
===

.. code-block:: python

    fake.coordinate(center=None, radius=0.001)
    # Decimal('-103.020900')

    fake.latitude()
    # Decimal('46.895312')

    fake.latlng()
    # (Decimal('62.242791'), Decimal('-131.954833'))

    fake.local_latlng(country_code="US", coords_only=False)
    # ('38.96372', '-76.99081', 'Chillum', 'US', 'America/New_York')

    fake.location_on_land(coords_only=False)
    # ('30.76468', '74.12286', 'Kanganpur', 'PK', 'Asia/Karachi')

    fake.longitude()
    # Decimal('87.180878')
