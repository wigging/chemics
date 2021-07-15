import numpy as np


class Proximate:
    """
    Proximate analysis values expressed as different bases. Such bases are
    as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).

    Parameters
    ----------
    vals : list
        Proximate analysis values given as weight percent (wt. %), μg/g
        (trace elements), or Btu/lb (gross calorific value). Order of values
        is [FC, VM, ash, moisture].
    basis : str
        Basis of given proximate analysis values. Options are 'ad' for
        as-determined basis or 'ar' for as-received basis.
    ADL : float, optional
        Air-dry loss as weight percent. Default value is 16.36 weight percent.

    Attributes
    ----------
    ad_basis : ndarray
        As-determined basis (ad).
    ar_basis : ndarray
        As-received basis (ar).
    d_basis : ndarray
        Dry basis (d).
    daf_basis : ndarray
        Dry ash-free basis (daf).

    Raises
    ------
    ValueError
        If basis is not ad or ar.

    Example
    -------
    >>> prox = Proximate([47.26, 40.05, 4.46, 8.23], 'ad')
    >>> prox.ar_basis
    array([39.52, 33.49, 3.73, 23.24])

    References
    ----------
    ASTM D3180-15, Standard Practice for Calculating Coal and Coke Analyses
    from As-Determined to Different Bases, ASTM International, West
    Conshohocken, PA, 2015.
    """

    def __init__(self, vals, basis, ADL=16.36):
        self.ADL = ADL

        if basis == 'ad':
            self.ad_basis = np.array(vals)
            self._convert_from_ad()
        elif basis == 'ar':
            self.ar_basis = np.array(vals)
            self._convert_from_ar()
        else:
            raise ValueError("Basis must be 'ad' or 'ar'")

    def __str__(self):
        ad = self.ad_basis
        ar = self.ar_basis
        d = self.d_basis
        daf = self.daf_basis
        s = '                ad        ar        d        daf\n' \
            f'FC       {ad[0]:>10.2f}{ar[0]:>10.2f}{d[0]:>10.2f}{daf[0]:>10.2f}\n' \
            f'VM       {ad[1]:>10.2f}{ar[1]:>10.2f}{d[1]:>10.2f}{daf[1]:>10.2f}\n' \
            f'ash      {ad[2]:>10.2f}{ar[2]:>10.2f}{d[2]:>10.2f}{"-":>10}\n' \
            f'moisture {ad[3]:>10.2f}{ar[3]:>10.2f}{"-":>10}{"-":>10}\n' \
            f'total    {sum(ad):>10.2f}{sum(ar):>10.2f}{sum(d):>10.2f}{sum(daf):>10.2f}'
        return s

    def _convert_from_ad(self):
        FC_ad = self.ad_basis[0]
        VM_ad = self.ad_basis[1]
        ash_ad = self.ad_basis[2]
        M_ad = self.ad_basis[3]
        ADL = self.ADL

        # As-received basis (ar)
        M_ar = (M_ad * (100 - ADL) / 100) + ADL
        FC_ar = FC_ad * (100 - M_ar) / (100 - M_ad)
        VM_ar = VM_ad * (100 - M_ar) / (100 - M_ad)
        ash_ar = ash_ad * (100 - M_ar) / (100 - M_ad)
        self.ar_basis = np.array([FC_ar, VM_ar, ash_ar, M_ar])

        # Dry basis (d)
        FC_d = FC_ad * 100 / (100 - M_ad)
        VM_d = VM_ad * 100 / (100 - M_ad)
        ash_d = ash_ad * 100 / (100 - M_ad)
        self.d_basis = np.array([FC_d, VM_d, ash_d])

        # Dry ash-free basis (daf)
        FC_daf = FC_ad * 100 / (100 - M_ad - ash_ad)
        VM_daf = VM_ad * 100 / (100 - M_ad - ash_ad)
        self.daf_basis = np.array([FC_daf, VM_daf])

    def _convert_from_ar(self):
        FC_ar = self.ar_basis[0]
        VM_ar = self.ar_basis[1]
        ash_ar = self.ar_basis[2]
        M_ar = self.ar_basis[3]
        ADL = self.ADL

        # As-determined basis (ad)
        M_ad = (M_ar - ADL) / ((100 - ADL) / 100)
        FC_ad = FC_ar * (100 - M_ad) / (100 - M_ar)
        VM_ad = VM_ar * (100 - M_ad) / (100 - M_ar)
        ash_ad = ash_ar * (100 - M_ad) / (100 - M_ar)
        self.ad_basis = np.array([FC_ad, VM_ad, ash_ad, M_ad])

        # Dry basis (d)
        FC_d = FC_ar * 100 / (100 - M_ar)
        VM_d = VM_ar * 100 / (100 - M_ar)
        ash_d = ash_ar * 100 / (100 - M_ar)
        self.d_basis = np.array([FC_d, VM_d, ash_d])

        # Dry ash-free basis (daf)
        FC_daf = FC_ar * 100 / (100 - M_ar - ash_ar)
        VM_daf = VM_ar * 100 / (100 - M_ar - ash_ar)
        self.daf_basis = np.array([FC_daf, VM_daf])
