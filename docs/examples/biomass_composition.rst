Biomass composition
===================

The ``biocomp()`` function uses ultimate analysis data to estimate biomass composition in terms of cellulose, hemicellulose, lignins, and extractives. The example below uses the carbon ``yc`` and hydrogen ``yh`` mass fractions from ultimate analysis data to calculate the cellulose mass fraction on a dry ash-free basis.

.. doctest::

   >>> yc = 0.534
   >>> yh = 0.06
   >>> bc = cm.biocomp(yc, yh)
   >>> bc['y_daf'][0]
   0.293...

The entire biomass composition can be printed to the screen with ``printcomp=True``.

.. doctest::
   :options: +NORMALIZE_WHITESPACE

   >>> bc = cm.biocomp(yc, yh, printcomp=True)
   basis    cell    hemi    ligc    ligh    ligo    tann    tgl
   x_daf    0.4118  0.2745  0.0627  0.1529  0.0981  0.0000  0.0000
   x_wet    0.4118  0.2745  0.0627  0.1529  0.0981  0.0000  0.0000
   y_daf    0.2936  0.1595  0.0713  0.2934  0.1822  0.0000  0.0000
   y_wet    0.2936  0.1595  0.0713  0.2934  0.1822  0.0000  0.0000
   y_wetash 0.2936  0.1595  0.0713  0.2934  0.1822  0.0000  0.0000

Use the ``plot_biocomp()`` function to plot the biomass (triangle symbol) in relation to the reference mixtures (square symbols) as shown below.

.. plot::
   :width: 500 px

   # Carbon and hydrogen mass fractions from ultimate analysis
   yc = 0.534
   yh = 0.06

   # Calculate the biomass composition
   bc = cm.biocomp(yc, yh)

   # Plot the biomass and reference mixtures
   fig, ax = plt.subplots(tight_layout=True)
   cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

   plt.show()

Notice that the C and H mass fractions may give negative biomass composition values when the default splitting parameters are used as shown below. This is also depicted by the biomass marker going outside the bounds (dashed triangle) of the reference mixtures.

.. doctest::
   :options: +NORMALIZE_WHITESPACE

   >>> yc = 0.51
   >>> yh = 0.057
   >>> _ = cm.biocomp(yc, yh, printcomp=True)
   basis    cell    hemi    ligc    ligh     ligo    tann    tgl
   x_daf    0.4534  0.3023  0.0489  -0.0106  0.2061  0.0000  -0.0000
   x_wet    0.4534  0.3023  0.0489  -0.0106  0.2061  0.0000  -0.0000
   y_daf    0.3527  0.1916  0.0605  -0.0223  0.4175  0.0000  -0.0000
   y_wet    0.3527  0.1916  0.0605  -0.0223  0.4175  0.0000  -0.0000
   y_wetash 0.3527  0.1916  0.0605  -0.0223  0.4175  0.0000  -0.0000

.. plot::
   :width: 500 px

   yc = 0.51
   yh = 0.057
   bc = cm.biocomp(yc, yh)

   fig, ax = plt.subplots(tight_layout=True)
   cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

   plt.show()

In this particular case, adjust the ``epsilon`` splitting parameter to properly characterize the biomass for the C and H mass fractions.

.. doctest::
   :options: +NORMALIZE_WHITESPACE

   >>> yc = 0.51
   >>> yh = 0.057
   >>> _ = cm.biocomp(yc, yh, epsilon=0.4, printcomp=True)
   basis    cell    hemi    ligc    ligh    ligo    tann    tgl
   x_daf    0.4623  0.3082  0.0259  0.0504  0.0532  0.0998  0.0000
   x_wet    0.4623  0.3082  0.0259  0.0504  0.0532  0.0998  0.0000
   y_daf    0.3800  0.2064  0.0339  0.1116  0.1140  0.1540  0.0000
   y_wet    0.3800  0.2064  0.0339  0.1116  0.1140  0.1540  0.0000
   y_wetash 0.3800  0.2064  0.0339  0.1116  0.1140  0.1540  0.0000

.. plot::
   :width: 500 px

   yc = 0.51
   yh = 0.057
   bc = cm.biocomp(yc, yh, epsilon=0.4)

   fig, ax = plt.subplots(tight_layout=True)
   cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

   plt.show()