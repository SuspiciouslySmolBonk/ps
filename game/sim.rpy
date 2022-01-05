

screen tie:
    imagemap:
        ground Animation("tie0001.jpg",.2,"tie0002.jpg",.2,"tie0003.jpg",.2,"tie0004.jpg",.2,"tie0005.jpg",.2,"tie0006.jpg",.2,"tie0007.jpg",.2,"tie0008.jpg",.2,"tie0009.jpg",.2,"tie0010.jpg",.2)
        hover Animation("tie_look0001.jpg",.1,"tie_look0002.jpg",.1,"tie_look0003.jpg",.1,"tie_look0004.jpg",.1,"tie_look0005.jpg",.1,"tie_look0006.jpg",.1,"tie_look0007.jpg",.1,"tie_look0008.jpg",.1,"tie_look0009.jpg",.1,"tie_look0010.jpg",.1,"tie_looka0001.jpg",.1,"tie_looka0002.jpg",.1,"tie_looka0003.jpg",.1,"tie_looka0004.jpg",.1,"tie_looka0005.jpg",.1,"tie_looka0006.jpg",.1,"tie_look0007.jpg",.1,"tie_look0008.jpg",.1,"tie_look0009.jpg",.1,"tie_look0010.jpg",.1)
        hotspot (243, 365, 600, 1000) action Function(renpy.transition, dissolve), Call ("simbutton")

label sim:
    $ showday = True
    show tie with fade
    call screen tie

label simbutton:
    scene tie_looka
    show screen day
    show screen stat
    if ene <=0:
        jump endday
    elif water<=0 or food <=0:
        jump faint
    elif clean<=0:
        jump bath
    else:
        if controlStage==2 and dogtraining==False:
            "A new event had been unlocked. Please check out Humiliation option."
            $dogtraining = True
        menu:
            "Water and Feed":
                menu:
                    "Water":
                        if ene <= 0:
                            jump endday
                        else:
                            if firstwater:
                                jump water_80_first
                            else:
                                if mental<=50 and pride<=50 and water>0:
                                    jump water_obe
                                elif water >=50:
                                    jump water_20
                                elif 50>water>=40:
                                    jump water_50
                                elif 40>water>=30:
                                        jump water_80
                                else:
                                    jump water_90
                    "Feed":
                        if ene <= 0:
                            jump endday
                        else:
                            $clean -=5
                            if mental<=50 and pride<=50 and food>=50:
                                jump hunger_obe
                            elif mental<=30:
                                menu:
                                    "How do you like to feed him?"
                                    "Like a dog":
                                        jump hunger_obe
                                    "Like a human":
                                        "The vine releases [p]."
                                        p "?"
                                        "[d] throws [p] some fruits."
                                        p "..."
                                        p "What do you want?"
                                        d "So you'd prefer to eat them on the ground then?"
                                        p "..."
                                        "[p] eats the fruits."

                            elif food >=40:
                                jump hunger_none
                            elif 40>food>=30:
                                jump hunger_1
                            else:
                                jump hunger_2
                    "Return":
                        jump simbutton
            "Humiliation":
                menu:
                    "Tease":
                        if ene <=0:
                            jump endday
                        else:
                            if pride >=90:
                                jump touch_first

                            elif 90>pride>=50:
                                if touchfirstnone:
                                    jump touch_first
                                else:
                                    jump touch
                            else:
                                if touchfirstnone:
                                    jump touch_first
                                elif touchnone:
                                    jump touch
                                else:
                                    jump touch_obe

                    "Toy":
                        if ene <=0:
                            jump endday
                        else:
                            $clean -=2
                            if pride <40:
                                if toyfirst:
                                    jump toy_thrust_first
                                else:
                                    jump toy_obe
                            elif pride >=90:
                                jump toy_no

                            elif 90>pride>=50:
                                if toyfirst:
                                    jump toy_thrust_first
                                else:
                                    jump toy_hook

                            else:
                                if toyfirst:
                                    jump toy_thrust_first
                                else:
                                    jump toy_thurst
                    "Dog Sex" if dogtraining:
                        jump dogtraining
                        jump simbutton
                    "Return":
                        jump simbutton
            "Sex":
                menu:
                    "Oral":
                        if ene <=0:
                            jump endday
                        else:
                            $clean -=1
                            if mental>=95:
                                jump cock_none
                            elif 95>mental>=75:
                                jump cock_1
                            elif 75>mental>=50:
                                jump cock_2
                            else:
                                if controlStage >=3:
                                    jump cock_end
                                else:
                                    jump cock_obe
                    "Anal":
                        if ene <=0:
                            jump endday
                        else:
                            $clean -=2
                            if mental>=90:
                                jump ass_none
                            elif 90>mental>=80:
                                jump ass
                            elif 80>mental>=50:
                                if firsttime:
                                    jump ass_nine
                                else:
                                    jump ass_nine2
                            else:
                                jump ass_obe
                    "Group Sex" if group_baby ==True:
                        jump group2

                    "Group Sex" if group_nobaby ==True:
                        jump group2_nobaby

                    "Return":
                        jump simbutton

            "Test mind control":
                if mental <=0 and pride <=0 and controlStage == 3:
                    jump alteration
                else:
                    if mental >=70:
                        jump control1
                    elif 70>mental>=30 and 70>pride>=30:
                        jump control2
                    else:
                        jump control3
            "Let [p] rest":
                jump endday
