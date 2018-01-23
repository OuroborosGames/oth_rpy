# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Doggo")


# The game starts here.

init python:
    #import On-the-hill/oth_core
    #backend = oth_core.GameBackend()
    import sys
    sys.path.append(sys.argv[1] + "/game/On-the-hill/")
    sys.path.append(sys.argv[1] + "/compat/")
    import oth_core
    backend = oth_core.GameBackend()
    building = None
    x = "dupa"

label start:


    scene bg room
    #show screen chuj
    python:
        backend.new_game("Kielce",10,10)
        building = backend.buildings_deck[1]

    image cowescale = im.Scale("cowe.jpg", 400, 250)
    image doggoscale = im.Scale("doggo.jpg", 100, 150)
    # image doggowan = Text([building.name])
    call screen building_card(building) 
     
    image cardTemplate = LiveComposite(
        (500, 500),
        (0,0), "back.jpg",
        (50, 100), "cowescale",
        (100, 0), "doggowan")
    

    
    
    
    
    
    
    transform card_transform:
     ypos 700

    image cardTemplateTransform = At("cardTemplate", card_transform)
    
    show cardTemplateTransform
    

    # These display lines of dialogue.

    "Hello, world."

    d "Doggo wan the fishe"
    

    # This ends the game.

    return
