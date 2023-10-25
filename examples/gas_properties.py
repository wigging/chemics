from textwrap import dedent
import chemics as cm


def get_gas_properties():
    """
    This example creates a Gas object that represents nitrogen gas (N2) at a
    temperature of 823.5 K and pressure of 120,500 Pa. The molecular weight,
    density, heat capacity, thermal conductivity, and viscosity of the gas
    are calculated for the given temperature and pressure.
    """
    gas = cm.Gas('N2', 823.5, 120500)

    mw = gas.molecular_weight
    rho = gas.density()
    cp = gas.heat_capacity()
    k = gas.thermal_conductivity()
    mu = gas.viscosity()

    results = gas, mw, rho, cp, k, mu
    return results


def main():
    """
    Run the example and print results.
    """
    gas, mw, rho, cp, k, mu = get_gas_properties()

    print(dedent(f"""
    Gas properties for N2 gas at {gas.temperature} K and {gas.pressure:,} Pa\n
    molecular weight        {mw:>10.4f} g/mol
    density, ρ              {rho:>10.4f} kg/m³
    heat capacity, Cp       {cp:>10.4f} J/(mol⋅K)
    thermal conductivity, k {k:>10.4f} W/(m⋅K)
    viscosity, μ            {mu:>10.4f} microPoise or μP"""))


if __name__ == '__main__':
    main()
