###################################################################################################################################################################3Hunger

label hunger_none:
    d "Hungry?"
    p "Fuck off!"
    $fuckoff +=1
    if fuckoff >=3:
        if firsttime:
            p "I said FUCK OFF."
            scene pull_day with vpunch
            d "Forgotten your place so soon, dog?"
            p "F-Fuck!"
            $fuckoff -=3
            jump sim
        else:
            jump group1
    else:
        jump sim

label hunger_1:
    "[d] throws a fruit near [p]"
    show m at s
    show m_m at s
    p "..."
    hide m
    hide m_m
    show m_tired at s
    show m_m_clench at s
    "The fruit looks dirty. It is covered in dirt from the ground."
    hide m_tired
    hide m_m_clench
    show m_surprise at s
    show m_m_sexclench2 at s
    "[p] glances at [d]"
    p "Fu-.."
    hide m_surprise
    hide m_m_clench
    show m_tired at s
    show m_m_sexclench1 at s
    show m_beaten2 at s
    "[d] slams [p]'s head against the tree." with vpunch
    d "You should stop your swearing habit, naughty child!"

    show m_hurt at s
    show m_m_scream at s
    show m_beaten3 at s
    show m_shame at s
    p "....m....a" with hpunch
    "[d] steps on him harder."

    hide m_m_scream
    hide m_m_sexclench2
    hide m_m_sexclench3
    show m_foodsmall at s
    show m_m_sexclench3 at s
    "[d] picks the fruit up and shoves it into [p]'s mouth." with vpunch
    d "Eat it!"
    hide m_m_sexclench3
    hide m_m_sexclench1
    show m_m_sexclench1 at s
    "[p] purses his lips and clenches his teeth."
    "[d] laughs."
    hide m_m_sexclench1
    hide m_foodsmall
    hide m_spermface at s
    show m_beaten3 at s
    show m_foodsmall at s
    show m_m_scream at s
    show m_blush at s

    p "AArgh!" with vpunch
    "He kicks [p] in the stomach."
    hide m_m_scream
    show m_m_sexclench3 at s
    d "If you don't know how to please others, you're going to have a reeeaaally hard life ahead of you."
    hide m_m_scream
    hide m_beaten3
    hide m_foodsmall
    hide m_blush
    hide m_shame
    show m_close at s
    show m_beaten3 at s
    show m_foodsmall at s
    show m_shame at s
    show m_blush at s
    show m_m_sexopen at s
    p "Fuck!"
    "[p] is exhausted physically. His hunger, thirst and dirtiness increase. His psyche decreases."
    hide screen day
    hide screen stat
    scene black with fade
    pause .5
    $food -=5
    $water -=10
    $ene -=40
    $clean-=2
    jump sim

label hunger_2:
    "[d] throws dozens of fruits in front of [p] as the vines retreat from his body."
    show m_tired at s
    show m_m at s
    p "..."
    "[p] looks at [d]. [d] smirks."
    d "If you are hungry, then eat. There's no one here for you to show off your stubbornness. Hunger will just starve your brain into submission faster."
    hide m_m
    show m_m_sexclench2 at s
    p "(Fuck!)"
    "[p] tries to move his hand."
    hide m_m_sexclench2
    show m_m_clench at s
    p "..."
    p "I can't eat with my hands tied."
    d "You can."
    hide m_m_clench
    show m_m at s
    p "..."
    hide m_m
    hide m_tired
    show m_close at s
    show m_m at s
    show m_shame at s
    p "(..Fuck!)"
    scene food
    "[p] bends down and eats."
    p "(It stinks!)"
    p "...*chomp*.. *chomp*.."

    show m_tired at s
    show m_m_sexclench2 at s
    show m_food1 at s
    show m_shame at s
    p "(Bastard, it's full of dirt!)"
    scene food_tram with vpunch
    "[d] steps on [p]'s head."
    scene food_trama
    p "Urg...mmm..."
    scene food_tram
    d "Hurry up prince. Don't be so picky. Do understand that this isn't your palace."
    scene fooda
    show m_close at s
    show m_food1 at s
    show m_shame at s
    show m_m_clench2 at s
    p "(Fuck! I'll definitely kill you!)"
    "[p] feels ashamed of himself. His pride and psyche decrease. His hunger decreases."
    "[p]'s thirst and dirtiness increase."
    hide screen day
    hide screen stat
    scene black with fade
    pause .5
    $food +=50
    $mental -= 2
    $water -=5
    $pride -=1
    $ene -=40
    $clean-=3
    scene black with dissolve
    jump sim

label hunger_obe:
    "[d] throws dozens of fruit in front of [p]. The fruits are covered in a sticky white liquid."
    show m_tired at s
    show m_m1 at s
    d "A special treat, just for you."
    show m_close at s
    show m_m_open2 at s
    show m_shame at s
    p "..."
    "[p] bends down and eats."
    scene food_sperm
    hide tie_looka
    d "Won't ask what it is?"
    d "Well, I guess you already know."
    p "...."
    d "Before you have your meal, clean up the sticky mess on the ground first."
    p "..."
    show food_tram_sperm with hpunch
    d "You're taking too long. I heard that the prince never hesitated in anything, but I guess the rumors were wrong. Why don't I assist you, [p]?"
    p "...m..."
    "[p] chews up the smashed fruit, dirt and cum."
    p "..."
    d "Shouldn't you be thanking me for the help? Or do you intend on eating dirt and semen forever?"
    p "...h..."
    show m_hurt at s
    show m_m_sexclench1 at s
    show m_shame at s
    show m_blush at s
    show m_beaten1 at s
    show m_food at s
    p "...T-thank you for your help..."
    d "Good job! Now you can enjoy your meal."
    hide food_tram_sperm
    p "..."

    "[p] is exhausted physically and mentally. His pride and psyche decrease. His hunger decreases."
    "[p]'s thirst and dirtiness increases."
    hide screen day
    hide screen stat
    scene black with fade
    pause .5
    $food +=70
    $water -=0
    $mental -=2
    $pride -=3
    $ene -=20
    $clean -=3
    jump sim
