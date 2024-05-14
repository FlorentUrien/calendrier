import random

chiffres = [0, 1, 2, 3, 4, 5, 6, 7, 8]
cubes = []


def enlever_chiffres(tableau: list[int], nb: int) -> tuple:
    """
    Enlève du 'tableau', 'nb' chiffres aléatoirement
    :param tableau : Le tableau d'entrée
    :param nb : le nombre de chiffres à enlever aléatoirement
    :return : Le tableau final et le tableau des valeurs enlevées
    """
    r = len(tableau)
    ret = tableau.copy()
    enl = []
    for i in range(1, nb + 1):
        a = random.randint(0, r - i)
        v = ret[a]
        enl.append(v)
        ret.remove(v)

    return ret, enl


def tirage_cubes() -> list[int]:
    """
    Tire au sort la valeur des deux cubes
    :return: cube[0] et cube[1]
    """
    ret = []
    r, e = enlever_chiffres(chiffres, 3)
    ret.append(r)
    r, e = enlever_chiffres(chiffres, 3)
    ret.append(r)

    return ret


def donne_faces(date: int) -> list[int]:
    """
    A partir d'une date, on donne les faces dont on a besoin.

    Par exemple: 8 -> [0, 8]

    A noter qu'on n'a pas de '9' car c'est un '6' inversé donc : 9 -> [0, 6]
    :param date: La date à tester
    :return: La liste des faces
    """
    faces = []
    if date < 10:
        faces.append(0)
    else:
        if date < 20:
            faces.append(1)
        else:
            if date < 30:
                faces.append(2)
            else:
                faces.append(3)
    unite = date % 10
    if unite == 9:
        unite = 6
    faces.append(unite)

    return faces


def date_ok(cubes: list[int], date: int) -> bool:
    """
    On vérifie que la date est compatible avec les cubes disponibles
    :param cubes: Les deux cubes et leurs faces
    :param date: La date à écrire
    :return: True si c'est possible.
    """
    faces = donne_faces(date)

    for i in range(0, 2):
        for j in range(0, 2):
            no = (i + j) % 2
            if faces[0] in cubes[no]:
                if faces[1] in cubes[(no + 1) % 2]:
                    return True
    return False


def fin(cubes: list[int]) -> int:
    """
    A partir des cubes voir jusqu'où l'on peut écrire une date.
    :param cubes: Les cubes
    :return: La date maximale atteignable
    """
    for i in range(1, 32):
        if not date_ok(cubes, i):
            return i - 1
    return 31


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nb_essais = 0
    for i in range(0, 10):
        record = 0
        while record < 31:
            nb_essais += 1
            cubes = tirage_cubes()
            nb = fin(cubes)
            if nb > record:
                record = nb
                if i == 0:
                    print(nb_essais, ": ", nb, ", ", cubes)
            else:
                div = 1000000
                if nb_essais % div == 0:
                    print(nb_essais / div, " M")
            if record == 31 and i > 0:
                print(nb_essais, ": ", nb, ", ", cubes)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
