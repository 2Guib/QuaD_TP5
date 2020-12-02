def message(noms):
    if len(noms.strip()) == 0:
        return "Hello, my friend."

    message = ""

    tab_nom = tab_noms_min(noms)
    tab_nom_maj = tab_noms_maj(noms)

    if len(tab_nom) != 0:
        message += "Hello, "
        if len(tab_nom) == 1:
            message += tab_nom[0].title() + "."
        else:
            for i in range(len(tab_nom)):
                if i == len(tab_nom) - 1:
                    message = message[0:-2] + " and " + tab_nom[i].title()
                else:
                    message += tab_nom[i].title() + ", "
            message += "."

    if len(tab_nom_maj) != 0:
        if len(tab_nom) == 0:
            message += "HELLO, "
        else:
            message += " AND HELLO, "
        if len(tab_nom_maj) == 1:
            message += tab_nom_maj[0] + " !"
        else:
            for i in range(len(tab_nom_maj)):
                if i == len(tab_nom_maj) - 1:
                    message = message[0:-2] + " AND " + tab_nom_maj[i]
                else:
                    message += tab_nom_maj[i] + ", "
            message += " !"

    return message


def tab_noms_min(noms):
    tab_nom = []
    nom = ""
    for i in range(len(noms)):
        if noms[i] == ',':
            if nom != nom.upper():
                tab_nom.append(nom)
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]
    if nom != nom.upper():
        tab_nom.append(nom)

    return tab_nom


def tab_noms_maj(noms):
    tab_nom = []
    nom = ""
    for c in noms:
        if c == ',':
            if nom == nom.upper():
                tab_nom.append(nom)
            nom = ""
        else:
            if c != " ":
                nom += c
    if nom == nom.upper():
        tab_nom.append(nom)
    return tab_nom
