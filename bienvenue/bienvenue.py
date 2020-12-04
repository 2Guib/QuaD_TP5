from collections import OrderedDict


def message(noms):
    if len(noms.strip()) == 0:
        return "Hello, my friend."

    message = ""

    dict_nom_min = tab_noms_min(noms)
    dict_nom_maj = tab_noms_maj(noms)

    if len(dict_nom_min) == 0 and len(dict_nom_maj) > 5:
        return "HELLO, WORLD !"
    if len(dict_nom_min) + len(dict_nom_maj) > 5:
        return "Hello, world !"
    if not isYoda(dict_nom_min, dict_nom_maj):
        if len(dict_nom_min) != 0:
            message += "Hello, "
            message += getListeNomMin(dict_nom_min)
            message += "."

        if len(dict_nom_maj) != 0:
            if len(dict_nom_min) == 0:
                message += "HELLO, "
            else:
                message += " AND HELLO, "
            message += getListeNomMaj(dict_nom_maj)
            message += " !"
    else:
        if len(dict_nom_maj) != 0:
            inv_maj = OrderedDict(reversed(dict_nom_maj.items()))
            message += getListeNomMaj(inv_maj)
            if len(dict_nom_min) == 0:
                message += ", HELLO !"
            else:
                message += ", HELLO AND "

        if len(dict_nom_min) != 0:
            inv_min = OrderedDict(reversed(dict_nom_min.items()))
            message += getListeNomMin(inv_min)
            message += ", Hello."

    return message


def isYoda(dict_nom_min, dict_nom_maj):

    for nom, nb in dict_nom_min.items():
        if nom.title() == "Yoda":
            return True
    for nom, nb in dict_nom_maj.items():
        if nom.upper() == "YODA":
            return True
    return False


def getListeNomMin(dict_nom):
    message = ""
    list_nom = list(dict_nom.keys())
    if len(dict_nom) == 1:
        message += list_nom[0].title() + nbNom(dict_nom, list_nom[0])
    else:
        for i in range(len(dict_nom)):
            if i == len(dict_nom) - 1:
                message = message[0:-2] + " and " + list_nom[i].title()
                message += nbNom(dict_nom, list_nom[i])
            else:
                message += list_nom[i].title()
                message += nbNom(dict_nom, list_nom[i])
                message += ', '
    return message


def getListeNomMaj(dict_nom_maj):
    message = ""
    list_nom_maj = list(dict_nom_maj.keys())
    if len(dict_nom_maj) == 1:
        message += list_nom_maj[0] + nbNom(dict_nom_maj, list_nom_maj[0])
    else:
        for i in range(len(dict_nom_maj)):
            if i == len(dict_nom_maj) - 1:
                message = message[0:-2] + " AND " + list_nom_maj[i]
                message += nbNom(dict_nom_maj, list_nom_maj[i])
            else:
                message += list_nom_maj[i]
                message += nbNom(dict_nom_maj, list_nom_maj[i])
                message += ', '
    return message


def nbNom(dict_nom, nom):
    if (dict_nom[nom] > 1):
        return " (x" + str(dict_nom[nom]) + ")"
    return ""


def tab_noms_min(noms):
    dict_nom = {}
    tab_nom_ignore = []
    nom = ""
    for i in range(len(noms)):
        if noms[i] == ',' or i == len(noms) - 1:
            if i == len(noms) - 1:
                if noms[i] != " ":
                    nom += noms[i]

            if nom != nom.upper():
                if nom[0] == '!':
                    tab_nom_ignore.append(nom[1:].upper())
                    nom = nom[1:]
                if nom in dict_nom.keys():
                    dict_nom[nom] += 1
                else:
                    dict_nom[nom] = 1
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]

    for ignore in tab_nom_ignore:
        i = 0
        while i < len(dict_nom):
            if ignore == list(dict_nom.keys())[i].upper():
                del dict_nom[list(dict_nom.keys())[i]]
                i -= 1
            i += 1
    return dict_nom


def tab_noms_maj(noms):
    dict_nom = {}
    tab_nom_ignore = []
    nom = ""
    for i in range(len(noms)):
        if noms[i] == ',' or i == len(noms) - 1:
            if i == len(noms) - 1:
                if noms[i] != " ":
                    nom += noms[i]

            if nom == nom.upper():
                if nom[0] == '!':
                    tab_nom_ignore.append(nom[1:].upper())
                    nom = nom[1:].upper()
                if nom in dict_nom.keys():
                    dict_nom[nom] += 1
                else:
                    dict_nom[nom] = 1
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]

    for ignore in tab_nom_ignore:
        i = 0
        while i < len(dict_nom):
            if ignore == list(dict_nom.keys())[i].upper():
                del dict_nom[list(dict_nom.keys())[i]]
                i -= 1
            i += 1

    return dict_nom
