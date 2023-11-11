Proximate and ultimate analysis
===============================

Use the ``Proximate`` class to express proximate analysis values as different bases. Bases are as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).

.. doctest::

   >>> prox = cm.Proximate([47.26, 40.05, 4.46, 8.23], 'ad')
   >>> print(prox)
                   ad        ar        d        daf
   FC            47.26     39.53     51.50     54.13
   VM            40.05     33.50     43.64     45.87
   ash            4.46      3.73      4.86         -
   moisture       8.23     23.24         -         -
   total        100.00    100.00    100.00    100.00

.. doctest::

   >>> prox = cm.Proximate([39.53, 33.50, 3.73, 23.24], 'ar')
   >>> print(prox)
                   ad        ar        d        daf
   FC            47.26     39.53     51.50     54.13
   VM            40.05     33.50     43.64     45.87
   ash            4.46      3.73      4.86         -
   moisture       8.23     23.24         -         -
   total        100.00    100.00    100.00    100.00

.. doctest::

   >>> prox = cm.Proximate([39.53, 33.50, 3.73, 23.24], 'ar')
   >>> prox.daf_basis
   array([54.12844037, 45.87155963])

Use the ``Ultimate`` class to express ultimate analysis values as different bases. Bases are as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).

.. doctest::

   >>> ult = cm.Ultimate([60.08, 5.44, 25.01, 0.88, 0.73, 7.86, 9.00], 'ad')
   >>> print(ult)
               ad        ar        d        daf
   C         60.08     46.86     66.02     72.26
   H          5.44      6.71      4.87      5.33
   O         25.01     39.05     18.70     20.47
   N          0.88      0.69      0.97      1.06
   S          0.73      0.57      0.80      0.88
   ash        7.86      6.13      8.64         -
   moisture   9.00     29.02         -         -
   total    109.00    129.02    100.00    100.00

.. doctest::

   >>> ult = cm.Ultimate([46.86, 6.70, 39.05, 0.69, 0.57, 6.13, 29.02], 'ar')
   >>> print(ult)
               ad        ar        d        daf
   C         60.08     46.86     66.02     72.26
   H          5.43      6.70      4.86      5.32
   O         25.02     39.05     18.71     20.47
   N          0.88      0.69      0.97      1.06
   S          0.73      0.57      0.80      0.88
   ash        7.86      6.13      8.64         -
   moisture   9.00     29.02         -         -
   total    109.00    129.02    100.00    100.00

.. doctest::

   >>> ult = cm.Ultimate([46.86, 3.46, 13.27, 0.69, 0.57, 6.13, 29.02], 'ar', HO=False)
   >>> print(ult)
               ad        ar        d        daf
   C         60.08     46.86     66.02     72.26
   H          5.44      3.46      4.87      5.34
   O         25.01     13.27     18.70     20.46
   N          0.88      0.69      0.97      1.06
   S          0.73      0.57      0.80      0.88
   ash        7.86      6.13      8.64         -
   moisture   9.00     29.02         -         -
   total    109.00    100.00    100.00    100.00

.. doctest::
   :options: +NORMALIZE_WHITESPACE

   >>> ult = cm.Ultimate([46.86, 6.70, 39.05, 0.69, 0.57, 6.13, 29.02], 'ar')
   >>> ult.d_basis
   array([66.01...,  4.86..., 18.70...,  0.97...,  0.80..., 8.63...])
