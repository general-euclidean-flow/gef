"""
GEF - Iris
2025-01-23
"""

import math

# ln(M_Pl/M_f) = (1/9)[Σ 1/α]
# where M_f ≈ 234.5 MeV
# Both sides ≈ 45.2

# Constants
M_Pl_eV = 1.220890e28      # SM Planck mass in eV
M_f_eV = 234.5e6           # Iris in eV

# Running fine structure constant at lepton masses
alpha_m_e = 1 / 137.036    # at electron mass
alpha_m_mu = 1 / 135.9     # at muon mass  
alpha_m_tau = 1 / 133.5    # at tau mass

def lhs():
    """Left side: ln(M_Pl / M_f)"""
    return math.log(M_Pl_eV / M_f_eV)

def rhs():
    """Right side: (1/9) * [1/α(mₑ) + 1/α(m_μ) + 1/α(m_τ)]"""
    return (1/9) * (1/alpha_m_e + 1/alpha_m_mu + 1/alpha_m_tau)

if __name__ == "__main__":
    lhs_val = lhs()
    rhs_val = rhs()

    print("Results:")
    print(f"  LHS: ln(M_Pl/M_f) = {lhs_val:.4f}")
    print(f"  RHS: (1/9)[Σ 1/α] = {rhs_val:.4f}")
    print(f"  Δ: {abs(lhs_val - rhs_val) / abs(lhs_val) * 100:.2f}%")
