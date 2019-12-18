user_agent
==========

.. code-block:: python

    fake.android_platform_token()
    # 'Android 2.2.3'

    fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)
    # ('Mozilla/5.0 (Windows NT 5.01) AppleWebKit/531.0 (KHTML, like Gecko) '
    #  'Chrome/54.0.886.0 Safari/531.0')

    fake.firefox()
    # ('Mozilla/5.0 (Windows 98; dv-MV; rv:1.9.2.20) Gecko/2013-09-09 14:02:27 '
    #  'Firefox/15.0')

    fake.internet_explorer()
    # 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)'

    fake.ios_platform_token()
    # 'iPad; CPU iPad OS 9_3_6 like Mac OS X'

    fake.linux_platform_token()
    # 'X11; Linux i686'

    fake.linux_processor()
    # 'x86_64'

    fake.mac_platform_token()
    # 'Macintosh; U; PPC Mac OS X 10_5_7'

    fake.mac_processor()
    # 'U; Intel'

    fake.opera()
    # 'Opera/8.40.(Windows NT 5.01; ig-NG) Presto/2.9.176 Version/12.00'

    fake.safari()
    # ('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_1 rv:4.0; id-ID) '
    #  'AppleWebKit/531.20.4 (KHTML, like Gecko) Version/4.0 Safari/531.20.4')

    fake.user_agent()
    # ('Mozilla/5.0 (Windows NT 4.0) AppleWebKit/531.0 (KHTML, like Gecko) '
    #  'Chrome/44.0.881.0 Safari/531.0')

    fake.windows_platform_token()
    # 'Windows NT 5.1'
