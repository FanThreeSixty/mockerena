profile
=======

.. code-block:: python

    fake.profile(fields=None, sex=None)
    # {   'address': '450 Bell Plain Suite 835\nMitchellshire, CT 90095',
    #     'birthdate': datetime.date(1974, 12, 4),
    #     'blood_group': 'B-',
    #     'company': 'Jacobson-Elliott',
    #     'current_location': (Decimal('11.6389045'), Decimal('-5.498963')),
    #     'job': 'Furniture conservator/restorer',
    #     'mail': 'vanessa06@yahoo.com',
    #     'name': 'Lindsey Moore',
    #     'residence': '28190 Mark Road\nEast Jonbury, AK 59940',
    #     'sex': 'F',
    #     'ssn': '575-51-4586',
    #     'username': 'kknight',
    #     'website': ['https://www.sutton.com/', 'http://gonzalez.org/']}

    fake.simple_profile(sex=None)
    # {   'address': '492 Felicia Coves Suite 951\nNew Keithtown, WY 72377',
    #     'birthdate': datetime.date(1952, 1, 18),
    #     'mail': 'mcleangregory@yahoo.com',
    #     'name': 'Rachel Lawrence',
    #     'sex': 'F',
    #     'username': 'robertking'}
