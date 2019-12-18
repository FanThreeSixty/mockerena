credit_card
===========

.. code-block:: python

    fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    # '09/25'

    fake.credit_card_full(card_type=None)
    # 'Discover\nDavid Taylor\n6011910416230682 07/24\nCVC: 814\n'

    fake.credit_card_number(card_type=None)
    # '4991269195116524'

    fake.credit_card_provider(card_type=None)
    # 'JCB 16 digit'

    fake.credit_card_security_code(card_type=None)
    # '4299'
