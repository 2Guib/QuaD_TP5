import bienvenue.bienvenue as b


def test_message_nom_simple():
    assert b.message("Bob") == "Hello, Bob."
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
    assert b.message("MICHEL,Amy,BOB,jerry,PATRICK") == "Hello, Amy and Jerry. AND HELLO, MICHEL, BOB AND PATRICK !"


def test_message_espace_inutiles():
    assert b.message("bob         ,amy") == "Hello, Bob and Amy."
    assert b.message("bob         ,amy,   PATRICK    ") == "Hello, Bob and Amy. AND HELLO, PATRICK !"


def test_message_exclamation():
    assert b.message("!bob,!amy,jerry") == "Hello, Jerry."
    assert b.message("!bob,amy,!jerry") == "Hello, Amy."
    assert b.message("bob,!bob,amy") == "Hello, Amy."
    assert b.message("bob,!bob,amy,jerry,MICHEL,JEAN,!MICHEL") == "Hello, Amy and Jerry. AND HELLO, JEAN !"


def test_message_doulons_nom():
    assert b.message("bob,bob") == "Hello, Bob (x2)."
    assert b.message("BOB,BOB") == "HELLO, BOB (x2) !"
    assert b.message("bob,jerry,amy,bob,amy,amy") == "Hello, Bob (x2), Jerry and Amy (x3)."
    assert b.message("bob,amy,bob") == "Hello, Bob (x2) and Amy."
    assert b.message("bob,amy,bob,!jerry,jerry") == "Hello, Bob (x2) and Amy."
    assert b.message("bob,BOB,BOB,BOB,amy,BOB") == "Hello, Bob and Amy. AND HELLO, BOB (x4) !"
    assert b.message("bob,bob,BOB,BOB,BOB,amy,BOB") == "Hello, Bob (x2) and Amy. AND HELLO, BOB (x4) !"

def test_message_plus_cinq_noms():

    assert b.message("MICHEL,Amy,BOB,jerry,PATRICK,jack") == "Hello, world !"

def test_message_plus_cinq_noms_MAJ():
    assert b.message("MICHEL,AMY,BOB,JERRY,PATRICK,JACK") == "HELLO, WORLD !"
    assert b.message("MICHEL,AMY,BOB,JERRY,PATRICK,JACK,denis") == "Hello, world !"

def test_message_yoda():
    assert b.message("amy,Bob,yoda,max") == "Max, Yoda, Bob and Amy, Hello."
    assert b.message("amy,bob,YODA,JERRY") == "JERRY AND YODA, HELLO AND Bob and Amy, Hello."
    assert b.message("JERRY,YODA,AMY") == "AMY, YODA AND JERRY, HELLO !"
    assert b.message("amy,Bob,!yoda,max") == "Hello, Amy, Bob and Max."

def test_message_yoda_plus_cinq():
    assert b.message("amy,Bob,yoda,max,MICHEL,denis") == "World, Hello !"
    assert b.message("AMY,BOB,YODA,MAX,MICHEL,DENIS") == "WORLD, HELLO !"

def test_special_guest():
    assert b.message("*bob*") == "Hello, our special guest Bob."
    assert b.message("*BOB*") == "HELLO, OUR SPECIAL GUEST BOB !"
    assert b.message("bob,*amy*,!amy") == "Hello, Bob."
    assert b.message("bob,*AMY*,!AMY") == "Hello, Bob."
    assert b.message("bob,*amy*,!AMY") == "Hello, Bob and our special guest Amy."
    assert b.message("bob,*amy*,jerry") == "Hello, Bob, our special guest Amy and Jerry."
    assert b.message("BOB,*AMY*,JERRY") == "HELLO, BOB, OUR SPECIAL GUEST AMY AND JERRY !"
    assert b.message("*bob*,*AMY*,jerry") == "Hello, our special guest Bob and Jerry. AND HELLO, OUR SPECIAL GUEST AMY !"
