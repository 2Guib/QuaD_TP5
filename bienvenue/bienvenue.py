from collections import OrderedDict


def message(noms):
    if len(noms.strip()) == 0:
        return "Hello, my friend."

    message = ""

    dict_nom_min = tab_noms_min(noms)
    dict_nom_maj = tab_noms_maj(noms)

    if not isYoda(dict_nom_min, dict_nom_maj):
        if len(dict_nom_min) == 0 and len(dict_nom_maj) > 5:
            return "HELLO, WORLD !"
        if len(dict_nom_min) + len(dict_nom_maj) > 5:
            return "Hello, world !"
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
        if len(dict_nom_min) == 0 and len(dict_nom_maj) > 5:
            return "WORLD, HELLO !"
        if len(dict_nom_min) + len(dict_nom_maj) > 5:
            return "World, Hello !"
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

def isGuest(nom):
    return nom[0] == '*' and nom[len(nom) - 1] == '*'

def nbGuest(dict_nom):
    compteur_guest = 0
    for nom, nb in dict_nom.items():
        if isGuest(nom):
            compteur_guest += 1

    return compteur_guest

def clearGuest(nom):
    if isGuest(nom):
        nom = nom[1:]
        nom = nom[:-1]

    return nom


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
        nom = list_nom[0].title()
        if isGuest(nom):
            nom = nom[1:]
            nom = nom[:-1]
            nom = "our special guest " + nom
        message += nom + nbNom(dict_nom, list_nom[0])
    else:
        tab_guest = []
        for i in range(len(dict_nom)):
            if isGuest(list_nom[i]):
                tab_guest.append(list_nom[i])
        nb_guest = len(tab_guest)
        if nb_guest > 0:
            guest = tab_guest[0]
            if nb_guest <= 1:
                guest = clearGuest(guest)
                message += "our special guest " + guest
            else:
                message += "our special guests"
                for guest in tab_guest:
                    guest = clearGuest(guest)
                    message += guest + " & "
                message = message[:-3]
            message += ', '
        i = 0
        while i < len(dict_nom) - nb_guest:
            nom = list_nom[i]
            if not isGuest(nom):
                if i == len(dict_nom) - nb_guest - 1:
                    if len(dict_nom) - nb_guest >1:
                        message = message[0:-2]
                    else:
                        message = message[0:-1]
                    message2 = message + " amd "
                    message2 += nom
                    message = message2+nbNom(dict_nom, list_nom[i])
                else:
                    message += nom
                    message += nbNom(dict_nom, list_nom[i])
                    message += ', '
                i += 1
    return message


def getListeNomMaj(dict_nom_maj):
    message = ""
    list_nom_maj = list(dict_nom_maj.keys())
    if len(dict_nom_maj) == 1:
        nom = list_nom_maj[0]
        if isGuest(nom):
            nom = nom[1:]
            nom = nom[:-1]
            nom = "OUR SPECIAL GUEST " + nom
        message += nom + nbNom(dict_nom_maj, list_nom_maj[0])
    else:
        for i in range(len(dict_nom_maj)):
            nom = list_nom_maj[i]
            if isGuest(nom):
                nom = nom[1:]
                nom = nom[:-1]
                nom = "OUR SPECIAL GUEST " + nom
            if i == len(dict_nom_maj) - 1:
                message = message[0:-2] + " AND " + nom
                message += nbNom(dict_nom_maj, list_nom_maj[i])
            else:
                message += nom
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
                if nom.title() in dict_nom.keys():
                    dict_nom[nom.title()] += 1
                else:
                    dict_nom[nom.title()] = 1
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]

    for ignore in tab_nom_ignore:
        i = 0
        while i < len(dict_nom):
            nom = list(dict_nom.keys())[i].upper()
            if isGuest(nom):
                nom = nom[1:]
                nom = nom[:-1]
            if ignore == nom:
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
            nom=list(dict_nom.keys())[i].upper()
            if isGuest(nom):
                nom = nom[1:]
                nom = nom[:-1]
            if ignore == nom:
                del dict_nom[list(dict_nom.keys())[i]]
                i -= 1

            i += 1

    return dict_nom
