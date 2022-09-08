"""
Estimate biomass composition from ultimate analysis values. Plot the
calculated biomass composition along with the associated reference mixtures.
Example 1 uses the default values for the splitting parameters. Example 2
demonstrates the adjusting the `epsilon` splitting parameter to properly
characterize the biomass; otherwise, the calculated composition values will be
negative.
"""

import matplotlib.pyplot as plt
import chemics as cm

# --- Example 1 --------------------------------------------------------------

# Carbon and hydrogen mass fractions from ultimate analysis
yc = 0.534
yh = 0.06

# Calculate biomass composition and print results
bc = cm.biocomp(yc, yh, printcomp=True)

# Plot the reference mixtures
fig, ax = plt.subplots(tight_layout=True)
cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

# --- Example 2 --------------------------------------------------------------

# Carbon and hydrogen mass fractions from ultimate analysis
yc = 0.51
yh = 0.057

# Calculate biomass composition and print results

# Use the default splitting parameter values. This will result in negative
# composition values for the given C and H fractions. Therefore the splitting
# parameters need to be adjusted to properly characterize the biomass.
bc = cm.biocomp(yc, yh, printcomp=True)

# Adjust the `epsilon` splitting parameter to properly characterize the
# biomass for the given C and H mass fractions. Comment the previous `bc` line
# and uncomment this line to see the results and associated plot.
# bc = cm.biocomp(yc, yh, epsilon=0.4, printcomp=True)

# Plot the reference mixtures
fig, ax = plt.subplots(tight_layout=True)
cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

plt.show()
