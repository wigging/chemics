"""
Use the `biocomp()` function to calculate biomass composition. Use the
`plot_biocomp()` function to create a Matplotlib figure of the biomass
composition results.
"""

import numpy as np


def biocomp(yc, yh, yo=None, yh2o=0, yash=0, alpha=0.6, beta=0.8, gamma=0.8,
            delta=1, epsilon=1, printcomp=False):
    """
    Determine bimoass composition from ultimate analysis mass fractions of C,
    H, and O. Composition returned as cellulose, hemicellulose, lignins, and
    extractives based on method discussed in the Debiagi 2015 paper [1]_.

    Parameters
    ----------
    yc : float
        Mass fraction of carbon in biomass, dry ash free basis [-]
    yh : float
        Mass fraction of hydrogen in biomass, dry ash free basis [-]
    yo : float, optional
        Mass fraction of oxygen in biomass, if not given then value is
        calculated as difference, dry ash free basis [-]. Default is None.
    yh2o : float, optional
        Mass fraction of water in biomass, as received basis [-]. Default is 0.
    yash : float, optional
        Mass fraction of ash in biomass, as received basis [-]. Default is 0.
    alpha : float, optional
        Splitting parameter as molar ratio of cellulose and hemicellulose
        contained in reference mixture RM1 [-]. Default is 0.6.
    beta : float, optional
        Splitting parameter as molar ratio of lignin LIG-O and lignin LIG-C
        contained in reference mixture RM2 [-]. Default is 0.8.
    gamma : float, optional
        Splitting parameter as molar ratio of lignin LIG-H and lignin LIG-C
        contained in reference mixture RM3 [-]. Default is 0.8.
    delta : float, optional
        Splitting parameter as molar ratio of lignins (LIG-H and LIG-C) and
        extractive TGL to define reference mixture RM2 [-]. Default is 1.0.
    epsilon : float, optional
        Splitting parameter as molar ratio of lignins (LIG-O and LIG-C) and
        extractive TANN to define reference mixture RM3 [-]. Default is 1.0.
    printcomp : bool, optional
        Print composition results if True. Default is False.

    Returns
    -------
    comp : dict
        Dictionary representing reference mixtures and biomass compositions on
        the basis of mole fractions (x) and mass fractions (y).

        - `y_rm1` mass fractions [C, H, O] of reference mixture RM1
        - `y_rm2` mass fractions [C, H, O] of reference mixture RM2
        - `y_rm3` mass fractions [C, H, O] of reference mixture RM3
        - `x_daf` mole fractions [cell, hemi, ligc, ligh, ligo, tann, tgl] of
          biomass as dry ash-free basis
        - `x_wet` mole fractions [cell, hemi, ligc, ligh, ligo, tann, tgl] of
          biomass as wet basis
        - `y_daf` mass fractions [cell, hemi, ligc, ligh, ligo, tann, tgl] of
          biomass as dry ash-free basis
        - `y_wet` mass fractions [cell, hemi, ligc, ligh, ligo, tann, tgl] of
          biomass as wet basis
        - `y_wetash` mass fractions [cell, hemi, ligc, ligh, ligo, tann, tgl]
          of biomass as wet ash basis

    Raises
    ------
    ValueError
        When sum of mass fractions is not equal to one.

    Examples
    --------
    >>> yc = 0.534
    >>> yh = 0.06
    >>> bc = biocomp(yc, yh)
    >>> bc['y_daf']
    array([0.2936, 0.1594, 0.0712, 0.2934, 0.1822, 0, 0])

    >>> yc = 0.500
    >>> yh = 0.060
    >>> yo = 0.440
    >>> yash = 0.15
    >>> biocomp(yc, yh, yo, yash=yash, printcomp=True)
    basis    cell    hemi    ligc    ligh    ligo    tann    tgl
    x_daf    0.5016  0.3344  0.0328  0.0614  0.0698  0.0000  0.0000
    x_wet    0.5016  0.3344  0.0328  0.0614  0.0698  0.0000  0.0000
    y_daf    0.4275  0.2322  0.0445  0.1409  0.1549  0.0000  0.0000
    y_wet    0.4275  0.2322  0.0445  0.1409  0.1549  0.0000  0.0000
    y_wetash 0.3634  0.1974  0.0378  0.1197  0.1317  0.0000  0.0000

    References
    ----------
    .. [1] Paulo Eduardo Amaral Debiagi, Chiara Pecchi, Giancarlo Gentile,
       Alessio Frassoldati, Alberto Cuoci, Tiziano Faravelli, and Eliseo Ranzi.
       Extractives Extend the Applicability of Multistep Kinetic Scheme of Biomass
       Pyrolysis. Energy and Fuels, vol. 29, no. 10, pp. 6544-6555, 2015.
    """

    # Determine oxygen mass fraction by difference if not explicitly given
    if yo is None:
        yo = 1 - yc - yh

    # Check that mass fractions sum to one
    sumy = yc + yh + yo
    tol = 1e-4
    if abs(sumy - 1.0) > tol:
        raise ValueError('Sum of mass fractions must equal one.')

    # Cellulose, hemicellulose, and lignins as arrays of [C, H, O]
    # See Figure 1 in reference for these formulas
    cell = np.array([6, 10, 5])
    hemi = np.array([5, 8, 4])
    ligc = np.array([15, 14, 4])
    ligh = np.array([22, 28, 9])
    ligo = np.array([20, 22, 10])
    tann = np.array([15, 12, 7])
    tgl = np.array([57, 100, 7])

    # Molecular weight of cellulose, hemicellulose, lignins, and water
    mw_cell = 162.141
    mw_hemi = 132.115
    mw_ligc = 258.273
    mw_ligh = 436.457
    mw_ligo = 422.386
    mw_tann = 304.254
    mw_tgl = 897.42
    mw_h2o = 18.015

    # Solve for pseudo species
    # -----------------------------------------------------------------------

    # Reference mixture where rm = [C, H, O]
    rm1 = alpha * cell + (1 - alpha) * hemi
    rm2 = beta * delta * ligh + (1 - beta) * delta * ligc + (1 - beta * delta - (1 - beta) * delta) * tgl
    rm3 = gamma * epsilon * ligo + (1 - gamma) * epsilon * ligc + (1 - gamma * epsilon - (1 - gamma) * epsilon) * tann

    # Molecular weight of reference mixture where C, H, O given as 12, 1, 16
    mw_rm1 = sum(rm1 * [12, 1, 16])
    mw_rm2 = sum(rm2 * [12, 1, 16])
    mw_rm3 = sum(rm3 * [12, 1, 16])

    # Mass fraction of reference mixture where y_rm = [yC, yH, yO]
    y_rm1 = (rm1 * [12, 1, 16]) / mw_rm1
    y_rm2 = (rm2 * [12, 1, 16]) / mw_rm2
    y_rm3 = (rm3 * [12, 1, 16]) / mw_rm3

    # Mass fraction of pseudo species where ys = [S1, S2, S3]
    # Solve system of linear equations Ax = b
    # A is 3x3 matrix with columns = [yC, yH, yO]
    a = np.array([y_rm1, y_rm2, y_rm3]).T
    b = np.array([yc, yh, yo])
    ys = np.linalg.solve(a, b)

    # Sum of mass fractions and molecular weights as sum(ys/MW)
    sum_ymw = sum(ys / [mw_rm1, mw_rm2, mw_rm3])

    # Mole fraction of pseudo species where xs = [S1, S2, S3]
    xs = (ys / [mw_rm1, mw_rm2, mw_rm3]) / sum_ymw

    # Biomass composition
    # -----------------------------------------------------------------------

    # Mole fraction as dry ash free basis for biomass components where
    # x_daf = [cell, hemi, ligc, ligh, ligo, tann, tgl]
    x_dafcell = alpha * xs[0]
    x_dafhemi = (1 - alpha) * xs[0]
    x_dafligc = (1 - beta) * delta * xs[1] + (1 - gamma) * epsilon * xs[2]
    x_dafligh = beta * delta * xs[1]
    x_dafligo = gamma * epsilon * xs[2]
    x_daftann = (1 - gamma * epsilon - (1 - gamma) * epsilon) * xs[2]
    x_daftgl = (1 - beta * delta - (1 - beta) * delta) * xs[1]
    x_daf = np.array([x_dafcell, x_dafhemi, x_dafligc, x_dafligh, x_dafligo, x_daftann, x_daftgl])

    # Molecular weight vector for biomass components where
    # mw_comp = [mw_cell, mw_hemi, mw_ligc, mw_ligh, mw_ligo, mw_tann, mw_tgl]
    mw_comp = x_daf * [mw_cell, mw_hemi, mw_ligc, mw_ligh, mw_ligo, mw_tann, mw_tgl]

    # Average molecular weight of all biomass components
    mw_avg = sum(mw_comp)

    # Mass fraction as dry ash free basis for biomass components where
    # y_daf = [cell, hemi, ligc, ligh, ligo, tann, tgl]
    y_daf = mw_comp / mw_avg

    # Mass fraction as wet basis for biomass components where
    # y_wet = [cell, hemi, ligc, ligh, ligo, tann, tgl]
    y_wet = y_daf * (1 - yh2o)

    # Mass fraction as wet + ash basis for biomass components where
    # y_wetash = [cell, hemi, ligc, ligh, ligo, tann, tgl]
    y_wetash = y_daf * (1 - yh2o - yash)

    # Mole fraction as wet basis for biomass components where
    # x_wet = [cell, hemi, ligc, ligh, ligo, tann, tgl]
    ywet_yh2o = np.concatenate((y_wet, [yh2o]))
    sum_xmw = sum(ywet_yh2o / [mw_cell, mw_hemi, mw_ligc, mw_ligh, mw_ligo, mw_tann, mw_tgl, mw_h2o])
    x_wet = (y_wet / [mw_cell, mw_hemi, mw_ligc, mw_ligh, mw_ligo, mw_tann, mw_tgl]) / sum_xmw

    comp = {
        'y_rm1': y_rm1,
        'y_rm2': y_rm2,
        'y_rm3': y_rm3,
        'x_daf': x_daf,
        'x_wet': x_wet,
        'y_daf': y_daf,
        'y_wet': y_wet,
        'y_wetash': y_wetash
    }

    # Print biomass composition results
    if printcomp:
        print('basis\t cell\t hemi\t ligc\t ligh\t ligo\t tann\t tgl')
        print('x_daf\t', '  '.join(f'{x:.4f}' for x in x_daf))
        print('x_wet\t', '  '.join(f'{x:.4f}' for x in x_wet))
        print('y_daf\t', '  '.join(f'{x:.4f}' for x in y_daf))
        print('y_wet\t', '  '.join(f'{x:.4f}' for x in y_wet))
        print('y_wetash', '  '.join(f'{x:.4f}' for x in y_wetash))

    return comp


