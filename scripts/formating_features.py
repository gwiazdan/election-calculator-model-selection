def format_scientific_notation(n):
    """Formatuje liczbę do notacji naukowej w formacie LaTeX."""
    # Użyj formatowania :.2e, aby uzyskać string np. "1.23e+25"
    s = f"{n:.2e}"
    # Podziel string na część przed 'e' (mantysa) i po 'e' (wykładnik)
    mantissa, exponent = s.split('e')
    # Zamień wykładnik na liczbę całkowitą
    exponent_val = int(exponent)
    # Zwróć string w formacie LaTeX
    return f"{mantissa} \\times 10^{{{exponent_val}}}"

def format_time(n):
    if n >= 1:
        return f"{n:.2f} s"
    elif n >= 1e-3:  # 0.001 s = 1 ms
        return f"{n * 1e3:.2f} ms"
    elif n >= 1e-6:  # 0.000001 s = 1 µs
        return f"{n * 1e6:.2f} µs"
    else:
        return f"{n * 1e9:.2f} ns"