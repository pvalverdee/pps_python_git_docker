# bayeta.py

def frotar(n_frases: int = 1) -> list:
    return ["Frase auspiciosa"] * n_frases

import random

def frotar(n_frases: int = 1) -> list:
    frases = ["Frase 1", "Frase 2", "Frase 3", "Frase 4", "Frase 5"]  # Lista de frases auspiciosas
    return random.sample(frases, k=n_frases)
