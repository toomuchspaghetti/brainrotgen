from moviepy.editor import *
import moviepy.video.fx.all as vfx
import moviepy
from os import listdir
from random import randint, random, choice
from math import sin, ceil

moviepy.config.FFMPEG_BINARY = "ffmpeg-2024-08-28-git-b730defd52-full_build\\bin\\ffmpeg.exe"

cant_wait_to_meet_you = False

def get_brainrot():
    global cant_wait_to_meet_you

    if cant_wait_to_meet_you:
        cant_wait_to_meet_you = False
        return VideoFileClip("brainrot/skibiditoilet.mp4")
    
    return VideoFileClip(f"brainrot/{choice(listdir("brainrot"))}")

WIDTH = int(540/2)
HEIGHT = int(WIDTH/9*16)
HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)
AMOUNT_OF_BRAINROTS_IN_MAIN_BRAINROT = 10

def random_horizontal_anchor():
    return choice(['left', 'center', 'right'])

def random_vertical_anchor():
    return choice(['top', 'center', 'bottom'])

def maybe_invert_colors(clip):
    if maybe(3):
        return vfx.invert_colors(clip)
    return clip

def get_main_brainrot():
    brainrots = [main_brainrot_processing(get_brainrot()) for i in range(AMOUNT_OF_BRAINROTS_IN_MAIN_BRAINROT)]
    
    brainrots[0] = brainrots[0].crossfadein(2)
    brainrots[-1] = brainrots[-1].crossfadeout(2)
    
    return concatenate_videoclips(brainrots, method="compose")

def get_special_brainrot():
    brainrot = get_brainrot().fx(vfx.resize, width=HALF_WIDTH)

    brainrot = maybe_invert_colors(brainrot)
    
    if maybe(8):
        degrees = 90 * (1 if maybe() else -1)
        brainrot = vfx.rotate(brainrot.add_mask(), lambda t: sin(t) * degrees)
    
    if maybe(5):
        if maybe():
            horizontal_anchor = random_horizontal_anchor()
            
            brainrot = brainrot.set_position(lambda t: (horizontal_anchor, sin(t)), relative=True)
        else:
            vertical_anchor = random_vertical_anchor()
            
            brainrot = brainrot.set_position(lambda t: (sin(t), vertical_anchor), relative=True)
    else:
        brainrot = brainrot.set_position((random_horizontal_anchor(), random_vertical_anchor()))
    
    if maybe(5):
        b = random() + 1
        brainrot = vfx.resize(brainrot, lambda t: 1.5 + sin(t*b))
            
    return brainrot

def maybe(odds_against_you = 1):
    return not randint(0, odds_against_you)

def random_horizontal_anchor():
    return choice(["left", "center", "right"])

def normal_brainrot_processing(brainrot):
    return brainrot.set_position('center', 'center').fx(vfx.resize, width=WIDTH)

def main_brainrot_processing(brainrot):
    brainrot = normal_brainrot_processing(vfx.speedx(brainrot, max(brainrot.duration / 10 + random() / 5, 0.75)))
    
    return brainrot

def get_uber_brainrot():
    brainrots = [get_main_brainrot()]
    
    start = 3
    
    for i in range(35):
        brainrots.append(get_special_brainrot().set_start(start))
        start += 1 + random()
        
    return CompositeVideoClip(brainrots, size=(WIDTH, HEIGHT))

def compilation_style_brainrot():
    return normal_brainrot_processing([main_brainrot_processing(get_brainrot()) for i in range(AMOUNT_OF_BRAINROTS_IN_MAIN_BRAINROT)], method="compose")

def grid_style_brainrot(side_length):
    return clips_array([[vfx.resize(compilation_style_brainrot(), width=int(WIDTH/side_length)) for i in range(side_length)] for i in range(side_length)])

styles = {
    "uber": get_uber_brainrot,
    "compilation": compilation_style_brainrot,
    "grid": grid_style_brainrot
}

style = input(f"what style? ({"/".join(styles.keys)}) >")

if style in styles:
    for i in range(int(input("how many times? >"))):
        brainrot = styles[style]()

        brainrot.write_videofile(f"output/{randint(1000, 9999)}.mp4", fps=15)
else:
    print("idk what that is")