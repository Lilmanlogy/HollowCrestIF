# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define C = Character("Connie")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    C "Gah!"
     
    scene bg conniewake
    with Dissolve(1)
    

    C "\*sniff\* Oh no\!"
    "\*bzz\* \*bzz\*"
    C "Gotta check the coms"

    scene doctorcall
    
    C "YO WHAT IS UP YOU BAD BITCH READY TO GET FUNKY\!"

    


    # This ends the game.
    return
