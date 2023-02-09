# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define C = Character("Connie")
define D = Character("Dr. Morgana")
define Q = Character("???")
$ timer_range = 0
$ time = 0
# The game starts here.
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen countdown:

    bar value time range timer_range xalign 0 yalign 1 xmaximum 300 at alpha_dissolve

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
    
    Q "Is this Connie\?"
    

    menu:

        "Yeah":
            jump choice1_yes

        "Who wants to know\?":
            jump choice1_no
    
            label choice1_yes:
             
                $ menu_flag = True

                Q "PERFECT\!"
            label choice3_no:
                D "My name is Dr. Morgana"
                D "Are you alright\?"
                
                menu:

                    "I'm fine":
                        jump choice2_yes

                    "My head is a lil fuzzy":
                        jump choice2_no
                       
                        label choice2_yes:

                            $ menu_flag = True

                            D "Doesn't seem like it according to your vitals"

                            jump timerintro

                        label choice2_no:
                           
                            $ menu_flag = False
                           
                            D "Well that would make a lot of sense based on your vitals"

                            jump timerintro

                jump choice1_done

            label choice1_no:
                
                $ menu_flag = False

                Q "Listen I don\'t have time to play around I need to reach Connie aboard the Astromorbus"
                Q "IS THAT YOU\?"
                    
            menu:
                        
                "Yeah, it's me":
                    jump choice1_yes
                "What do you want\?":
                    jump choice3_no

                


    jump choice1_done

label timerintro:
    
    label menu1:
        $ time = 3
        $ timer_range = 3
        show screen countdown

    label timertest:

    D "TIMER TEST"

    menu:
        "Lose Time":
            jump timeloss

    label timeloss:
        $ time = time - 1
        jump timertest

    
              

    label choice1_done:
    


    # This ends the game.
    return
