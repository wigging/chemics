import numpy as np
import textwrap


def proximate_bases(fc, vm, ash, moisture, disp=False):
    """
    Convert proximate analysis from as-received basis (% ar) to dry basis (%
    dry) and dry-ash free basis (% daf).

    Parameters
    ----------
    fc : float
        Percent fixed carbon
    vm : float
        Percent volatile matter
    ash : float
        Percent ash
    moisture : float
        Percent moisture
    disp : bool, optional
        Print results to console, default is `False`

    Returns
    -------
    bases : dict
        Proximate analysis bases calculated from given as-received basis.
        Bases are represented by keys in the dictionary where `'ar'` is
        as-received basis with values of `[FC, VM, ash, moisture]`, `'dry'` is
        dry basis with values of `[FC, VM, ash]`, and `'daf'` is dry ash-free
        basis with values of `[FC, VM]`.

    Raises
    ------
    ValueError
        If the proximate analysis sum is not 100.

    Example
    -------
    >>> proximate_bases(16.92, 76.40, 0.64, 6.04)
    {
        'ar': [16.92, 76.4, 0.64, 6.04],
        'dry': [18.00, 81.31, 0.68],
        'daf': [18.13, 81.86]
    }
    """

    # as-received basis (% ar)
    prox_ar = [fc, vm, ash, moisture]
    sum_ar = sum(prox_ar)

    # make sure proximate analysis sums to 100
    if not np.isclose(sum_ar, 100.0):
        raise ValueError('Sum of proximate analysis values must be 100')

    # dry basis (% dry)
    prox_dry = [100 * x / (sum_ar - prox_ar[-1]) for x in prox_ar[:-1]]
    sum_dry = sum(prox_dry)

    # dry ash-free basis (% daf)
    prox_daf = [100 * x / (sum_dry - prox_dry[-1]) for x in prox_dry[:-1]]
    sum_daf = sum(prox_daf)

    # print results to console if `disp=True`
    if disp:
        results = textwrap.dedent(f"""
                        % ar    % dry    % daf
        FC          {prox_ar[0]:8} {prox_dry[0]:8.2f} {prox_daf[0]:8.2f}
        VM          {prox_ar[1]:8} {prox_dry[1]:8.2f} {prox_daf[1]:8.2f}
        ash         {prox_ar[2]:8} {prox_dry[2]:8.2f}
        moisture    {prox_ar[3]:8}
        sum         {sum_ar:8.2f} {sum_dry:8.2f} {sum_daf:8.2f}
        """)
        print(results)

    # results dictionary
    bases = {
        'ar': prox_ar,
        'dry': prox_dry,
        'daf': prox_daf
    }

    return bases
