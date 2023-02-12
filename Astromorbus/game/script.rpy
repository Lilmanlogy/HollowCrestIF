# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define C = Character("Connie")
define D = Character("Dr. Morgana")
define Q = Character("???")
$ timer_range = 0
$ time = 0
$ health_range = 0
$ health = 0


image Crewmate:
    "infectedcrewmate"
    zoom 1.5

# The game starts here.
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform alpha_dissolve2:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:

    bar value time range timer_range xalign 0 yalign 1 xmaximum 300 at alpha_dissolve

screen countdown2:

    vbar value health range health_range xalign 1.0 yalign 0 ymaximum 300 at alpha_dissolve2

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "audio/bg_music.wav"

    # These display lines of dialogue.

    C "Gah!"

    scene bg conniewake
    with Dissolve(1)



    C "What happened...my head feels...warm. Blood!?"
    Q "Co.....hea......me...?"
    C "Huh? The com is going off."

    scene doctorcall

    D "Captain! Can you hear me? Connie...Connie!?"
    C "Doctor! Yes, I can hear you loud and clear."
    D "Oh! Thank goodness, you are still coherent!"
    D "I was worried it already got you."
    C "Yes, I’m fine... wait, what do you mean got me already? "
    D "I do not have much time, so I’m not gonna sugarcoat this. One of the cargos we were transporting harbored a deadly virus. A crewmate was taking inventory and when they opened the container…the symptoms started fast."
    D "It’s a neural virus that infects the brain and mutates the body. It destroys any semblance of human thought and makes you really aggressive."
    D "A lot of the crew with weaker immune systems fell within minutes. I was worried since your immune compromised, that it would get you first."
    C "Am...Am I going to be ok?"
    D "I’ve thankfully been able to find some record of similar viruses and already synthesized a cure."
    D "Thank goodness we just blew our last paycheck on fully stocking the med bay"
    C "And here I thought it be wiser to upgrade the hyper…I’m getting sidetracked…"


    menu:

        "Ask about crew":
            jump choice1_crew

        "Ask about ship":
            jump choice1_ship

            label choice1_crew:

                $ menu_flag = True

                C "What's our casualty count?"
                D "About 85\% of our crew. Most crewmates on the lower floors went first. I was able to secure a lot of people in the med bay right away since it was a major lunch rush."
                D "I’ve tried to reach out to other areas, but you’re the only one who has responded."

                jump choice1_done



            label choice1_ship:

                $ menu_flag = False

                C "Why is the emergency alarm blaring? Did something happen to compromise the ship?"
                D "A fight between infected crewmates broke out earlier in the engine room. They hit one of the critical points of the main system and now a lot of major systems are going offline."

                jump choice1_done


            label choice1_done:

                D "Luckily, the emergency power should hold until we get the cure out. "
                C "Roger. And...how long do I have left?"

            label timerintro:

            label menu1:
                $ time = 10
                $ timer_range = 10
                show screen countdown

                D "You have 10 minutes left, Hurry to the med bay, and if you are coherent enough, I'll let you in and give you the cure"

    scene mainpath
    with Dissolve(.5)

    C "Damn it! Can I even make it through?"

    menu:
        "Head back to the elevator":
            jump scene2altpath

        "Squeeze through the cracks":
            jump scene2mainpath


    label scene2mainpath:
        $ time = time - 1

        if time == 0:
            jump infected

        C "In for a penny..."

        scene cafeteria
        show Crewmate
        with Dissolve(.5)

    C "There’s no way I can sneak around him!"
    C "Screw this, let’s do it head on!"


    $ health = 3
    $ health_range = 3
    show screen countdown2
    play music "audio/battle.wav"

    menu:
        "Punch":
            jump choice_punch

        "Throw Food Tray":
            jump choice_tray

        "Push Cafeteria Table":
            jump choice_table


    label choice_punch:
    $ time = time -1
    if time == 0:
       jump infected
    $ health = health - 1
    if health == 0:
       jump death
    "Connie throws a punch at the infected crewmate easily, which is easily deflected and sent back at her"
    C "Screw this! I'm heading to the elevator"

    jump scene2altpath

    label choice_tray:
    $ time = time -1
    if time == 0:
        jump infected
    "Connie tosses the tray at the infected crewmate, distracting him allowing her to escape back to the elevator"

    jump scene2altpath

    label choice_table:
    $ time = time -1
    if time == 0:
        jump infected
    C "C'mon you piece of junk"
    "Connie pushes the table into the infected crewmate, pinning him to the wall"
    hide Crewmate
    C "If it is any consolation...I am sorry"
    C "Phew"
    C "Right! The med bay is through here"

    jump medbay


    label scene2altpath:

    play music "audio/bg_music.wav" if_changed
    scene mainpath
    with Dissolve (1.0)

    C "I don't have the time to take the stairs."
    C "The med bay is on...on..."
    C "I can't remember, DAMN IT!"

    label floordecision:
    C "Well I guess I'll let lady luck guide me"

    menu:
        "Choose Floor 8":
            jump flooreight
        "Choose Floor 3":
            jump floorthree
        "Choose Floor 5":
            jump floorfive
        "Choose Floor B1":
            jump floorb

    label flooreight:
    $ time = time - 1
    if time == 0:
        jump infected
    C "UGH! Theres nothing in here. A literal time waster!"

    jump floordecision

    label floorthree:
    $ time = time - 1
    if time == 0:
        jump death
    show Crewmate
    C "Why me why today..."

    menu:
        "Run Away":
            hide Crewmate
            jump floordecision
        "Fight":
            jump fight

    label fight:
            $ health
            $ health_range = 3
            play music "audio/battle.wav"
            "Connie grabs a metal tube and whacks the crewmate with it knocking it out instantly"
            hide Crewmate
            C "Ok \*pants\* I should head...OW!"
            $ health = health - 1
            if health == 0:
                jump death
            show Crewmate
            "Another infected crew member rises up off the floor, but Connie takes another lucky swing"
            hide Crewmate
            C "ANYONE ELSE!? NO...that's what I thought"
            play music "audio/bg_music.wav"
            jump floordecision

    label floorfive:
        $ time = time - 1
        if time == 0:
            jump infected
        C "Another dead...wait... a map right! The med bay is back where I came from"
        C "And a ship manifesto"
        C "We made it back to the Andromeda System; the nearest port should only be an hour away"
        C "Hopefully we can get there soon after the chaos calms down"

        jump floordecision

    label floorb:
        $ time = time - 1
        if time == 0:
            jump infected
        C "The engine room is down this way...I think..."
        C "I can't remember my own ship, what the hell!"
        C "Oh! Up ahead!"

        jump medbay

    label medbay:
        play music "audio/bg_music.wav" if_changed
        scene medbaydoor
        with Dissolve (0.5)
        C "Doctor! It's me, let me in!"
        D "Hold on Connie, while I'd love to, I need you to wait here for just a minute"
        D "I need to test you to make sure your not too far gone"
        C "WHAT! A test, I don't have time for that!?"
        D "I’m sorry, I deeply am. But I can’t afford to make the same mistake I did an hour ago that nearly cost us our lives…"
        D "now please settle down. This will only take a minute."

    label finalquestions:
        D "What is today's current date"

    menu:
        "Sept 26th....uhhh...1917?":
            jump wrong1
        "4280 C.E.":
            jump correctanswer
        "October 13th 201036":
            jump wrong2

    label wrong1:
        D "Connie, your great great great grandmother was not even alive back then"
        D "I'm sorry I..."
        C "Wait! Give me one more shot, PLEASE!"
        D "Alright"

        jump finalquestions

    label wrong2:
        D "That's...in the future"
        D "I'm sorry I..."
        C "Wait! Give me one more shot, PLEASE!"
        D "Alright"

        jump finalquestions

    label correctanswer:
        C "It’s 4280…"
        C "I don’t remember the exact date though…is that fine?"
        D "I suppose..."
        D "But just in case I will ask you one more question."

    label finalquestion:
        D "What solar system are we in?"

    menu:
        "Andromeda":
            jump correctfinal
        "Michael":
            jump wrongfinal

    label correctfinal:
        C "ANDROMEDA! We're in Andromeda!"
        D "Phew! Welcome in captain..."

        jump finale

    label wrongfinal:
        C "Michael! We're in Michael!"
        D "Im sorry captain but we never were in the Michael system"

        jump infected

    label finale:
        scene medbay
        with Dissolve (1.0)
        D "I hope you can forgive me for delaying you...?"
        C "It's fine, just give me the cure..."

        jump success

    label death:
        scene bg black
        with Dissolve (1.0)
        C "Gah! Not like this!"

        jump end

    label infected:
        scene bg black

        "Connie feels the infected run through here body"
        C "I’m almo…I’m atmost…. I’m compo…No…no pleas…tim….tim…I knee…..AHHH!"

        jump end

    label success:
        scene bg black
        with Dissolve (1.0)
        "With the cure in her system, Connie and Doctor Morgana start working on plans to get back control of the Astromorbus"

        jump end



    label end:
    # This ends the game.
    return
