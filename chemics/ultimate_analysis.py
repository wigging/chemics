import numpy as np


class Ultimate:
    """
    Ultimate analysis values expressed as different bases. Such bases are
    as-determined (ad), as-received (ar), dry (d), and dry ash-free (daf).

    Parameters
    ----------
    vals : list
        Ultimate analysis values given as weight percent (wt. %), μg/g
        (trace elements), or Btu/lb (gross calorific value). Order of values
        is [C, H, O, N, S, ash, moisture].
    basis : str
        Basis of given ultimate analysis values. Options are 'ad' for
        as-determined basis or 'ar' for as-received basis.
    ADL : float, optional
        Air-dry loss as weight percent.
    HO : bool, optional
        If `True` then the given H and O values include H and O from moisture.
        If `False` then the given H and O values exclude H and O from the
        moisture content.

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
    >>> ult = Ultimate([60.08, 5.44, 25.01, 0.88, 0.73, 7.86, 9.00], 'ad')
    >>> ult.ar_basis
    array([46.86, 6.70, 39.04, 0.68, 0.56, 6.13, 29.02])

    References
    ----------
    ASTM D3180-15, Standard Practice for Calculating Coal and Coke Analyses
    from As-Determined to Different Bases, ASTM International, West
    Conshohocken, PA, 2015.
    """

    def __init__(self, vals, basis, ADL=22, HO=True):
        self.ADL = ADL
        self.HO = HO

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
        s = '            ad        ar        d        daf\n' \
            f'C    {ad[0]:>10.2f}{ar[0]:>10.2f}{d[0]:>10.2f}{daf[0]:>10.2f}\n' \
            f'H    {ad[1]:>10.2f}{ar[1]:>10.2f}{d[1]:>10.2f}{daf[1]:>10.2f}\n' \
            f'O    {ad[2]:>10.2f}{ar[2]:>10.2f}{d[2]:>10.2f}{daf[2]:>10.2f}\n' \
            f'N    {ad[3]:>10.2f}{ar[3]:>10.2f}{d[3]:>10.2f}{daf[3]:>10.2f}\n' \
            f'S    {ad[4]:>10.2f}{ar[4]:>10.2f}{d[4]:>10.2f}{daf[4]:>10.2f}\n' \
            f'ash  {ad[5]:>10.2f}{ar[5]:>10.2f}{d[5]:>10.2f}{"-":>10}\n' \
            f'moisture {ad[6]:>6.2f}{ar[6]:>10.2f}{"-":>10}{"-":>10}\n' \
            f'total {sum(ad):>9.2f}{sum(ar):>10.2f}{sum(d):>10.2f}{sum(daf):>10.2f}'
        return s

    def _convert_from_ad(self):
        C_ad = self.ad_basis[0]
        H_ad = self.ad_basis[1]
        O_ad = self.ad_basis[2]
        N_ad = self.ad_basis[3]
        S_ad = self.ad_basis[4]
        ash_ad = self.ad_basis[5]
        M_ad = self.ad_basis[6]
        ADL = self.ADL

        # As-received basis (ar)
        M_ar = (M_ad * (100 - ADL) / 100) + ADL
        C_ar = C_ad * (100 - M_ar) / (100 - M_ad)
        if self.HO:
            H_ar = (H_ad - 0.1119 * M_ad) * (100 - M_ar) / (100 - M_ad) + 0.1119 * M_ar
            O_ar = (O_ad - 0.8881 * M_ad) * (100 - M_ar) / (100 - M_ad) + 0.8881 * M_ar
        else:
            H_ar = (H_ad - 0.1119 * M_ad) * (100 - M_ar) / (100 - M_ad)
            O_ar = (O_ad - 0.8881 * M_ad) * (100 - M_ar) / (100 - M_ad)
        N_ar = N_ad * (100 - M_ar) / (100 - M_ad)
        S_ar = S_ad * (100 - M_ar) / (100 - M_ad)
        ash_ar = ash_ad * (100 - M_ar) / (100 - M_ad)
        self.ar_basis = np.array([C_ar, H_ar, O_ar, N_ar, S_ar, ash_ar, M_ar])

        # Dry basis (d)
        C_d = C_ad * 100 / (100 - M_ad)
        H_d = (H_ad - 0.1119 * M_ad) * 100 / (100 - M_ad)
        O_d = (O_ad - 0.8881 * M_ad) * 100 / (100 - M_ad)
        N_d = N_ad * 100 / (100 - M_ad)
        S_d = S_ad * 100 / (100 - M_ad)
        ash_d = ash_ad * 100 / (100 - M_ad)
        self.d_basis = np.array([C_d, H_d, O_d, N_d, S_d, ash_d])

        # Dry ash-free basis (daf)
        C_daf = C_ad * 100 / (100 - M_ad - ash_ad)
        H_daf = (H_ad - 0.1119 * M_ad) * 100 / (100 - M_ad - ash_ad)
        O_daf = (O_ad - 0.8881 * M_ad) * 100 / (100 - M_ad - ash_ad)
        N_daf = N_ad * 100 / (100 - M_ad - ash_ad)
        S_daf = S_ad * 100 / (100 - M_ad - ash_ad)
        self.daf_basis = np.array([C_daf, H_daf, O_daf, N_daf, S_daf])

    def _convert_from_ar(self):
        C_ar = self.ar_basis[0]
        H_ar = self.ar_basis[1]
        O_ar = self.ar_basis[2]
        N_ar = self.ar_basis[3]
        S_ar = self.ar_basis[4]
        ash_ar = self.ar_basis[5]
        M_ar = self.ar_basis[6]
        ADL = self.ADL

        # As-determined basis (ad)
        M_ad = (M_ar - ADL) / ((100 - ADL) / 100)
        C_ad = C_ar * (100 - M_ad) / (100 - M_ar)
        if self.HO:
            H_ad = (H_ar - 0.1119 * M_ar) / ((100 - M_ar) / (100 - M_ad)) + 0.1119 * M_ad
            O_ad = (O_ar - 0.8881 * M_ar) / ((100 - M_ar) / (100 - M_ad)) + 0.8881 * M_ad
        else:
            H_ad = H_ar / ((100 - M_ar) / (100 - M_ad)) + 0.1119 * M_ad
            O_ad = O_ar / ((100 - M_ar) / (100 - M_ad)) + 0.8881 * M_ad
        N_ad = N_ar * (100 - M_ad) / (100 - M_ar)
        S_ad = S_ar * (100 - M_ad) / (100 - M_ar)
        ash_ad = ash_ar * (100 - M_ad) / (100 - M_ar)
        self.ad_basis = np.array([C_ad, H_ad, O_ad, N_ad, S_ad, ash_ad, M_ad])

        # Dry basis (d)
        C_d = C_ad * 100 / (100 - M_ad)
        H_d = (H_ad - 0.1119 * M_ad) * 100 / (100 - M_ad)
        O_d = (O_ad - 0.8881 * M_ad) * 100 / (100 - M_ad)
        N_d = N_ad * 100 / (100 - M_ad)
        S_d = S_ad * 100 / (100 - M_ad)
        ash_d = ash_ad * 100 / (100 - M_ad)
        self.d_basis = np.array([C_d, H_d, O_d, N_d, S_d, ash_d])

        # Dry ash-free basis (daf)
        C_daf = C_ad * 100 / (100 - M_ad - ash_ad)
        H_daf = (H_ad - 0.1119 * M_ad) * 100 / (100 - M_ad - ash_ad)
        O_daf = (O_ad - 0.8881 * M_ad) * 100 / (100 - M_ad - ash_ad)
        N_daf = N_ad * 100 / (100 - M_ad - ash_ad)
        S_daf = S_ad * 100 / (100 - M_ad - ash_ad)
        self.daf_basis = np.array([C_daf, H_daf, O_daf, N_daf, S_daf])
