#####################################################################################################################################################################################333Thirst
label water_20:
    show m at s
    show m_m at s
    d "Want to drink something?"
    hide m_m
    show m_m_sexclench1 at s
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


label water_50:
    d "You must be thirsty."
    show m_tired at s
    show m_m_clench at s
    p "..."
    "[d] pulls out a waterskin and drinks from it. He intentionally gulps the water down loudly."
    hide m_m_clench
    show m_m_sexclench2 at s
    d "*gulp* *gulp*"
    d "You sure you don't want it?"
    show m_close at s
    show m_m_sexclench1 at s
    p "..."
    d "Alright, I get your message."
    "[d] pours the water onto the ground"
    hide m_close
    hide m_m_sexclench1
    hide m_m_sexclench2
    hide m_m_clench
    show m_m_clench2 at s
    p "..."
    $water -=5
    $ene -=20
    $pride -=1
    $mental -=1
    "[p]'s thirst increases. His pride and mental decreases."
    hide screen day
    hide screen stat
    scene black with fade
    pause .5
    jump sim

label water_80_first:  ##only for the first time
    show m at s
    show m_m at s
    d "You look dehydrated. Are you sure you don't want this?"
    "The vines loosen as [d] hands the waterskin to [p]."
    scene darkforest
    hide m_m
    show m at left
    show m_cockdown at left
    show m_m_sexclench2 at left
    p "..."
    hide m_m_sexclench2
    hide m_cockdown
    show m_close at left
    show m_cockdown at left
    show m_shame at left
    show m_m_sexclench2 at left
    "[p] reaches towards it. \n[d] pulls back at the last moment."
    hide m_cockdown
    show m_surprise at left
    show m_cockdown at left
    show m_m_open1 at left
    p "..."
    d "You can drink, but not that way."
    show m at left
    hide m_m_open1
    show m_m_clench at left
    "[d] pours water onto the ground."
    d "You either drink this way, or you're not getting any."
    hide m_surprise
    hide m_cockdown
    show m_surprise at left
    show m_cockdown at left
    show m_shame at left
    show m_blush at left
    show m_m_sexclench1 at left
    p "Fuck you! I don't need it!"
    "[p]'s thirst increases. His pride and mental decrease."
    $water -=5
    $ene -=20
    $pride -=1
    $mental -=1
    $firstwater = False
    jump sim

label water_80:
    show m at s
    show m_m at s
    d "You look dehydrated. Are you sure you don't want this?"
    "[d] hangs the water above [p]. [p] remains motionless."
    scene darkforest
    show m at left
    show m_cockdown at left
    show m_m at left
    p "..."
    d "Okay."
    hide m_cockdown
    show m_surprise at left
    show m_cockdown at left
    show m_sperm at left
    show m_m_open2 at left
    "[d] pours the water over [p]'s head" with hpunch
    hide m_m_open2
    hide m_cockdown
    hide m_sperm
    show m_tired at left
    show m_cockdown at left
    show m_shame at left
    show m_sperm at left
    show m_blush at left
    show m_m_sexopen at left
    "[p] licks the water droplets falling onto his lips."
    d "Interesting."
    "[p]'s thirst decreases. His pride and psyche decreases"
    $water +=25
    $mental -=2
    $pride -=2
    $ene -=20
    jump sim


label water_90:
    show m_tired at s
    show m_m at s
    "The vines loosen as [d] put the waterskin on [p]'s chest"
    scene darkforest
    show m_tired at left
    show m_cockdown at left
    show m_m1 at left
    p "..."
    d "You're not gonna take it?"
    hide m_m1
    show m_m_open1 at left
    p "Like you would let me."
    d "What a surprise. You aren't as dumb as I thought."
    hide m_cockdown
    show m_close at left
    show m_cockdown at left
    show m_blush at left
    show m_m_1 at left
    p "(That bastard!)"
    "[d] starts pouring out the water in front of [p]."
    hide m_m_1
    hide m_blush
    hide m_m1
    hide m_tired
    hide m_cockdown
    show m_tired at left
    show m_blush at left
    show m_cockdown at left
    show m_m1 at left
    d "So, are you going to drink it or not?"
    hide m_m1
    show m_shame at left
    show m_m_sexclench2 at left
    p "(Fuck!)"
    "[p] kneels down and drinks it"
    scene water
    show m_tired at s
    show m_blush at s
    show m_m1 at s
    show m_shame at s
    p "..."
    $water +=50
    $pride -=2
    $ mental -=2
    $ene -=20
    "[p]'s thrist increases. His pride and psyche decrease."
    scene black with dissolve
    pause .5
    jump sim

