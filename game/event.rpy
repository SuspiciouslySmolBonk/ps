



##########################################################################################Fanit

label faint:
    scene darkforest with flash
    p "...haaa...haaa..."
    d "You alright?"
    p "...m..."
    scene black
    "[p] fainted from poor care."
    "[d] gives him food, water and lets him rest for a day."
    "His thirst and hunger decrease. His psyche increases."
    $water =20
    $food =20
    $mental +=3
    $day +=1
    jump sim




################################################################################################################################################################################################ End day
label justendday:
    $firstMos =1
    hide screen day
    hide screen stat
    scene black with dissolve
    pause .5
    "[p] still hasn't recovered from yesterday. [d] lets him rest for a day."
    $day +=1
    $clean = 100
    jump newday

label endday:
    if firstMos == 1 and clean<=30 and clean>0:
        jump bath30
    elif clean <=0:
        jump bath
    elif water >=100:
        show m_tired at s
        show m_shame at s
        show m_m_open2 at s
        p "[d]"
        d "How rare! The prince is calling me."
        hide m_tired at s
        hide m_shame at s
        hide m_m_open2 at s
        show m_close at s
        show m_m1 at s
        show m_shame at s
        show m_blush at s
        p "..."
        hide m_close
        hide m_m1
        hide m_shame
        hide m_blush
        show m_tired at s
        show m_shame at s
        show m_m_open2 at s
        show m_blush at s
        p "Please untie me. I need to pee."
        d "You can pee right there."
        hide m_tired
        hide m_shame
        hide m_m_open2
        hide m_blush
        show m_surprise at s
        show m_shame at s
        show m_m_clench at s
        show m_blush at s
        p "..."
        hide m_surprise
        hide m_shame
        hide m_m_clench
        hide m_blush
        show m_close at s
        show m_shame at s
        show m_m_clench at s
        show m_blush at s
        menu:
            "Untie him":
                "[d] lets Pitchy untie [p]"
                scene darkforest with dissolve
                hide m_close
                hide m_shame
                hide m_m_clench
                hide m_blush
                show m_surprise at left
                show m_shame at left
                show m_m at left
                show m_blush at left
                show m_cockup at left
                d "Go!"
                scene darkforest with dissolve
                pause 1.0
                hide m_surprise
                hide m_shame
                hide m_m
                hide m_blush
                hide m_cockup
                "[p] goes away for a while, then comes back."
                show m_tired at left
                show m_shame at left
                show m_m at left
                show m_blush at left
                show m_cockup at left
                d "Not trying to escape?"
                hide m_m
                show m_m1 at left
                p "..."
                d "Smart choice. I'll let you rest for now."
                p "..."
                jump controlnote
                jump newday




            "Make him pee":
                if mental >=35 and pride >=35:

                    d "Let see how long the prince can hold back."
                    p "Fuck you!"
                    "[d] steps closer as [p] tries to moves backwards."
                    d "Don't be scared, I'll make you feel better."
                    p "No! Stop!"
                    "[d] stomps hard on [d]'s stomach repeatedly."
                    p "Arghhh!..Argh!!"
                    "[p] spilled his piss onto the ground."
                    p "..."
                    "[d] laughs"
                    $mental -=10
                    $pride -=10
                    d "Dogs mark with their urine either when they're highly aroused, overstimulated or anxious. I wonder which one it is in your case."
                    p "...F-fuck.."
                    $water =70
                    $clean -=5
                    jump controlnote
                    "[p]'s psyche and pride decrease. He becomes dirtier."
                    jump newday
                else:
                    d "Hurry dog. You know what happens if I wait too long."
                    p "..."
                    "[p] pees on the ground"
                    p "...m..."
                    d "Hmph, it stinks! You've just dirtied the ground. Clean it up with your mouth."
                    "The vines release [p]"
                    d "Chop chop."
                    p "...no..."
                    d "Don't make me repeat myself twice!"
                    p "...No [d]...please have mercy."
                    d "Huh?"
                    p "...Th-that's enough. I can't take it anymore. Please...don't make me look more despicable more than you already have..."
                    d "...Hmph..."
                    p "...Please spare me... I'm begging you.."
                    menu:
                        "Force him":
                            d "Still able to talk back, huh?"
                            "[d] grabs a fistful of the mixture of dirt and piss, violently ramming it into [p]'s mouth."
                            p "...m..."
                            d "Open your mouth and eat it before I make you clean all of your mess."
                            p "..."
                            "[p] chews some of the dirt in [d]'s hand."
                            p "*gulp*"
                            "[p] chokes."
                            p "*cough* *cough*"
                            d "How does it taste, prince?"
                            p "*Gulp*"
                            p "..."
                            d "Huh?"
                            p "..."
                            p "...It's...horrible..."
                            d "Hmm? What's that? I don't think I've heard you correctly."
                            p "..."
                            p "...It-..."
                            d "The mixture of my piss and the dirt..."
                            p "..."
                            p "..The mixture of my piss and the dirt...t-tastes...delicious..."
                            "[d] laughs."
                            d "Your taste is weird, even worse than that of a pig."
                            p "...m.."
                            "[d] touches [p]'s face."
                            d "If you like it that much, finish up the rest!"
                            p "..."
                            "[p] eats up the remaining mixture both on his face and from [d]'s hand."
                            p "...n..."
                            "[d] pulls [p]'s hair back."
                            p "...argh..."
                            d "Seems like you understand your place now."
                            d "Remember this well. Now you've stooped even lower than a dog."
                            "[p] is exhausted physically. His pride and psyche decreases dramatically."
                            "His thirst increases from eating dirt and piss. He becomes dirtier."
                            p "..."
                            $water =70
                            $pride -=15
                            $mental -=15
                            $clean -=7
                            jump controlnote

                        "Spare him":
                            "[d] laughs"
                            d "You understand how to beg now."
                            "The vines release [p]"
                            p "?"
                            d "Show me your appreciation!"
                            p "..."
                            p "T-thank yo..."
                            d "Do you even have a brain? I didn't untie you for that."
                            p "..."
                            d "How does a dog show appreciation to its owner?"
                            p "..."
                            "[p] crawls to [d]"
                            d "Clean your face first! Don't dirty my feet!"
                            "[p] cleans his face."
                            p "..."
                            d "Chop chop!!"
                            "[p] licks [d]'s foot."
                            show water_lickb
                            p "...n..."
                            d "You don't resist this much these days."
                            show water_licka
                            p "..."
                            p "...You win..."
                            d "Huh?"
                            p "..."
                            d "Hah. Seems like your master has trained you well."
                            "[p] is exhausted physically. His pride and psyche decrease. He becomes dirtier"
                            p "..."
                            $water =70
                            $pride -=10
                            $mental -=10
                            $clean -=5
                            jump controlnote
    elif nothing >= 4:
        show m at s
        show m_m_open1 at s
        p "..!.."
        d "What's with that look? Are you feeling lonely?"
        hide m_m_open1
        show m_m_sexclench2 at s
        show m_shame at s
        p "..."
        d "Rest well!"
        hide m_shame
        show m_surprise at s
        show m_m_clench at s
        show m_shame at s
        show m_blush at s
        p "!"
        hide m_blush
        hide m_shame
        show m_tired at s
        show m_m_1 at s
        show m_shame at s
        show m_blush at s
        p"..."
        "[p] feels ashamed of himself. His pride decreases."
        $ nothing = 1
        jump controlnote
    else:
        d "Let's let him rest."
        jump controlnote
        jump newday


