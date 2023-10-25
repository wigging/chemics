import chemics as cm


def main():
    """
    This example calculates the viscosity of a gas mixture.
    """
    gas1 = cm.Gas('H2', 773)
    gas2 = cm.Gas('N2', 773)
    gas3 = cm.Gas('CH4', 825)

    gas_mixture = cm.GasMixture([gas1, gas2, gas3], [0.4, 0.1, 0.5])

    mu_mixture = gas_mixture.viscosity()

    print(f'gas mixture viscosity is {mu_mixture:.2f} µP')


if __name__ == '__main__':
    main()
