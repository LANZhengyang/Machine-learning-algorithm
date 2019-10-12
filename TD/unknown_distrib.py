import numpy as np
import pandas as pd

def polynom_sample(x, coefs, sigma=5):
    """Une fonction pour associer un vecteur y e un vecteur x avec 
    une relation polynomiale de coefficient coefs et un bruit gaussien 
    de variance sigma"""
    d = len(coefs) # le degre du polynome
    y = sigma*np.random.randn(*x.shape) # intialise avec bruit gaussien 
    for i in range(d): # accumule le calcul du polynome
        y = y + coefs[i]*( x**i) 
    return y 

def data_sample(N):
    """Une fonction qui genere un ensemble de donnees de taille N tirees d'un polynome particulier"""
    a = -5 # borne inf
    b = 5 # borne sup
    coefs = [0, 4.63235734e+00,  -6.39114341e+00,
             -6.32024032e-01,   1.89403935e+00,   1.17905282e-01,
             -2.11509996e-01,  -7.77580853e-03,   9.75144372e-03,
             1.59857817e-04,  -1.57464310e-04]
    x = (b-a)*np.random.random_sample(N) + a # N points tires uniformement de l'intervalle [a,b]
    y = polynom_sample(x, coefs)
    df = pd.DataFrame({"x":x,"y":y})
    return df