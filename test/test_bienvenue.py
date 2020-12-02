import bienvenue.bienvenue as b

def test_message_nom_simple():
    assert b.message("Bob")=="Hello, Bob."
    assert b.message("michel") == "Hello, Michel."

def test_message_vide():
    assert b.message("") == "Hello, my friend."
    assert b.message("   ") == "Hello, my friend."
    assert b.message("  ") == "Hello, my friend."
    assert b.message("  bob") != "Hello, my friend."

def test_message_cris_nom_simple():
    assert b.message("JERRY") == "HELLO, JERRY !"
    assert b.message("MICHEL") == "HELLO, MICHEL !"

def test_message_noms_liste():
    assert b.message("Amy,bob") == "Hello, Amy and Bob."
    assert b.message("Bob,Michel") == "Hello, Bob and Michel."
    assert b.message("Bob,Michel,denis,jacky") == "Hello, Bob, Michel, Denis and Jacky."

def test_message_liste_avec_cris():
    assert b.message("Amy,BOB,jerry") == "Hello, Amy and Jerry. AND HELLO, BOB !"
    assert b.message("MICHEL,Amy,BOB,jerry") == "Hello, Amy and Jerry. AND HELLO, MICHEL AND BOB !"



