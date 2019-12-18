python
======

.. code-block:: python

    fake.pybool()
    # False

    fake.pydecimal(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)
    # Decimal('39.382069')

    fake.pydict(nb_elements=10, variable_nb_elements=True, *value_types)
    # {   'any': 'bIEWImVSeilExvfVzAQt',
    #     'anything': 'sarah38@coleman.info',
    #     'could': 'reeseshirley@peterson-baker.com',
    #     'country': -88977.0,
    #     'decade': 'drew86@kelley.com',
    #     'do': 'http://hendrix-smith.com/tag/register.html',
    #     'face': 3725,
    #     'full': 'eUgYmsfBwJpsFyWEfeLA',
    #     'own': 'http://www.turner.com/about/',
    #     'reach': 'https://schneider.info/tags/about.html',
    #     'soon': 'http://deleon.com/terms.asp',
    #     'wall': 'TaiIVervjjrQwFaajGOs',
    #     'worry': 'https://www.wu.biz/main/author.html'}

    fake.pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)
    # -67743.0

    fake.pyint(min_value=0, max_value=9999, step=1)
    # 3053

    fake.pyiterable(nb_elements=10, variable_nb_elements=True, *value_types)
    # (   'GldbKzKOMarKaMFqQDmb',
    #     'http://www.ford-williams.com/main/',
    #     'vYQaVmyaQrcvJzhJgihZ',
    #     'KJyejdinuwiDDUqoCnoJ',
    #     datetime.datetime(2008, 4, 15, 16, 47, 16),
    #     datetime.datetime(1981, 10, 2, 1, 51, 11),
    #     'YzXjwbpKihNWeRCyTVzu',
    #     Decimal('8014.687'),
    #     'vgwjrqxVgMgrXThstPQG',
    #     Decimal('-598068520.484'))

    fake.pylist(nb_elements=10, variable_nb_elements=True, *value_types)
    # [   datetime.datetime(2014, 1, 21, 4, 21, 52),
    #     8014,
    #     681,
    #     'WsSaNstwIaDHcVKmwGmR',
    #     datetime.datetime(1976, 11, 8, 10, 0, 35),
    #     'derrick66@yahoo.com',
    #     'https://smith.com/search/',
    #     -760473.42934]

    fake.pyset(nb_elements=10, variable_nb_elements=True, *value_types)
    # {1859, datetime.datetime(2011, 3, 21, 17, 20, 40), datetime.datetime(1971, 11, 27, 14, 27, 40), 'katherinecarter@hotmail.com', 'PkylXftPgKdqkcDzqObK', datetime.datetime(2010, 10, 23, 3, 35, 52), 'https://wright.com/', 4047, 7094, 'npviFeKJukhLXSFpIdxL', -7811233.3}

    fake.pystr(min_chars=None, max_chars=20)
    # 'WpbgERLJeDwPLNqdAQoU'

    fake.pystr_format(string_format="?#-###{{random_int}}{{random_letter}}", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # 'n2-0755234c'

    fake.pystruct(count=10, *value_types)
    # (   [   Decimal('-13540452324169.0'),
    #         'HRTLLqhfMsyBUuTwPNQt',
    #         811.702,
    #         'xqQhyFatECkNSIjbVpxP',
    #         -567370968463.22,
    #         'rUwhBmMMSRrNibOLnarU',
    #         'http://jackson.com/',
    #         1408,
    #         'rzShTqnQEfTZFwUgQFmU',
    #         'BGZodRmEsmeCIYnmXLGc'],
    #     {   'hear': Decimal('12369.435855'),
    #         'inside': 'IEtHqVPrvNUWScErsLTY',
    #         'lawyer': 'http://www.brown.com/faq.html',
    #         'necessary': 8257,
    #         'operation': 'sBwzglaZfNFnLhBjbYqu',
    #         'or': datetime.datetime(1979, 3, 27, 3, 32, 30),
    #         'our': 6768,
    #         'professional': 'ZlsAberdyIlJHZoCrSag',
    #         'record': 8488,
    #         'research': 3544},
    #     {   'cold': {   8: 'DnMwftNGSOdKmUtKQQxU',
    #                     9: [   'vbMZtMmBkjeuzBudfpSm',
    #                            'RCpBHQdiphIcNNlxSxxw',
    #                            'ebryant@rivera-mccann.com'],
    #                     10: {   8: datetime.datetime(1996, 12, 18, 11, 42, 15),
    #                             9: 'SUYNmeCAOEjoqYBjvSat',
    #                             10: ['vIziFlxhKaTBYLSVnFxo', Decimal('-9105.65')]}},
    #         'hour': {   7: Decimal('841271008.3'),
    #                     8: [   Decimal('311033719146.0'),
    #                            datetime.datetime(2007, 7, 8, 8, 34, 45),
    #                            223258276.5],
    #                     9: {   7: 'OhyKgLnDCRXwjYnzzmoo',
    #                            8: 'jVsAZXLSxqaYqXkNQIvb',
    #                            9: ['CicHUNSAEiErymSfNkeb', 968]}},
    #         'mean': {   5: 5393,
    #                     6: [   'https://www.garrett.com/',
    #                            5269,
    #                            datetime.datetime(2006, 1, 26, 9, 16, 23)],
    #                     7: {   5: Decimal('2634721280916.84'),
    #                            6: Decimal('846707683.27825'),
    #                            7: [   'https://www.zimmerman.com/',
    #                                   'IHvYFjdDHEGOUiEHqJAP']}},
    #         'never': {   4: -834261.80146,
    #                      5: [   'starkbrian@alvarez-dougherty.com',
    #                             3449,
    #                             'DOgmMaICIEoJYPgLxQDS'],
    #                      6: {   4: 'bUotzJfglHzxGyMblnkX',
    #                             5: 'sUAKifKmBpJXfWinlYEO',
    #                             6: [5648, 'grixWfpmMxCkrstxiUGp']}},
    #         'policy': {   9: 'dOxQtYxnorjnNAylcybt',
    #                       10: [   'https://www.smith.net/category/tag/posts/homepage/',
    #                               'UcrHiubkbwxUwuMLekpY',
    #                               'keithanderson@hotmail.com'],
    #                       11: {   9: 7038,
    #                               10: 'DweqThgILmtONoNwYhns',
    #                               11: [   Decimal('-610193752.97'),
    #                                       Decimal('8.949')]}},
    #         'rest': {   2: 'RDUEeMKSqvllYmLAdlMY',
    #                     3: [   920067058.845,
    #                            'nZIhIKGblTmLJnPNjkQR',
    #                            'https://mccarthy.com/main/list/posts/home/'],
    #                     4: {   2: 'MlfORxISpVlfsvuFvvto',
    #                            3: 'martinjohnny@lynch.org',
    #                            4: [   'https://clark.com/categories/app/faq.html',
    #                                   5619]}},
    #         'significant': {   0: datetime.datetime(2018, 8, 11, 14, 1, 22),
    #                            1: [   'http://www.martinez.net/',
    #                                   'https://www.morales-herman.com/app/categories/main.asp',
    #                                   'YjVqprZmsQzZDpHuIcAY'],
    #                            2: {   0: -7952.5686,
    #                                   1: 'tznlmdnqjBnsZKkBKbvB',
    #                                   2: [   1473,
    #                                          'http://www.barton.com/search/list/login.php']}},
    #         'strategy': {   6: 'myoder@hotmail.com',
    #                         7: [   'hernandeztiffany@hotmail.com',
    #                                'wQMlQOkBuzsVXjgEpIZp',
    #                                datetime.datetime(1974, 10, 13, 14, 54, 11)],
    #                         8: {   6: 3876,
    #                                7: 'ISLzWOPvZWVHOwgDrSSf',
    #                                8: [   'JWvWmBcgWHYmDfufNeEz',
    #                                       'pUSajWlzevGzwUAxxIMx']}},
    #         'wife': {   3: 8954,
    #                     4: [   'EeCtgLpDddwUicuLvgui',
    #                            'shannonbriggs@colon.com',
    #                            Decimal('-6937.5183')],
    #                     5: {   3: 9418,
    #                            4: 'WzjiAVybyrqzWoAqBipj',
    #                            5: [6294, 'OqslaYxCpZZnmpcaUzwH']}}})

    fake.pytuple(nb_elements=10, variable_nb_elements=True, *value_types)
    # (   8381764.17824994,
    #     'linda94@ortiz.biz',
    #     datetime.datetime(1978, 6, 3, 1, 56, 27),
    #     'oRHkIVsefCJQpucnsYQM',
    #     8259477.0,
    #     'jeasMeHZAqGldPMxpeof',
    #     'zCbgTRLOmQsqTyFioKpw',
    #     'https://www.aguilar.com/register.htm')
