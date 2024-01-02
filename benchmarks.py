"""
Benchmarks.
"""

import time
import chemics as cm


def run_benchmarks():
    """
    Run benchmarks for Gas methods.

    Run benchmarks for Gas heat capacity, thermal conductivity, and viscosity
    methods. Elapsed time for subsequent method calls should be near zero
    compared to the initial method execution.
    """
    gas = cm.Gas("CH4", 890.5, 120325)

    for i in range(5):
        tic = time.perf_counter()
        cp = gas.heat_capacity()
        toc = time.perf_counter()
        print(f"Run {i + 1}, Elapsed time {toc - tic:.4f} s, cp {cp:.4f}")
    print()

    for i in range(5):
        tic = time.perf_counter()
        k = gas.thermal_conductivity()
        toc = time.perf_counter()
        print(f"Run {i + 1}, Elapsed time {toc - tic:.4f} s, k {k:.4f}")
    print()

    for i in range(5):
        tic = time.perf_counter()
        mu = gas.viscosity()
        toc = time.perf_counter()
        print(f"Run {i + 1}, Elapsed time {toc - tic:.4f} s, mu {mu:.4f}")


def main():
    """
    Run the benchmarks.
    """
    run_benchmarks()


if __name__ == "__main__":
    main()