label controlnote:
    p "Ngh..."
    if 60>mental>30 and 60>pride>30:
        if control3first:
            d "Time to test!"
            jump control3
        else:
            jump newday
    else:
        jump newday


label newday:
    "[p]'s thirst and hunger increased as the day went by."
    hide screen day
    hide screen stat
    $day +=1
    $water -=7
    $food -=5
    $clean -=7
    scene black with dissolve
    pause .5
    if ene>=100:
        $nothing +=1
        jump sim
    else:
        jump jumpsim

label jumpsim:
    $ene =100
    hide screen day
    hide screen stat
    scene black with dissolve
    pause .5
    jump sim

label endday2:
    hide screen day
    hide screen stat
    hide screen sit_up_screen
    scene darkforest2
    $day +=1
    $water -=7
    $food -=5
    $clean -=2
    if water >=100 or food >=100:
        scene darkforest2
        show m_tired
        show m_cockdown
        show m_m2
        "[p] goes behind the tree."
        scene darkforest2
        show m_surprise
        show m_cockdown
        show m_blush
        show m_m_open_speak
        d "What are you doing?"
        scene darkforest2
        show m_tired
        show m_cockdown
        show m_blush
        show m_shame
        show m_m_open2
        p "I-I need to...have some privacy. Please don't follow me."
        scene darkforest2
        show m_close
        show m_cockdown
        show m_blush
        show m_shame
        show m_m_open2
        "[d] laughs."
        hide m_m_open2
        show m_m2
        p "..."
        "A few minutes later, [p] returns to his place."
        scene darkforest2
        show m
        show m_cockdown
        show m_blush
        show m_shame
        show m_m2
        d "Relief?"
        scene darkforest2
        show m_tired
        show m_cockdown
        show m_blush
        show m_shame
        show m_m_open2
        p "Y-yeah."
        scene darkforest2
        show m_close
        show m_cockdown
        show m_blush
        show m_shame
        show m_m_normal
        p "..."
        $water = 70
    if talk >= 18:
        hide screen sit_up_screen
        scene black with dissolve
        pause .5
        $ roll = 0
        $ roll = renpy.random.randint(1, 3)
        if roll == 1:
            jump morning_greet1
        elif roll == 2:
            jump morning_greet2
        elif roll == 3:
            jump morning_greet3
    else:
        hide screen sit_up_screen
        scene black with dissolve
        pause .5
        "A new day has come."
    $ene = 100
    jump simbutton2
