internet
========

.. code-block:: python

    fake.ascii_company_email(*args, **kwargs)
    # 'michael17@lynn.net'

    fake.ascii_email(*args, **kwargs)
    # 'harrylloyd@hotmail.com'

    fake.ascii_free_email(*args, **kwargs)
    # 'landryjennifer@hotmail.com'

    fake.ascii_safe_email(*args, **kwargs)
    # 'sweeneydorothy@example.com'

    fake.company_email(*args, **kwargs)
    # 'whitney09@lowe.com'

    fake.domain_name(*args, **kwargs)
    # 'smith.com'

    fake.domain_word(*args, **kwargs)
    # 'wilson'

    fake.email(*args, **kwargs)
    # 'bradyadam@hotmail.com'

    fake.free_email(*args, **kwargs)
    # 'ecolon@gmail.com'

    fake.free_email_domain(*args, **kwargs)
    # 'gmail.com'

    fake.hostname(*args, **kwargs)
    # 'email-49.peterson.com'

    fake.image_url(width=None, height=None)
    # 'https://placekitten.com/748/98'

    fake.ipv4(network=False, address_class=None, private=None)
    # '150.231.191.162'

    fake.ipv4_network_class()
    # 'b'

    fake.ipv4_private(network=False, address_class=None)
    # '192.168.232.118'

    fake.ipv4_public(network=False, address_class=None)
    # '11.123.139.156'

    fake.ipv6(network=False)
    # '4a9f:dc70:9aba:53a:a0b1:d050:6d07:9b80'

    fake.mac_address()
    # '65:ec:40:78:62:92'

    fake.safe_email(*args, **kwargs)
    # 'owenswilliam@example.net'

    fake.slug(*args, **kwargs)
    # 'off-study-western'

    fake.tld()
    # 'org'

    fake.uri()
    # 'https://chambers-mcgee.com/search.htm'

    fake.uri_extension()
    # '.htm'

    fake.uri_page()
    # 'home'

    fake.uri_path(deep=None)
    # 'list/main/search'

    fake.url(schemes=None)
    # 'https://foster.info/'

    fake.user_name(*args, **kwargs)
    # 'michael98'
