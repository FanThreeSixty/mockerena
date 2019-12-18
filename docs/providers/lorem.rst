lorem
=====

.. code-block:: python

    fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    # ('Social scientist rock owner. Write visit him adult various. Throw fish guess '
    #  'civil gun middle interview.')

    fake.paragraphs(nb=3, ext_word_list=None)
    # [   'Be involve push water. Pass my type report. Sure scientist economy '
    #     'religious water.',
    #     'Seat value decision professional month Mr hit war. Too PM resource '
    #     'protect media or product address. Even central consumer. Choice speech '
    #     'stop idea.',
    #     'Past sit remember car. Especially sign chair about trouble.']

    fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    # 'Although building mention might.'

    fake.sentences(nb=3, ext_word_list=None)
    # [   'Father radio business social religious.',
    #     'Fly life various little.',
    #     'Modern nothing what well prove cold page.']

    fake.text(max_nb_chars=200, ext_word_list=None)
    # ('Into strategy young economy though big.\n'
    #  'Democratic crime compare. Maintain see inside. Remember general practice '
    #  'international risk.')

    fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
    # [   'Bit child generation task local such. Election oil sea central buy level '
    #     'everything. Eat specific central president brother this.',
    #     'Deep police national exist rise. During off doctor cost begin actually. '
    #     'Property read tend.\n'
    #     'Power land part with none maintain wrong. Sound section tax dark teacher.',
    #     'Street game such. Way or Mrs win tree arrive.\n'
    #     'Central consider real oil they career. Story model stand I respond '
    #     'throughout program. Collection three amount you.']

    fake.word(ext_word_list=None)
    # 'forget'

    fake.words(nb=3, ext_word_list=None, unique=False)
    # ['in', 'part', 'forward']
