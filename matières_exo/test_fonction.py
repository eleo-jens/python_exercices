from random import randint

def say_hello(n_min, n_max):
    # ici on rajoute une protection au sein meme du code pour contrer une mauvaise utilisation de la fonction par exemple en mettant say_hello(10,1)
    if n_min > n_max:
        temp = n_min
        n_min = n_max
        n_max = temp
        # n_min, n_max = n_max, n_min raccourcis pour inverser mais seulement en python
    r = randint(n_min, n_max)
    txt = ""
    for _ in range(r):
        txt += "Hello "
    return (txt)