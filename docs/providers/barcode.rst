barcode
=======

.. code-block:: python

    fake.ean(length=13)
    # '4003832285771'

    fake.ean13(leading_zero=None)
    # '9620020275212'

    fake.ean8()
    # '17726313'

    fake.upc_a(upc_ae_mode=False, base=None, number_system_digit=None)
    # '915865094906'

    fake.upc_e(base=None, number_system_digit=None, safe_mode=True)
    # '12356247'
