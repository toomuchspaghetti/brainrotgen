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
    
    # match randint(0, 2):
    #     case 0:
    #         brainrot = brainrot.set_position((random_horizontal_anchor(), random_vertical_anchor()))
    #     case 1:
    #         horizontal_anchor = random_horizontal_anchor()
            
    #         brainrot = brainrot.set_position(lambda t: (horizontal_anchor, sin(t) * HALF_HEIGHT / 2))
    #     case 2:
    #         vertical_anchor = random_vertical_anchor()
            
    #         brainrot = brainrot.set_position(lambda t: (sin(t) * HALF_WIDTH / 2, vertical_anchor))
            
    return brainrot

def maybe(odds_against_you = 1):
    return not randint(0, odds_against_you)

def random_horizontal_anchor():
    return choice(["left", "center", "right"])

def main_brainrot_processing(brainrot):
    brainrot = vfx.speedx(brainrot, max(brainrot.duration / 10 + random() / 5, 0.75)).set_position('center', 'center').fx(vfx.resize, width=WIDTH)
    
    return brainrot


# def get_brainrot():
#     brainrots = listdir("brainrot")
#     brainrot = VideoFileClip(f"brainrot/{brainrots[randint(0, len(brainrots) - 1)]}")
#     if randint(0, 2):
#         brainrot = brainrot.fx(vfx.resize, width=THIRD)
#     else:
#         brainrot = brainrot.fx(vfx.resize, width=WIDTH)
#         brainrot = brainrot.fx(vfx.speedx, random() * 2 + 0.9)
#         brainrot = brainrot.set_opacity(0.5)
#         return brainrot 
    
#     if maybe():
#         if maybe():
#             brainrot = brainrot.set_position(('center', random_vertical_position()))
#         else:
#             horizontal = random_horizontal_position()
#             brainrot = brainrot.set_position(lambda t: (horizontal, sin(t) * 100)) 
#     else:
#         brainrot = brainrot.set_position(random_horizontal_position(), random_vertical_position())
    
#     if maybe():
#         brainrot = brainrot.crossfadein(1).crossfadeout(1)
        
#     if not randint(0, 5):
#         brainrot = brainrot.fx(vfx.invert_colors)
        
#     brainrot = brainrot.fx(vfx.speedx, random() * 2 + 0.9)
    
#     if maybe():
#         brainrot = brainrot.crossfadein(randint(1, 5))
        
#     if maybe():
#         brainrot = brainrot.crossfadeout(randint(1, 5))
        
#     if not randint(0, 7):
#         brainrot = brainrot.rotate(135)

#     if maybe():
#         brainrot = brainrot.fx(vfx.mirror_x)
#         # if maybe():
#         #    brainrot = brainrot.fx(vfx.mirror_y)
            
#     if not randint(0, 5):
#         rotation_speed = random() * 3
#         brainrot = brainrot.fx(vfx.rotate, lambda t: sin(t*rotation_speed) * 360)
    
#     return brainrot


def get_uber_brainrot():
    brainrots = [get_main_brainrot()]
    
    start = 3
    
    for i in range(35):
        brainrots.append(get_special_brainrot().set_start(start))
        start += 1 + random()
        
    return CompositeVideoClip(brainrots, size=(WIDTH, HEIGHT))

for i in range(6):
    get_uber_brainrot().write_videofile(f"{randint(1000, 9999)}.mp4", fps=15)

# get_main_brainrot().write_videofile(f"{randint(1000, 9999)}.mp4", fps=24)
    