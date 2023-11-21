def obtener_dict_peliculas_por_año():
    archivo = open("IMDB Top 250 Movies.txt", "r")
    D = {
        "[1970-1979]": [],
        "[1980-1989]": [],
        "[1990-1999]": [],
        "[2000-2009]": [],
        "[2010-2019]": [],
    }
    for lineas in archivo:
        palabras = lineas.split(",")
        # [nombre, score, año]
        Lpelicula = [palabras[1], palabras[3].strip("\n"), palabras[2]]
        if 1970 <= int(Lpelicula[2]) <= 1979:
            D["[1970-1979]"].append(Lpelicula)
        if 1980 <= int(Lpelicula[2]) <= 1989:
            D["[1980-1989]"].append(Lpelicula)
        if 1990 <= int(Lpelicula[2]) <= 1999:
            D["[1990-1999]"].append(Lpelicula)
        if 2000 <= int(Lpelicula[2]) <= 2009:
            D["[2000-2009]"].append(Lpelicula)
        if 2010 <= int(Lpelicula[2]) <= 2019:
            D["[2010-2019]"].append(Lpelicula)
    archivo.close()
    return D

def obtener_mejores_peliculas(D):
    assert type(D) == dict
    Dnueva = {
        "[1970-1979]": [],
        "[1980-1989]": [],
        "[1990-1999]": [],
        "[2000-2009]": [],
        "[2010-2019]": [],
    }
    for pelicula1 in D.values():
        score1 = float(pelicula1[1])
        nombre1 = pelicula1[0]
        año1 = int(pelicula1[2])
        for pelicula2 in D.values():
            score2 = float(pelicula2[1])
            nombre2 = pelicula2[0]
            año2 = int(pelicula2[2])
            if 1970 <= año1 <= 1979 and 1970 <= año2 <= 1979:
                if score2 < score1:
                    Dnueva["[1970-1979]"].append(nombre1)
                else:
                    Dnueva["[1970-1979]"].append(nombre2)
            if 1980 <= año1 <= 1989 and 1980 <= año2 <= 1989:
                if score2 < score1:
                    Dnueva["[1980-1989]"].append(nombre1)
                else:
                    Dnueva["[1980-1989]"].append(nombre2)
            if 1990 <= año1 <= 1999 and 1990 <= año2 <= 1999:
                if score2 < score1:
                    Dnueva["[1990-1999]"].append(nombre1)
                else:
                    Dnueva["[1990-1999]"].append(nombre2)
            if 2000 <= año1 <= 2009 and 2000 <= año2 <= 2009:
                if score2 < score1:
                    Dnueva["[2000-2009]"].append(nombre1)
                else:
                    Dnueva["[2000-2009]"].append(nombre2)
            if 2010<= año1 <= 2019 and 2010 <= año2 <= 2019:
                if score2 < score1:
                    Dnueva["[2010-2019]"].append(nombre1)
                else:
                    Dnueva["[2010-2019]"].append(nombre2)
    return Dnueva


D = obtener_dict_peliculas_por_año()
assert obtener_mejores_peliculas(D) == {
    "[1970-1979]": "The Godfather",
    "[1980-1989]": "Star Wars: Episode V - The Empire Strikes Back",
    "[1990-1999]": "The Shawshank Redemption",
    "[2000-2009]": "The Dark Knight",
    "[2010-2019]": "Inception",
}



def obtener_scores_promedio(D):
    # implemente su función aquí
    pass # <- borre esto

D = obtener_dict_peliculas_por_año()
assert obtener_scores_promedio(D) == {
    "[1970-1979]": 8.342,
    "[1980-1989]": 8.281,
    "[1990-1999]": 8.395,
    "[2000-2009]": 8.302,
    "[2010-2019]": 8.258,
}



def obtener_mejores_años(D):
    # implemente su función aquí
    pass # <- borre esto

D = obtener_dict_peliculas_por_año()
assert obtener_mejores_años(D) == ["[1990-1999]", 8.395]
