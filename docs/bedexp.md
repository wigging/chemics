# Bed expansion factor

Brief summary goes here.

## Equation

Math equation goes here.

$$
\frac{n!}{k!(n-k)!} = \binom{n}{k}
$$

Inline math here $x^2 + s$.

## Reference

Goes here.

## Example

Example python code here.

```python
import chemics as cm

# Parameters
#------------------------------------------------------------------------------

umf = 0.1157    # minimum fluidization velocity, m/s
us = 3.0*umf    # superficial gas velocity, m/s
db = 0.05232    # bed diameter, m
zmf = 0.1016    # bed height at minimum fluidizaiton, m
emf = 0.46      # void fraction at minimum fluidization
rhop = 2500     # density of bed particle, kg/m^3
dp = 0.0004     # diameter of bed particle, m
g = 9.81        # gravity, m/s^2
rhog = 0.4413   # density of gas, kg/m^3

# Bed Expansion Calculations
#------------------------------------------------------------------------------

# bed expansion factor, fbexp (-)
fbexp = cm.fbexp(db, dp, rhog, rhop, umf, us)

# fluidized bed height, zf (m)
zf = zmf*fbexp

# fluidized void fraction of bed from Eq 14.18, ef (-)
ef = 1 - (1-emf)/fbexp

```

Gives the following results:

```
zmf (m) = 0.1016
emf = 0.46
fbexp = 1.4864346912670614
zf (m) = 0.15102176463273342
ef = 0.6367146143906968
```
