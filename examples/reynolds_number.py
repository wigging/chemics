"""
Examples of using the Reynolds number function.
"""

import chemics as cm

# Example 1
# ---------------------------------------------------------------------------

u = 2.6         # flow speed in m/s
d = 0.025       # characteristic length or dimension in meters
ρ = 910         # density of the fluid or gas in kg/m³
μ = 0.38        # dynamic viscosity of the fluid or gas in kg/(m⋅s)

re = cm.reynolds(u, d, rho=ρ, mu=μ)
print(f're = {re:.4f}')

# Example 2
# ---------------------------------------------------------------------------

u = 0.25        # flow speed in m/s
d = 0.102       # characteristic length or dimension in meters
𝒗 = 1.4e-6      # kinematic viscosity of the fluid or gas in m²/s

re = cm.reynolds(u, d, nu=𝒗)
print(f're = {re:.4f}')
