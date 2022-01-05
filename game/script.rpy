# The script of the game goes in this file. /D/PROGRAM/RENPY/renpy-6.99.14-sdk/PriceAndSub

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define p = Character("Prince")
define n = Character("Nine")
define m = Character("Monster")
define k = Character("King Raphael")
define h = Character("A Random Human")
define ri = Character("Rivakh")
define ren = Character("Ren")
default showday = False
default show = False
default firstwater = True # if this is the first time water                  country name:   Rivakh
default firsttime = True # if this is the first time Anal
default firstMos = 0 # BATH Mosquito monsters meeting, =0 at first
default bath_just_enough = False # BATH wrech him enough
default toyfirst = True # if this is the first time with Sword
default group_baby = False
default group_nobaby = False
default touchfirstnone = True # if this is the first time Tease him
default touchnone = True
default controlState = 0
default dogtraining = False
default goodend = 0
default talk = 0
define config.window_show_transition = { "screens" : Dissolve(0) }

init python:
    showday= False
    day = 1
    def display_day():
        if showday:
            ui.frame(background= "frame.png",xpos= 500, ypos= 50, xsize= 579, ysize= 130, left_padding= 20)
            ui.text("$ %d" %day, xalign= 0.5, yalign= 0.5, xoffset= 2, yoffset= 8)
            config.overlay_functions.append(display_day)

transform s:
    zoom 0.8
    ypos 600
    xpos -180