def plot_biocomp(ax, yc, yh, y_rm1, y_rm2, y_rm3):
    """
    Plot characterization of biomass sample and calculated reference mixtures
    as mass fractions, dry ash-free basis.

    Parameters
    ----------
    ax : Axes
        The Matplotlib axes from a figure
    yc : float
        Mass fraction of carbon in biomass, dry ash free basis [-]
    yh : float
        Mass fraction of hydrogen in biomass, dry ash free basis [-]
    y_rm1 : array
        Mass fraction of reference mixture RM1 where y_rm1 = [yC, yH, yO]
    y_rm2 : array
        Mass fraction of reference mixture RM2 where y_rm2 = [yC, yH, yO]
    y_rm3 : array
        Mass fraction of reference mixture RM3 where y_rm3 = [yC, yH, yO]

    Returns
    -------
    ax : Axes
        The Matplotlib axes for the plot figure
    """

    ax.plot(yc, yh, '^', label='biomass')

    ax.plot(0.4444, 0.0617, 'o')
    ax.annotate('cell', xy=(0.4444, 0.0617), xytext=(-10, 6), textcoords='offset points')

    ax.plot(0.4545, 0.0606, 'o')
    ax.annotate('hemi', xy=(0.4545, 0.0606), xytext=(-10, -12), textcoords='offset points')

    ax.plot(0.6977, 0.0543, 'o')
    ax.annotate('ligc', xy=(0.6977, 0.0543), xytext=(-10, -12), textcoords='offset points')

    ax.plot(0.6055, 0.0642, 'o')
    ax.annotate('ligh', xy=(0.6055, 0.0642), xytext=(-10, 6), textcoords='offset points')

    ax.plot(0.5687, 0.0521, 'o')
    ax.annotate('ligo', xy=(0.5687, 0.0521), xytext=(-10, -12), textcoords='offset points')

    ax.plot(0.5921, 0.0395, 'o')
    ax.annotate('tann', xy=(0.5921, 0.0395), xytext=(-10, -12), textcoords='offset points')

    ax.plot(0.7634, 0.1116, 'o')
    ax.annotate('tgl', xy=(0.7634, 0.1116), xytext=(-6, -12), textcoords='offset points')

    x = 0.4444, 0.5921, 0.6977, 0.7634
    y = 0.0617, 0.0395, 0.0543, 0.1116
    ax.fill(x, y, '0.8', alpha=0.5)

    ax.plot(y_rm1[0], y_rm1[1], 's', label='rm1')
    ax.plot(y_rm2[0], y_rm2[1], 's', label='rm2')
    ax.plot(y_rm3[0], y_rm3[1], 's', label='rm3')

    x = y_rm1[0], y_rm2[0], y_rm3[0], y_rm1[0]
    y = y_rm1[1], y_rm2[1], y_rm3[1], y_rm1[1]
    ax.plot(x, y, 'k:')

    ax.grid(color='0.9')
    ax.set_axisbelow(True)
    ax.set_frame_on(False)
    ax.set_xlabel('Carbon mass fraction, daf basis [-]')
    ax.set_ylabel('Hydrogen mass fraction, daf basis [-]')
    ax.tick_params(color='0.9')
    ax.legend(frameon=False)

    return ax
