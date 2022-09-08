"""
Plot the Geldart particle classification based on gas density, solid density,
and mean particle diameter.
"""

import chemics as cm
import matplotlib.pyplot as plt

dp = 300
dpmin = 100
dpmax = 500
rhog = 0.1
rhos = 2.5

cm.geldart_chart(dp, rhog, rhos)
cm.geldart_chart(dp, rhog, rhos, dpmin, dpmax)

plt.show()
