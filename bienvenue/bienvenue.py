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
    tab_nom_ingnore = []
    nom = ""
    for i in range(len(noms)):
        if noms[i] == ',' or i == len(noms) - 1:
            if i == len(noms) - 1:
                if noms[i] != " ":
                    nom += noms[i]

            if nom != nom.upper():
                if nom[0] == '!':
                    tab_nom_ingnore.append(nom[1:].upper())
                    nom = nom[1:]
                tab_nom.append(nom)
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]


    for ignore in tab_nom_ingnore:
        i = 0
        while i < len(tab_nom):
            if ignore == tab_nom[i].upper():
                del tab_nom[i]
                i -= 1
            i += 1

    return tab_nom


def tab_noms_maj(noms):
    tab_nom = []
    tab_nom_ingnore = []
    nom = ""
    for i in range(len(noms)):
        if noms[i] == ',' or i == len(noms) - 1:
            if i == len(noms) - 1:
                if noms[i] != " ":
                    nom += noms[i]

            if nom == nom.upper():
                if nom[0] == '!':
                    tab_nom_ingnore.append(nom[1:].upper())
                    nom = nom[1:].upper()
                tab_nom.append(nom)
            nom = ""
        else:
            if noms[i] != " ":
                nom += noms[i]


    for ignore in tab_nom_ingnore:
        i = 0
        while i < len(tab_nom):
            if ignore == tab_nom[i].upper():
                del tab_nom[i]
                i -= 1
            i += 1

    return tab_nom