label water_obe:
    "The vine loosens."
    scene darkforest
    show m_close at left
    show m_cockup at left
    show m_m at left
    p "...Mnh..."
    d "Time for a drink, [p]!"
    hide m_close
    hide m_cockup
    hide m_m_open2
    show m_tired at left
    show m_cockup at left
    show m_shame at left
    show m_m_open2 at left
    p "..."
    hide m_close
    hide m_cockup
    hide m_m
    hide m_shame
    show m_close at left
    show m_cockup at left
    show m_m at left
    show m_shame at left
    "[p] kneels down and waits for [d] to pour water."
    hide m_m
    hide m_close
    hide m_cockup
    hide m_m_open2
    show m_tired at left
    show m_cockup at left
    show m_shame at left
    show m_m_clench at left
    show m_blush at left
    "[d] looks at [p] and smirks."
    scene water_wait
    d "You've become so submissive."
    show m_close at s
    show m_m_clench at s
    show m_shame at s
    show m_blush at s
    p "..m...h..."
    d "If you were as cute as this from the beginning, I would have gone easier on you."
    hide m_m_clench
    show m_m_sexopen at s
    p "...nh..."
    "[d] pours water onto the ground"
    scene water
    show m_tired at s
    show m_cockup at s
    show m_shame at s
    show m_m_open2 at s
    show m_sperm at s
    show m_blush at s
    p "*gulp* *gulp*"
    d "There is still some drops of water on my foot. You wouldn't want to waste it."
    "[d] points to his foot."
    hide m_shame
    hide m_m_open2
    hide m_blush
    hide m_tired
    hide m_sperm
    show m_close at s
    show m_m_open2 at s
    show m_shame at s
    show m_blush at s
    show m_sperm at s
    p "..*gulp*. That-..."
    d "Hurry up, dog!"
    p "...n..."
    hide m_shame
    hide m_m_open2
    hide m_blush
    hide m_sperm
    hide m_close
    show m_tired at s
    show m_shame at s
    show m_m_open2 at s
    show m_sperm at s
    show m_blush at s
    "[p] laps up the water droplets on [d]'s feet"
    scene water_licka
    p "...mn..."
    show m_tired at s
    show m_shame at s
    show m_sperm at s
    show m_m_sexopen at s
    show m_blush at s
    d "Are you blind? There's some on my legs too!"
    hide m_shame
    hide m_blush
    hide m_sperm
    show m_close at s
    show m_sperm at s
    show m_m_open2 at s
    show m_shame at s
    show m_blush at s
    p "..."
    scene water_lickb
    show m_close at s
    show m_sperm at s
    show m_m_1 at s
    show m_shame at s
    show m_blush at s
    d "I want to see you lick it all up passionately."
    hide m_m_1
    show m_m_sexopen at s
    p "...n..."
    d "Good boy! Very good!"
    hide m_m_sexopen
    show m_m1 at s
    p "...m..."
    scene darkforest with dissolve
    show m_close at left
    show m_sperm at left
    show m_m_sexclench3 at left
    show m_blush at left
    show m_shame at left
    show m_beaten1 at left
    show m_cockup at left
    d "Once you return to the palace, you should serve your people this way. They will adore you deeply."
    hide m_m_sexclench3
    show m_m_sexclench1 at left
    p "..."
    $water +=80
    $mental -=1
    $pride -=1
    $ene -=20
    "[p]'s thirst decreases. His pride and psyche decrease."
    jump sim
