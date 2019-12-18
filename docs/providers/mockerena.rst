mockerena
=========

.. code-block:: python

    fake.empty()
    # ''

    fake.price(minimum=0, maximum=20)
    # 16.78

    fake.regex(expression='[a-zA-Z0-9]{12}')
    # 'd79eSfd98Sz2'

    fake.weighted_choice(elements=['a', 'b', 'c'], weights=[10, 2, 1])
    # 'a'