label start:
    scene black
    "Are you a new or old player?"
    $d = "Dietrich"
    $p = "Ray"
    #jump alteration
    #jump goodend
    menu:
        "New":
            "Welcome and enjoy the game!"
        "Old":
            "Where do you want to skip to?"
            menu:
                "The sim":
                    $p = renpy.input("Your name is...(press enter to use the default name)", "Ray", length=20)
                    $d = renpy.input("The monster's name is...(press enter to use the default name)", "Dietrick", length=20)
                    $water =30
                    $food =40
                    $ene =100
                    $nothing =1
                    $mental = 90
                    $pride = 90
                    $day = 4
                    $fuckoff =0
                    $clean = 90
                    $controlStage = 0
                    play music "Angevin.mp3"
                    jump sim
                "End of the sim":
                    $p = renpy.input("Your name is...(press enter to use the default name)", "Ray", length=20)
                    $d = renpy.input("The monster's name is...(press enter to use the default name)", "Dietrick", length=20)
                    $water =90
                    $firstwater = False
                    $food =90
                    $ene =100
                    $nothing =1
                    $mental = 0
                    $pride = 0
                    $day = 50
                    $clean = 40
                    $group_baby = True
                    $controlStage = 2
                    play music "Angevin.mp3"
                    jump sim
                "Ending choices":
                    $p = renpy.input("Your name is...(press enter to use the default name)", "Ray", length=20)
                    $d = renpy.input("The monster's name is...(press enter to use the default name)", "Dietrick", length=20)
                    $water =90
                    $firstwater = False
                    $food =90
                    $ene =100
                    $nothing =1
                    $mental = 0
                    $pride = 0
                    $day = 50
                    $clean = 40
                    $group_baby = True
                    $controlStage = 3
                    play music "Angevin.mp3"
                    jump sim2
                "No skipping":
                    "Please continue the game."

    play music "Thaxted.mp3" fadeout 3.0
    scene cg1
    "Once upon a time, there was a young boy. This youth was far more determined than all others of his age."
    scene cg3
    "Whatever he did, he always succeeded in. Whatever he wanted, he always got."
    scene cg4
    show cg_ray
    "When he first chose to enroll in the army, everyone opposed his decision due to his age, but he was having none of that—he does as he pleases."
    "After demonstrating his skills, he immediately silenced his opposition."
    "Years later, at the tender age of twenty-two, he became a general and was known as one of the strongest men alive in the country."
    scene cg4
    show cg_fight
    "He and the king rarely talked to each other. And if they did, it usually became a big fight, resulting in him being thrown out."
    "The fights were shocking to see, yet equally unsurprising. He was the king’s son, the first heir."
    "Unlike his younger half-brother, who was loved by everyone, this prince was either feared or hated."
    "{i}Arrogant. Stubborn. Unpleasant. Barbaric. Ruthless. Repulsive. Quick-tempered.{/i} \nThat was how everyone described him."
    "No wonder then, despite his capability, that the king chose Ren, the younger brother, to become the crown prince."
    scene cg4
    show cg_fight
    "\"You want this dumbass to be your successor because all you want is a puppet!” The uninvited prince shouts angrily, his voice echoing through the throne room."
    "“Don’t you dare speak like that to your future king! Ren can have you executed should he choose to!” The king retorts."
    scene cg4 with vpunch
    show cg_ren
    show cg_fight
    "\"Dad, brother, please stop it you two!\" Ren jumps in between them." with hpunch
    "The room grows noisy. Some begin to laugh.\n\"SILENCE!\" the prince shouts." with vpunch
    "The king slaps his face. \"Who gave you such authority? Disrespectful brat!\"" with hpunch
    "The prince glances at the king, and returning the gesture, forcefully slapping the king back in retaliation. \nThe king falls to the floor. Soldiers surround the prince." with vpunch
    "\"How dare you! From now on, you are no longer my son. Don’t ever come back to this palace!\" The king pointed at him angrily."
    scene cg2
    "The prince turns to leave. \"Getting rid of me now? One day you will regret this.\"\n He takes one last look at the throne room, and all he sees are happy smiles. The prince clenches his fist."
    scene black with dissolve
    pause .5
    "He slams the door as hard as when he first came in." with hpunch
    stop music
    play music "Angevin.mp3" fadeout 3.0
    scene darkforest_night with dissolve
    "A few days later, he arrived at the entrance of the Dark Forest, the most fearsome place known to man."
    "Legend says that this was the place where God hid the First Stone, inscribed with the following quote: \n{i}\"This stone bestows upon its owner the power to bend The Flow and destroy all laws of the current Universe.\"{/i}"
    "To put it another way: {i}The stone could grant wishes.{/i}"
    show m_armor at left
    p "It is not merely a legend. Many rulers from all over the world have sent troops here in search of it. Even now, there are many who lose their lives here."
    "The prince laughs."
    p "Those useless fools don't even know the proper methods in navigating these deep woods. They lack the experience in battling monsters."
    "Immediately after entering the forest, he encountered many groups of monsters, but he slayed them with little difficulty."
    "A young monster trips and falls on its own. It tries to stand up."
    p "Running away?"
    m "P-please spare m-..."
    "He cuts off the monster's head without an inch of hesitation, pressing forward."
    "Suddenly, a small demon appears in front of him."
    show n at right with dissolve
    p "A demon? In the far depths of the Dark Forest? How could a demon as weak as you survive in such a place? Are you here by yourself?"
    $n ="Demon"
    hide n
    show n_smile at right
    n "Are you a human knight?"
    p "..."
    n "Sir Knight, if you go further, there will be no return. The monsters there are extremely strong."
    "The prince grips his sword hard, before eventually relaxing his muscles."
    p "..."
    hide n_smile
    show n at right
    n "?"
    menu:
        "Ask him about the stone":
            p "Demon."
            hide n
            show n_smile at right
            n "What is it, sir Knight?"
            p "Do you know anything about the First Stone?"
            hide n_smile
            show n_smile2 at right
            n "Yes. I have been asked this very question many times before."
            hide n_smile2
            show n_sad at right
            "The demon shook his head."
            hide n_sad
            show n_angry at right
            n "Most who seek it are now dead..."
            p "Cut to the chase and tell me!"
            hide n_angry
            show n_sad2 with dissolve
            n "..."
            "The demon whispers to the prince."
            hide n_sad2
            show n_surprise
            n"In the middle of a giant river lies the Water Temple, which holds the first stone..."
            p"I know that."
            hide n_surprise
            show n_surprise2
            n"..."
            hide n_surprise2
            show n_smile
            n "You know a lot. None of the knights who came before you knew that."
            p "..."
            hide n_surprise2
            show n_smile2
            n "There is but a single large river in this forest. Is that new information to you?"
            p "..."
            "The prince moved past the demon."
            scene darkforest_night
            show m_armor at left
            p "(That's good, I'll just need to look for one river.)"
            "Two hours later, the prince was still nowhere near finding the First Stone. All he could see were trees and more trees."
            p "I should be getting close to the river."
        "Ignore him":
            p "(I doubt such a weak demon will know anything.)"
            "The prince walks forward."
            p "..."
            menu:
                "Show him the way out":
                    $ show = True
                    "The prince turns around and points towards where he came from."
                    hide n
                    show n2 at right
                    n "What is it?"
                    p "That’s the way out."
                    hide n2 with dissolve
                    n "{i}Look for the only river in this forest.{/i}"
                    p "!"
                    scene darkforest_night
                    show m_armor at left
                    "The demon goes away."

                "Nevermind":
                    "The prince walks past the demon."
                    n "{i}Look for the only river in this forest.{/i}"
                    p "!"
                    scene darkforest_night
                    show m_armor at left
                    "The demon goes away."

            "He made his way further into the forest."
            "Two hours later, the prince was still nowhere near finding the First Stone. All he could see were trees and more trees."


    "Suddenly, there came a scream in a young maiden’s voice.\n \"HELP! SOMEONE! PLEASE HELP ME!!\""
    menu:
        "Go take a look":
            "The prince follows the scream, and sees five monsters ravaging a monster girl."
            m "Oh, it’s a human. Human. HUMAN!" with hpunch
            "The monsters attack him. \nThese monsters are stronger than the monsters he faced before. But he is still stronger than them. " with vpunch
            "Monster girl: \"Thank you very much!\""
            "The girl suddenly attacks him. He evades the blow and easily strikes her down." with hpunch
            p "Tch, like I couldn’t figure out things would turn out this way."
            m "She is far weaker than you, human knight, why did you have to kill her?"
            p "What now?"
            "[p] turns around and sees a monster. Its aura was so weak that he didn't even sense his presence."
            p "(Another feeble one? What a funny forest this is. Could it be that the monsters here spare the extra weak?)"
            p "(What a stupid move. They could still get the upper hand by stabbing you in the back.)"
            "The prince turns his head to see a normal sized monster."
            p "Your tone is annoying for that of a mere insect."
            m "Oh? Is that so?"
            p "Either run or bow down and beg right now if you don’t want to be tortured to death."
            m "Wow, sir, I’m soooooo scared. Can you pleeaase spare me your mercy?"
            p "..."
            "[p] clenches his sword. In a burst of speed akin to lighting, the prince slashes through the monster." with hpunch
            "When the monster collapses onto the ground, he kicks its wounds in rapid succession and stomps violently on its face." with vpunch
            p "If you dare use that sarcastic tone one more time, I'll make you wish you were never born."
            m "Oh? Why is that? What are you going to do about it, hmm?"
            "Angered by the mockery, the prince stabs the monster’s hand, causing a torrent of fresh blood to spew out." with vpunch
            m "Argh!"
            "The monster's hand twitches from the pain. The prince laughs maniacally."
            p "This feels... so... {i}good{/i}. All of my troubles and irritation up until this point, {i}I'll use you to relieve it!{/i}"
            m "..."
            p "You won't be dying so soon. Not before I'm satisfied and through with you."
            m "Ugh!"
            p "Beg me! BEG!!"
            "The monster smirks."
            m "I didn't know that a Royal palace hired a thug to take the position of a general. Have humans already become that rotten?"
            "[p] paused for a second, unblinking. Then, he begins to laugh."
            p "Ha...Hahaha..."
            p "I don't know where you've learnt to distinguish a general from a mere knight, but it doesn't matter. You'll die right now."
            "[p] brutally stabs [d]. He would twist his sword deep into their flesh, pull it out, only to stab them again and again." with hpunch
            m "Mnn...Nhh...ahaha..."
            "The monster doesn't move or say anything. But [p] knows he is still alive."
            p "Dammit. Why is this monster so irritating? It is as if he's taunting me."
            "The prince grows more furious."

        "Ignore":
            "The prince continues to drink water. Fifteen minutes later, the screaming still persists."
            m "Argh.. Help!"
            p "Ugh, how noisy!"
            "The prince feels like he is being watched."
            p "Who’s there?"
            "A monster walks out."
            m "You don't plan on helping her? I thought humans are all about maintaining their morals."
            "His voice is full of sarcasm."
            p "Get out of my sight."
            "The monster draws close to him. The prince doesn’t move. \nIts aura is even weaker than that of the small demon."
            m "Tell me, what makes a human come to such a place alone?"
            p "Go away before I kill you."
            "The monster grabs ahold of his sword and inspects it intently."
            m "Now {i}this{/i} is some good craftsmanship."
            p "(Since when? This monster...)\nThe prince takes his sword back and immediately slashes through the monster. The monster falls to the ground, covered in blood." with vpunch
            p "Normally, I don’t beat up weaklings, but you are just too annoying."
            m "Annoying? Interesting."
            "The monster laughs."
            m "No one’s ever spoken to me like that before."
            p "..."
            p "Either run, or bow down to me and beg right now, if you don’t want to be beaten to death."
            m "But sir, I’m hurt. My blood won't stop spilling. I can't run or bow down now. Can I only beg you instead?"
            "The prince kicks the monster’s wound repeatedly and stomps on its face." with hpunch
            p "Even a loser like you is making fun of me. Do I look like a joke? HUH?"
            p "Beg me! BEG!" with vpunch
            m "Please let me go!"
            "The prince stabs the monster’s hand, blood spews out. He laughs." with vpunch
            p "HAHAHAHAHAHA! More! Beg me more!"
            "He wrenches the blade of the sword deep into its flesh." with hpunch
            m "Ouch! Dear human, pretty pleeeeaaase let this lowly monster go! It hurts sooooooo much!"
            p "Shut The Fuck Up! Stop it with that sarcastic tone!"
            "The prince begins beating up the monster more brutally." with vpunch

    p "FUCK! You damned beast! You think I'm a joke too, don't you? HUH!?"
    "He stabs the monster again and again."
    "[p] looks at the monster wounds from head to toe, eyes landing on his erect crotch."
    p "Seriously? Are all monsters like this? Getting hard from being beaten to death? \nSuch a disgusting race!"
    m "\$.....\%"
    p "What?"
    "The monster talks so silently that [p] simply could not hear what they were saying. The monster looks at [p] with a devilish gaze, almost as if he wants [p] to hear it."
    p "..."
    "[p] clenches his sword hard, carefully bending over to hear what the monster has to say. He was so close to the monster that he can hear its breath."
    p "Repeat yourself if you have something to say."
    "Suddenly, a frigid chill runs down his spine and his gut was screaming at him to get out. His heart rate spikes from the rush of adrenaline, beating quickly as an intense aura swallows the area."
    "The monster's voice becomes deeper and more sinister as the prince winds up frozen by the sheer aura it is emanating. The monster whispers into his ears."
    m "Want to know why I'm hard? Because I can't help but want to pin you down on the ground and fuck your tight, obscene hole over and over again, until your brains fall out and you end up nothing but a senseless little fucktoy."
    p "!!!" with hpunch
    "[p] was shocked. Not only due the monster's obscene behavior, but also because it was the first time someone had ever spoken to him with such vulgar words."
    "He snaps out of his fear and steps backward, now bearing a defensive stance. The monster stands up, unfazed. His wounds were completely healed." with vpunch
    p "You... you healed yourself?"
    p "(Impossible! I can't even sense any magic from him. There was something rotten about him from the start!)"
    p "Did you absorb the power of other monsters?"
    "The monster smirks."
    "Absorption and power sharing are two very dangerous processes, you should know. Moreover, if a monster is involved in it some way or form, the absorber's appearance will be mutated, making them easy to tell apart."
    p "(He looks completely normal. This is insane. Not only was he able to heal himself, he heals all those fatal wounds with such speed and acts as if it's nothing.)"
    p "!!" with hpunch
    "The vines in the forest suddenly begin moving, grabbing ahold of the prince." with vpunch
    hide m_armor
    show vine at left with dissolve
    m "The image of you on the ground, begging, twisting your body like a bitch in heat just from my presence alone really does turn me on, you know?"
    p "You Sick Bastard!" with hpunch
    hide vine with dissolve
    show vinek at left with flash
    "The prince uses his dagger to hastily slice apart the vines. Quickly, he picks up his sword, stabbing the monster in a swift, fluid motion." with hpunch
    p "Ha!" with vpunch
    "The monster disappears. The very earth itself rises up to form a hand, slamming down against his whole body." with hpunch
    hide vinek
    show m_break2 at left
    p "Urgh!" with vpunch
    "The prince grows furious. \nHe concentrates his power on the tip of his sword and slashes though the gravel hand." with vpunch
    "From behind, the vine takes the opportunity to flank him, restraining him tightly. " with hpunch
    hide m_break1
    hide m_break2
    hide m_break3
    show vinebeat at left with flash
    p "Argh!"
    m "You’re not so smart, are you?"
    hide vinebeat
    show vinebeatfast at left
    "The vines wrap around him tighter." with vpunch
    p "Ugh!"
    p "I'm warning you! Let me go!"
    m "Beg me."
    hide vinebeatfast with dissolve
    show vinebreak2 at left with flash
    "The prince creates a barrier to destroy the vines. \n He falls to the ground in exhaustion."
    hide vinebreak2
    show m_break1 at left
    show m_beaten4 at left
    "The monsters kicks his stomach." with hpunch
    hide m_break2
    hide m_break4
    show m_break5 at left
    p "Arggghhh!...Ahhhh!"
    p "Ughhh..."
    "The monster cruelly stomps on it." with vpunch
    p "Urgh!"
    hide m_break5
    hide m_beaten4
    show trample
    "Poor little thing, you muuussst have been hurt a lot. Let me caress you"
    "The monster presses his foot against the prince’s groin."
    show m_break4:
        zoom 0.8
        ypos 600
        xpos -200
    show m_beaten4:
        zoom 0.8
        ypos 600
        xpos -200
    p "Get your foot off of me you fucking monster!!"
    hide m_break4
    hide m_beaten4
    "The monster stomps on his cock brutally."
    hide trample
    show trample_a
    hide m_beaten4
    show m_break5:
         zoom 0.8
         ypos 600
         xpos -200
    p "Stop that!"
    hide m_break5
    m "You are strange indeed. You allow yourself to do this to me, yet I can’t do this to you? It’s very unfair, you know."
    "He steps on him harder."
    hide trample_a
    show trample_b
    p "Mmhh..haa..haa\n...\nStop..."
    m "Shouldn't you be asking more nicely?"
    hide trample_b
    show trample_c
    "He steps on him even harder."
    p "P-please stop."
    m "You're going to have to beg more!"
    p "H-have some mercy!"
    m "For who? For this arrogant, dumb, prick?"
    p "F...for th – this… arroga.."
    "The prince clenches his teeth, swallowing his words"
    hide trample_c
    show trample_cum
    "The monster presses even harder"
    p "Ahaahh..."
    p "Urgh...ahhh"
    m "Now isn't that interesting? Seems like humans can even cum from pain."
    p "..."
    p "Hhh..."
    m "What's your name, brat?"
    p "..."
    hide trample_cum
    show trample_mouth
    "The monster shifts his foot from the prince's cock to his face."
    hide trample_mouth
    show trample_moutha
    p "N.."
    m "Want to play the silent game? It won't end pretty for you."
    hide trample_moutha
    show trample_a
    p "..N..n....n..ahaaa...haa"
    p ".N..m...Try...me!"
    "The monster laughs."
    hide trample_a
    show trample_cum
    m "Heh. You even dare to provoke me in this situation? \nI admire your stupidity, sir knight."
    "With the force of an explosion, the monster's foot barrels into his head, badly damaging his helmet." with hpunch
    p "Urgh....\n....n..."
    hide trample_cum
    hide m_break1
    hide m_break2
    hide m_break3
    hide m_break4
    show m_break5:
        zoom 0.8
        ypos 600
        xpos -200
    p "....F-fuc-k..."
    "The prince tries to get up. \nThe monster steps on his face, pushing him back down."
    hide m_break5
    show trample_moutha
    p "Urgh!"
    "The prince struggles."
    m "All you are doing is hurting yourself. And your helmet is in the way." with vpunch
    "The monster throws his helmet away."  with hpunch
    p "NO! DON'T!" with flash
    hide trample_moutha
    hide trample_cum
    show m_head_tired at left
    show m_m_sexclench1 at left
    show m_beaten3 at left
    show m_blush at left with flash
    p "..."
    m "Why, did you want to keep the helmet? What for? To conceal your disgraceful face?"
    p "Bastard!"
    m "It must be shameful for a knight to have his balls trampled on."
    hide m_head_tired
    hide m_m_sexclench1
    hide m_beaten3
    hide m_blush
    show m_head_close at left
    show m_m_clench at left
    show m_beaten3 at left
    show m_shame at left
    p "..."
    "[p]'s armor falls off. The monster squeezes his face."
    p "Nnn!"
    m "I like your face. Still looks like that of an arrogant brat, but otherwise, not bad at all. Makes me wonder how this face looks like when you tremble in fear and shame."
    hide m_head_close
    hide m_m_clenth
    hide m_beaten3
    hide m_shame
    show m_head_surprise at left
    show m_m_sexclench2 at left
    show m_beaten3 at left
    show m_blush at left
    p "(Fuck this monster!)\n(Just wait till I get my strength back)"
    m "What's your name, kid?"
    hide m_head_surprise
    hide m_m_sexclench2
    hide  m_blush
    hide m_beaten3
    hide m_m_clench
    show m_head_close at left
    show m_m_clench at left
    show m_beaten3 at left
    p "..."
    "The prince stays silent."
    "The monster pulls on his hair."
    show pull_armor
    p "Arghhh!"
    m "What is your name?"
    p"..."
    hide m_head_close
    hide m_m_clench
    hide m_beaten3
    hide pull_armor
    show pull_armor_hard
    "The monster clenches the back of his head roughly."
    p "Ahhh..ahh..ahh..."
    m "Talk!"
    menu:
        "Say it":
            $p = renpy.input("press enter to use the default name)", "Ray", length=20)
            p "[p]!...[p]!"
            hide pull_armor_hard
            "The monster releases him. [p] falls to the ground."
            show m_head_hurt at left
            m "See? It wasn't that hard."
            m "Hmm... your name sounds familiar, and your sword and armor show you are a high ranking general of the Royal Army. [p], [p]. I’ll find out more about this."
        "Stay silent":
            m "You are a stubborn one, aren’t you?"
            hide pull_armor_hard
            show m_head_hurt at left
            "The monster releases him. The prince falls to the ground."
            m "You see..."
            show m_head_hurt2 at left
            "The monster kicks him brutally." with vpunch
            p "Argh...argh..ahhh"
            hide m_head_hurt2
            m "I’m pretty stubborn too. I can beat you all day and night till you do what I tell you to."
            "He drags the prince's head up."
            show pull_armor_hard
            p "Urg...aghh..."
            m "I’ll ask you again, what’s your name?"
            $p = renpy.input("(press enter to use the default name)", "Ray", length=20)
            p "[p]! ..m.ngh.. [p]!"
            hide pull_armor_hard
            hide m_head_hurt
            show m_head_close at left
            show m_beaten6 at left
            show m_shame at left
            show m_m_sexopen at left
            m "[p]. Good boy! See? It wasn’t that hard."
            m "Hmm... your name sounds familiar. Plus, your sword and armor show you are a high ranking general of the Royal Army. [p], [p]. I’ll find out more about this."

    $d = renpy.input("I'm...(press enter to use the default name)", "Dietrick", length=20)
    d "I'm [d]. The oldest monster in this forest. \nNice to meet you."
    hide m_head_close
    hide m_beaten6
    hide m_shame
    hide m_m_clench
    show m_head_tired at left
    show m_beaten6 at left
    show m_m_sexclench1 at left
    p "..."
    d "Shouldn’t you be saying \"Nice to meet you too\", [p]?"
    "The prince clenches his hands and teeth."
    hide m_head_tired
    hide m_beaten6
    hide m_m_sexclench1
    show m_head_close at left
    show m_beaten6 at left
    show m_shame at left
    show m_m_sexclench2 at left
    p "Nice to meet you too."
    "[d] laughs."
    d "You have good manners, [p]."
    "The monster goes away."
    hide m_head_close
    hide m_beaten6
    hide m_m_sexclentc2
    show m_head_hurt at left
    show m_beaten6 at left
    "[p] tries to get up but he can’t, being beaten up so badly. \nNever in his life had he been though a shameful situation as this. \nHe wants to cut that monster into a thousand pieces and burn what’s left."
    hide m_head_hurt
    hide m_beaten6
    show m_head_surprise at left
    show m_m_sexclench1 at left
    show m_beaten6 at left
    p "..Mm..fuck!!"
    n "See, I told you."
    hide m_head_surprise
    hide m_m_sexclench1
    hide m_beaten6
    show m_head at left
    show m_m at left
    show m_beaten6 at left
    show n_smile at right with dissolve
    "The demon boy appears."
    if show:
        hide m_surprise
        hide m_m_clench
        hide m_m
        hide m_beaten6
        show m_head_close at left
        show m_m at left
        show m_beaten6 at left
        p "You...you haven't...gotten out of here"
        n "Why? This is my home."
        hide m_head_close
        show m_head at left
    "[p] looks away"
    p "You're gonna laugh at me now?"
    hide n_smile
    hide m_m_clench
    show n at right
    n "You aren't asking for my help?"
    hide m_m
    show m_m_clench at left
    p "Fuck you! Don't jest with me!"
    "Ray feels thirsty. So thirsty as if he could die. \nThe demon boy throws Ray’s backpack at him."
    hide n
    show n_smile2 with dissolve:
        xpos 750
    n "It’s yours right? You should keep your belongings near you."
    hide m_m_clench
    show m_m at left
    p "..."
    n "Sir Knight, please get out of this forest. Don't look for The Stone anymore. It's for your own good"
    p "..."
    hide n_smile2 with dissolve
    "The demon goes away."
    hide m_m
    hide m_head
    hide m_beaten6
    show m_head_tired at left
    show m_beaten6 at left
    show m_m at left
    p "..."
    "Using his head and teeth, [p] opens his bag to get a drink of water. A lot of the water spills out."
    hide m_m
    hide m_m_sexopen
    show m_m_sexopen at left
    show m_beaten5 at left
    p "(What a waste...)"
    hide m_m_sex_open
    show m_m
    p "..."
    p "(...Did that demon just help me despite how I treated him?)"
    hide m_beaten5
    hide m_m
    show m_head_close at left
    show m_beaten5 at left
    show m_m at left
    p "(Gosh! I despise those personalities the most...)"
    "[p] falls asleep before he realizes it."
    scene black with fade
    pause .5
    scene darkforest with dissolve
    "Morning comes."
    show m_head_close at left
    show m_m_clench at left
    p "Ugh!"
    "[p] tries to get up but falls back to the ground. His entire body still trembles in pain. Especially his crotch, head, and stomach."
    "Hm..."
    hide m_head_close
    hide m_m_clench
    show m_head_surprise at left
    show m_m_sexclench1 at left
    p "Bastard!"
    d "You seem to be doing well. Better than I thought."
    "[p] glances at him."
    p "(Why is it still here?)"
    d " Hahaha! Why look at me with such pleading eyes? In love with me? Or perhaps you lust for me? You were very hot last night, you should know."
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    p "Fucking scumbag!"
    hide m_head_surprise
    hide m_m_sexclench2
    show m_head_close at left
    show m_m at left
    "[p] goes past [d]."
    d "I heard that you are a prince."
    hide m_head_close
    hide m_m
    show m_head_surprise at left
    show m_m_clench at left
    p "!"
    hide m_m_clench
    hide m_head_surprise
    show m_head at left
    show m_m_sexclench2 at left
    p "I'm not."
    d "Not anymore?"
    hide m_head
    hide m_m_sexclench2
    show m_head_surprise at left
    show m_m_sexclench1 at left
    p "!"
    hide m_head_surprise
    hide m_m_sexclench1
    show m_head at left
    show m_m_clench at left
    p "(Since when did monsters in the Dark Forest know that so about humans? This is too dangerous...)"
    hide m_head
    hide m_m_clench
    show m_head_close at left
    show m_m at left
    "[p] ignores [d] and continues forward."
    hide m_head_close
    hide m_m
    show m_head at left
    show m_m at left
    d "I’m not done talking to you."
    "[p] ignores [d] completely."
    "[d] laughs."
    d "Seems like your dad’s so busy that he did a poor job raising his child. Spoiled you too much."
    hide m_head
    hide m_m
    show m_head_surprise at left
    show m_m_sexclench1 at left
    "[p] turns back, glances at [d]"
    p "!" with vpunch
    hide m_m_sexclench1
    show m_m_clench at left
    p "(Something is moving..)"
    "From underground, dozen of vines wrap around [p]'s legs. He falls to the ground."
    hide m_m_clench
    show m_m_sexclench1 at left
    show m_shame at left
    p "(Shit! What the fuck?!)"
    "[p] uses all his strength to try and get up, yet his movements were too slow. The vines squeeze him tight."
    hide m_head_surprise
    hide m_m_sexclench1
    show vinehead:
        xpos-30
    p "Arghh!"
    d "I can help your dad with teaching you some manners..."
    hide vinehead
    show vinehead_shit2:
        xpos-50
    p "Fuck you!"
    d "...by beating you up till you’re on you knees."
    hide vinehead_shit2
    hide m_shame
    show vinehead_blush:
        xpos-50
    p "You asshole!"
    d "..."
    d "Look at him, such a naughty boy, keeps on interrupting me. Silence him!"
    "The vines squeeze stronger and tighter."
    hide vinehead_blush
    show vinehead:
        xpos-50
    p "Aaaaa! Arghhh!...m..."
    "[d] laughs"
    d "That's better. What a nice sound in comparison."
    hide vinehead
    show vinehead_shit:
        xpos-50
    p "Mm...h"
    hide vinehead_shit
    hide m_m_sexclench1
    show vinehead0020:
        xpos-50
    p "(Fuck!)"
    "[p] tries to release his barrier again to destroy the vines."
    d "Hahahah, seems like idiots never learn! Up, Pitchy!" with hpunch
    scene sky with dissolve
    hide vinehead
    show vinehead with dissolve:
        xpos-30
    "The vines shoot up to the sky." with vpunch
    hide vinehead
    show vinehead_shit:
        xpos-50
    p "S-shit!"
    "A giant stone hand carries [d] to the sky."
    hide vinehead_shit
    show vinehead_shit2:
        xpos-50
    p "..."
    p "Mm...nn.."
    d "Loosen his binds a bit. I want to talk."
    hide vinehead_shit2
    show vinehead_breath:
        xpos-50
    "The vines stop squeezing [p]."
    p "Haaa...haaaa..."
    p "What do you want?"
    "[d] licks [p]'s ear and whispers."
    hide vinehead_breath
    show vinehead_blush:
        xpos-50
    d "Let's make a deal. \nI'll help you sit on the throne you rightfully deserve. And in turn, you will become my slave."
    hide vinehead_blush
    show vinehead_blush2:
        xpos-50
    p "What the fuck?!? In your dreams you lowly monster! You're insane!"
    d "HAHAHAHAHAHAHAHAHA!" with vpunch
    d "If I'm a lowly monster, then what does that make you, sir prince?"
    "[d] tears [p]'s clothing off."
    hide vinehead_blush2 with vpunch
    show m_heavybreaksurprise at left
    show m_m_sexclench1 at left
    show m_shame at left
    show m_beaten2 at left
    p "!"
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    d "Remember last night? Your entire body trembling under my feet while your mouth couldn't stop begging me like a cute little pet?"
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    show m_blush at left
    p "I-I'm not..."
    hide m_blush
    hide m_m_sexclench1
    show m_m_clench at left
    d "Really?"
    "[d] touches [p]'s cock."
    hide m_heavybreaksurprise
    hide m_blush
    hide m_shame
    hide m_beaten2
    hide m_m_sexclench1
    show m_heavybreaktired at left
    show m_blush at left
    show m_m_sexclench2 at left
    show m_beaten2 at left
    p "Mm-!"
    "[d] squeezes it harder."
    hide m_heavybreaktired
    hide m_blush
    hide m_m_sexclench3
    hide m_beaten2
    show m_heavybreakclose at left
    show m_blush at left
    show m_beaten2 at left
    show m_m_sexopen at left
    p "N-nh!"
    d "You really turned me on that time."
    hide m_m_sexopen
    hide m_m_clench
    show m_shame at left
    show m_m_sexclench3 at left
    p "Aa-ah....hhhh"
    "[d] rips off [p]’s remaining clothing, leaving him completely naked." with hpunch
    hide m_m_sexclench2
    hide m_heavybreaksurprise
    hide m_heavybreakclose
    hide m_m_sexclench3
    hide m_shame
    hide m_blush
    hide m_beaten2 with hpunch
    show m_surprise at left
    show m_cockdown at left
    show m_blush at left
    show m_m_sexclench1 at left
    show m_beaten3 at left
    p "W-What are you doing?" with vpunch
    "[d] touches [p]'s stomach."
    hide m_surprise
    hide m_cockdown
    hide m_blush
    hide m_m_sexclench1
    hide m_beaten3
    show m_close at left
    show m_m_sexopen at left
    show m_shame at left
    show m_blush at left
    show m_cockdown at left
    show m_beaten3 at left
    p "H!.."
    d "Say [p], between the two of us, which one of us is a lowly nobody?"
    "[p] spits on [d]'s face"
    hide m_shame
    hide m_close
    hide m_blush
    hide m_cockdown
    hide m_beaten3
    hide m_sexopen
    show m_surprise at left
    show m_m_clench at left
    show m_beaten3 at left
    show m_cockdown at left
    p "Isn't it clear? A lowborn creature like you will always be beneath my feet!"
    "[d] laughs maniacally."
    d "Interesting. You are the first one to ever say that to me. Even monsters and demons who are far stronger than you dare not say that."
    d "It's funny. But also annoying."
    "[d] clenches his fingers around the back of [p]'s head."
    hide m_m_sexclench1
    hide m_surprise
    hide m_beaten3
    hide m_cockdown
    show m at left
    show m_cockup at left
    show m_m_scream at left
    show m_beaten3 at left
    show m_shame at left
    p "Aghhh!...Ah"
    d "Who is it, you masochistic brat?!"
    hide m
    hide m_cockup
    hide m_m_scream
    hide m_beaten3
    hide m_shame
    hide m_m_sexopen
    show m_hurt at left
    show m_m_sexopen at left
    show m_beaten3 at left
    show m_cockup at left
    show m_shame at left
    show m_blush at left
    p "Agh...F-Fuck!..Aghhh!...You!...Agh!"
    "[d]'s eyes flash red!"
    hide m_m_sexopen
    hide m_shame
    show m_shame at left
    show m_m_sexclench3 at left
    p "...m...Fuck you!"
    d "..."
    d "Your will is strong. It's impressive. But it won't stay that way for long."
    hide m_m_sexclench3
    show m_m_sexopen at left
    p "What the fuck you blabbing on about?"
    d "Hey Pitchy, seems like our prince has gotten so comfortable that he's forgotten who owns him. Why don't you tighten your grip, and play with him however you like?"
    "The vines squeeze [p]'s body tightly and pull [p]'s nipples taut, until it can't stretch anymore."
    hide m_m_sexopen
    hide m_beaten3
    hide m_cockup
    hide m_shame
    show m_nipple at left
    show m_m_sexclench3 at left
    show m_beaten7 at left
    show m_cockup at left
    show m_shame at left
    p "Kuh!...aaahhhh"
    d "Who is it, brat?"
    hide m_m_sexclench3
    show m_m_sexclench1 at left
    show m_blush at left
    p "...H!...You!"
    "[d] smiles."
    d "Listen up kid. Being stubborn with me is never going to work. I'm actually pretty good at teaching manners to rebellious brats like you."
    d "Stretch his cock Pitchy."
    hide m_m_sexclench1
    hide m_cockup
    show m_cockvine at left
    show m_m_scream at left
    p "NO! STOP! AGHHHH!"
    d "Shut up. You annoy me."
    "A vine thrusts into [p]'s throat."
    hide m_m_scream
    show m_m_vine at left
    p "Mm.....h"
    "[p] tries to stop the vines. It only wraps around him tighter, fucking and thrusting into his mouth harder and harder."
    show vinecock with dissolve
    p "H..m..! Grghhh! Ggggg..!"
    p "Mmm...mmm"
    "The vines wrap around [p]'s dick and nipples, squeezing them like a balloon." with vpunch
    p "mmmm..n..s-!"
    d "You seem to enjoy it. What a perverted prince!"
    "Everyone just kept spreading rumors of you, saying that you know nothing about having fun. Seems like they don't understand you at all."
    show vinecockfast
    p "mm...nn..f-.."
    d "If you knew this day would come, you wouldn't have had to try so hard all through your life. \nIn the end, whatever you achieve doesn't matter. You’d still end up becoming my adorable little sex toy."
    p "S-s-...! L-... m-.. g..!"
    d "What? You said you're happy to become my sex toy? You are most certainly welcome!"
    d "Pitchy, hear that? Pick up your pace. Our prince loves it!"
    hide vinecock
    hide vinecockfast
    show vinecockcum
    p "F-fu-...mm....nngh"
    p "h..hgh...ahhhhhhhh"
    d "Oh wow, our prince came from being facefucked by a plant!"
    hide vinecockcum
    hide m_m_vine
    show m_m_scream at left
    show m_blush at left
    show m_shame at left
    "[p] bites the vine invading his throat. The vine pulls out of his mouth."  with hpunch
    p "Haaa...Haaaa! Let! Me! Go!"
    d "Sure!"
    scene sky with hpunch
    "The vines release [p]. He falls from the sky down to the trees, slipping from branch to branch, tumbling down like a helpless object. \nHe tries to grab on to anything he can, yet his whole body is already badly injured from the swift descent." with vpunch
    p "H...haah.." with vpunch
    scene darkforest
    "[p] falls straight to the ground."
    show m_hurt at left
    show m_beaten3 at left
    show m_sperm at left
    show m_m_sexclench3 at left
    show m_shame at left
    show m_cockdown at left
    p "(It hurts!... My back!)"
    p "Nggh..."
    d "Falling from such heights and yet you aren't dead? What a miracle!"
    p "..."
    hide m_m_sexclench3
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    p"..mhh.."
    d " That look really does suit you."
    d "Your naked body is making my cock really, really hard, and it won't stop telling me to make you my very own sex toy."
    show m_blush at left
    p "B-bas..."
    "[d] uses his foot to caress [p]'s cock"
    hide m_m_sexclench1
    show m_m_sexopen at left
    p "Mmm..nn..."
    p "(It hurts! Damm this scumbag!)"
    d "It must be hard for you. \nI heard you had never lost before this, so you're still quite full of yourself."
    "[d] gently squeezes it."
    hide m_hurt
    hide m_beaten3
    hide m_sperm
    hide m_shame
    hide m_cockdown
    hide m_m_sexopen
    hide m_blush
    show m_close at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexclench3 at left
    show m_cockup at left
    p "...m...n..."

    d "Understand this; for me, you are but a pathetic insect."
    hide m_m_sexclench3
    show m_m_sexclench1 at left
    p "M...h..."
    hide m_m_sexclench1
    show m_m_sexclench3 at left
    p "Haaa...haaaa..."
    hide m_m_sexclench3
    show m_m_sexopen at left
    p "H..*cough* *cough*"
    hide m_m_sexopen
    show m_m at left
    p "*gulp*"
    hide m_m
    show m_m_sexclench1 at left
    p "...m..."
    d "You seem so helpless right now. I almost feel bad for you."
    hide m_m_sexclench1
    show m_m_sexclench2 at left
    p "Fuck you!"
    d "I have a wonderful idea. Prince [p], if you suck my cock, I'll let you rest for a bit. Otherwise, I'll have Pitchy play with you till you kneel and beg for my cock."
    hide m_m_sexclench2
    show m_m_sexclench1 at left
    p "Bastard! In your dreams! I'll cut your cock in half!"
    d "Pitchy!"
    hide m_close
    hide m_beaten3
    hide m_sperm
    hide m_shame
    hide m_cockup
    hide m_m_sexopen
    hide m_blush
    show m_surprise at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexclench3 at left
    show m_cockup at left
    p "!"
    show vinecocktree with vpunch
    "The vines lift [p] up and continue to stretch [p]'s cock and nipples."
    p "...mngh..."
    d "Have fun, brat. I'll let you catch up on {i}all{/i} the fun you've missed in the past."
    scene black with fade

    "Day 2"
    scene darkforest with dissolve
    show m_nipple
    show m_m_sexclench3
    show m_beaten7
    show m_cockvine
    show m_shame
    show m_m_vine
    p "Mm...n...h"
    p "(Fuck! How long do I have to stay here with these disgusting vines! I’ve had enough!)"
    p "...mm...nnh..."
    "[d] appears out of thin air."
    d "Hey [p], feel like getting out yet?"
    p "F-...mm..."
    d "Okay, got it! Stay here and have fun with Pitchy, won't you?"
    "[d] left."
    p "...M-mmh..."
    scene black with fade
    "Day 3"
    scene darkforest_night with dissolve
    show m_nipple at left
    show m_sperm at left
    show m_m_sexclench3 at left
    show m_beaten7 at left
    show m_cockvine at left
    show m_shame at left
    show m_m_vine at left
    p "...ngh...h..."
    d "You seem less lively."
    p "Mm...n!"
    d "Want to get out?"
    "[p] nods."
    "[d] smirks."
    p "..."
    d "Release him Pitchy!"
    "[p] falls to the ground." with vpunch
    hide m_nipple
    hide m_sperm
    hide m_m_sexclench3
    hide m_beaten7
    hide m_cockvine
    hide m_shame
    hide m_m_vine
    show m_tired at left
    show m_sperm at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m_sexopen at left
    show m_cockdown at left
    p "Ha...haaa...haaa..h....m..."
    "[p] closes his eyes."
    hide m_tired
    hide m_sperm
    hide m_beaten3
    hide m_sperm
    hide m_blush
    hide m_shame
    hide m_m_sexopen
    hide m_cockdown
    show m_close at left
    show m_sperm at left
    show m_beaten3 at left
    show m_sperm at left
    show m_blush at left
    show m_shame at left
    show m_m at left
    show m_cockdown at left
    d "The fuck? You plan on sleeping after all this?"
    menu:
        "Let him sleep":
            d "Oh well. Have a good rest. I'll play with you later"
            d "Tie him up. Not so tightly that it wakes him up, just make sure he can't escape."
            scene black with fade
            "Day 4"
            scene darkforest with dissolve
            p "...m..."
            show m_close at left
            show m_beaten1 at left
            show m_blush at left
            show m_shame at left
            show m_m at left
            show m_cockdown at left
            "[p] wakes up!"
            hide m_close
            hide m_beaten1
            hide m_blush
            hide m_shame
            hide m_m
            hide m_cockdown
            show m_tired at left
            show m_m at left
            show m_beaten1 at left
            show m_cockdown at left
            p "How long have I been asleep?"
            hide m_tired at left
            hide m_m at left
            hide m_beaten1 at left
            hide m_cockdown at left
            show m_surprise at left
            show m_m_clench at left
            show m_beaten1 at left
            show m_cockdown at left
            p "!"
            hide m_m_clench
            show m_m_sexclench2 at left
            p "I can't move!"
            "[p] looks around and sees the vines wrapping him around a tree."
            scene tie_looka with dissolve
            p "Fuck, that scumbag!"
            d "What did you say about me?"
            show m_surprise at s
            show m_m_clench at s
            show m_beaten1 at s
            p "!"
            hide m_m_clench
            show m_m_sexclench2 at s
            p "(He's been here all this time?)"
            "(Please click on [p] to continue)"
        "Torture him more":
            "[d] kicks [p]"
            d "Wake up, brat!"
            hide m_m
            show m_close at left
            show m_beaten1 at left
            show m_blush at left
            show m_shame at left
            show m_m_sexclench2 at left
            show m_cockdown at left
            p "..m.."
            hide m_m_sexclench2
            show m_m_clench at left
            p "..."
            d "Remember what I said. Give me a blowjob now, or I'll let Pitchy continue to play with you."
            p "..."
            hide m_close
            hide m_beaten1
            hide m_blush
            hide m_shame
            hide m_m_sexclench2
            hide m_cockdown
            show m_nipple2 at left
            show m_sperm at left
            show m_beaten7 at left
            show m_cockvine at left
            show m_shame at left
            show m_m_sexclench1 at left
            hide m_cockdown at left
            "The vines wrap around [p] tightly."
            hide m_m_sexclench1
            show m_m_scream at left
            pause .5
            hide m_m_scream with dissolve
            show m_m_sexclench3 at left
            p "Argh!"
            "[d] touches [p]'s face"
            d "So?"
            hide m_m_sexclench3
            show m_m_sexopen at left
            p "Do whatever you want with me, bastard! I'll never do anything you say!"
            d "Well put."
            d "Pitchy!"
            hide m_nipple2
            hide m_sperm
            hide m_beaten7
            hide m_cockvine
            hide m_shame
            hide m_m_sexclench1
            hide m_cockdown
            show m_nipple at left
            show m_sperm at left
            show m_beaten7 at left
            show m_cockvine at left
            show m_shame at left
            show m_m_scream at left
            pause 1.0
            hide m_m_scream with dissolve
            show m_m_sexclench3 at left
            p "Argh!"
            d "I like your spirit. Keep it up, [p]!"
            hide m_m_sexclench3
            show m_m_sexclench1 at left
            p "Motherfuck-...m...ngh"
            hide m_m_sexclench1
            show m_m_vine at left
            p "...m...ngh..."
            scene vinecocktree
            show night
            p "...ngh..."
            scene black with dissolve
            "Day 4"
            show vinecocktree
            p "m...n.."
            p "..."
            "[p] is about to die from asphyxiation."
            d "Release him gently. Our helpless princess seems to be one step from Hell’s door."
            "The vines slowly descend [p] onto the ground"
            scene darkforest
            show m_close at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench2 at left
            show m_cockdown at left
            p "...m..."
            "[p] is lying on the ground, cover by sweat. His whole body trembling as he slowly takes long, deep breaths."
            hide m_m_sexclench2
            show m_m_sexopen at left
            p "Haaah... haaa..."
            "[p] lies there, motionless and completely vulnerable. It seems like he cannot even move a muscle."
            "[d] touches [p]'s face."
            d "Has anyone ever told you that you look awfully cute when you're suffering?"
            hide m_close
            hide m_sperm
            hide m_beaten1
            hide m_shame
            hide m_m_sexclench2
            hide m_cockdown
            show m_tired at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockdown at left
            "[p] tries to push [d]'s hand away. But he's too weak."
            hide m_m_sexclench1
            show m_m_sexclench2 at left
            p "Fuck you! I'll slash your tongue in half."
            d "You are funny. People kept saying the firstborn prince is smart and strong, yet all I can see is the opposite. Dumb, and {i}pathetic{/i}."
            hide m_tired
            hide m_sperm
            hide m_beaten1
            hide m_shame
            hide m_m_sexclench2
            hide m_cockdown
            show m_surprise at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockdown at left
            p "Damn you!"
            "[d] strokes [p]'s face."
            d "But you are indeed a very interesting creature. I have never seen anything this entertaining."
            p "SHUT U-mph!"
            "[d] covers [p]'s mouth."
            "[d]'s eyes flash red."
            p "?"
            "[d] smirks."
            d "Still nothing? You really are stubborn."
            d "Consider yourself lucky, or perhaps unlucky, but at least I'll be teaching you some great life lessons, kid."
            "[d] touches [p]'s cock"
            hide m_cockup
            show m_blush at left
            show m_cockdown at left
            p "Mn...S-shit! Get your filthy hands away from me!..N..."
            d "Tie him up, Pitchy!"
            hide m_m_sexopen
            hide m_surprise
            hide m_sperm
            hide m_beaten1
            hide m_shame
            hide m_blush
            hide m_m_sexclench1
            hide m_cockup
            show m_tired at left
            show m_sperm at left
            show m_beaten1 at left
            show m_shame at left
            show m_m_sexclench1 at left
            show m_cockup at left
            show m_blush at left
            p "F-Fuck!"
            hide m_m_sexclench1
            show m_m_sexclench2 at left
            "(Please click on [p] to continue)"

#############################################################################################  Sim start (no proofreading here
    $water = 20
    $food = 30
    $mental = 90
    $pride = 100
    $ene = 100 #(energy)
    $day =4
    $fuckoff =0
    $nothing =1
    $clean = 90
    $bath = 0
    $controlStage = 0
    jump sim


    return
