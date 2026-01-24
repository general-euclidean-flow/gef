"""
GEF - Equilibrium
2025-01-23
"""

# E_ZPE = (1/2) * m_0 * c^2
# The zero-point energy of any particle equals exactly half its rest mass energy.

def zero_point_energy(rest_mass_kg):
    """
    E_ZPE = ½m₀c²
    """
    c = 299_792_458  # m/s
    return 0.5 * rest_mass_kg * c**2

if __name__ == "__main__":
    print(zero_point_energy(1))