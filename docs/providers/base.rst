base
====

.. code-block:: python

    fake.bothify(text="## ??", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # '70 SY'

    fake.hexify(text="^^^^", upper=False)
    # '5d05'

    fake.language_code()
    # 'kk'

    fake.lexify(text="????", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # 'ueZW'

    fake.locale()
    # 'fi_FI'

    fake.numerify(text="###")
    # '928'

    fake.random_choices(elements=('a', 'b', 'c'), length=None)
    # ['a', 'b']

    fake.random_digit()
    # 2

    fake.random_digit_not_null()
    # 7

    fake.random_digit_not_null_or_empty()
    # 1

    fake.random_digit_or_empty()
    # 0

    fake.random_element(elements=('a', 'b', 'c'))
    # 'a'

    fake.random_elements(elements=('a', 'b', 'c'), length=None, unique=False)
    # ['b']

    fake.random_int(min=0, max=9999, step=1)
    # 3825

    fake.random_letter()
    # 'A'

    fake.random_letters(length=16)
    # ['k', 'f', 'y', 'g', 'c', 'J', 'x', 'f', 'H', 'K', 'M', 'O', 'm', 'b', 'w', 'm']

    fake.random_lowercase_letter()
    # 'n'

    fake.random_number(digits=None, fix_len=False)
    # 6

    fake.random_sample(elements=('a', 'b', 'c'), length=None)
    # ['b']

    fake.random_uppercase_letter()
    # 'Z'

    fake.randomize_nb_elements(number=10, le=False, ge=False, min=None, max=None)
    # 11