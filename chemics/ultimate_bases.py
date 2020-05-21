import numpy as np


def ultimate_bases(c, h, o, n, s, ash, moisture, disp=False):
    """
    Convert ultimate analysis from as-received basis (% ar) to dry basis (%
    dry) and dry ash-free (% daf) basis.

    Parameters
    ----------
    c : float
        Percent carbon
    h : float
        Percent hydrogen
    o : float
        Percent oxygen
    n : float
        Percent nitrogen
    s : float
        Percent sulfur
    ash : float
        Percent ash
    moisture : float
        Percent moisture
    disp : bool, optional
        Display results to console, default is `False`

    Returns
    -------
    bases : dict
        Ultimate analysis bases calculated from given as-received basis. Bases
        are represented by keys in the dictionary where `'ar'` is as-received
        basis with values that represent `[C, H, O, N, S, ash, moisture]`,
        `'dry'` is dry basis with values that represent `[C, H, O, N, S,
        ash]`, and `'daf'` is dry ash-free basis with values of `[C, H, O, N,
        S]`.

    Raises
    ------
    ValueError
        If the ultimate analysis sum is not 100.

    Example
    -------
    >>> ultimate_bases(49.52, 5.28, 38.35, 0.15, 0.02, 0.64, 6.04)
    {
        'ar': [49.52, 5.28, 38.35, 0.15, 0.02, 0.64, 6.04],
        'dry': [52.70, 5.61, 40.81, 0.15, 0.02, 0.68],
        'daf': [53.06, 5.65, 41.09, 0.16, 0.02]
    }
    """

    # as-received basis (% ar)
    ult_ar = [c, h, o, n, s, ash, moisture]
    sum_ar = sum(ult_ar)

    # make sure ultimate analysis sums to 100
    if not np.isclose(sum_ar, 100.0):
        raise ValueError('Sum of ultimate analysis values must be 100')

    # dry basis (% dry)
    ult_dry = [100 * x / (sum_ar - ult_ar[-1]) for x in ult_ar[:-1]]
    sum_dry = sum(ult_dry)

    # dry ash-free basis (% daf)
    ult_daf = [100 * x / (sum_dry - ult_dry[-1]) for x in ult_dry[:-1]]
    sum_daf = sum(ult_daf)

    # print results to console if `disp=True`
    if disp:
        results = (
            f'               % ar    % dry    % daf\n'
            f'C          {ult_ar[0]:8} {ult_dry[0]:8.2f} {ult_daf[0]:8.2f}\n'
            f'H          {ult_ar[1]:8} {ult_dry[1]:8.2f} {ult_daf[1]:8.2f}\n'
            f'O          {ult_ar[2]:8} {ult_dry[2]:8.2f} {ult_daf[2]:8.2f}\n'
            f'N          {ult_ar[3]:8} {ult_dry[3]:8.2f} {ult_daf[3]:8.2f}\n'
            f'S          {ult_ar[4]:8} {ult_dry[4]:8.2f} {ult_daf[4]:8.2f}\n'
            f'ash        {ult_ar[5]:8} {ult_dry[5]:8.2f}\n'
            f'moisture   {ult_ar[6]:8}\n'
            f'sum        {sum_ar:8.2f} {sum_dry:8.2f} {sum_daf:8.2f}\n'
        )
        print(results)

    # results dictionary
    bases = {
        'ar': ult_ar,
        'dry': ult_dry,
        'daf': ult_daf
    }

    return bases
