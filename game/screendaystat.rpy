screen day:
    text ("Day %d" %day):
        xpos 5
        ypos 20
        font "Benegraphic.ttf"
    imagebutton idle ("gui/button/donate.png") hover ("gui/button/donate_hov.png") xpos 1700 ypos 1220 action OpenURL("https://sponsus.org/u/vivigames")
    imagebutton idle ("gui/button/home.png") hover ("gui/button/home_hov.png") xpos 1700 ypos 1140 action OpenURL("https://thaovyletruong.wixsite.com/vivi/copy-of-home")
    imagebutton idle ("gui/button/donate.png") hover ("gui/button/donate_hov.png") xpos 1700 ypos 1060 action OpenURL("https://subscribestar.adult/pride-and-submission")

screen stat:
    text ("Energy: %d" % ene):
        xpos 10
        ypos 100

    text ("Water: %d" % water):
        xpos 10
        ypos 150

    text ("Food: %d" % food):
        xpos 10
        ypos 200

    text ("Pride: %d" % pride):
        xpos 10
        ypos 250

    text ("Psyche: %d" % mental): 
        xpos 10
        ypos 300

    text ("Cleaniness: %d" % clean):
        xpos 10
        ypos 350
