# Mihnea Burceag, Theodore Popescu, Matthew Bautista
# Advanced group number 1
# Drawing app
# Started 9/3/25

import random
import pygame  # imports pygame
import pygame_textinput
import time
import pyperclip
import ast
import zlib
import os
from tkinter import colorchooser
from tkinter import filedialog
import tkinter as tk

pygame.init()  # initializes pygame
screen = pygame.display.set_mode((1260, 750))  # set screen size
screen_canvas = pygame.Surface((1260, 750), pygame.SRCALPHA)
Screen_saving = pygame.Surface((1260, 750), pygame.SRCALPHA)
Screen_Loading = pygame.Surface((1260, 750), pygame.SRCALPHA)
screen_canvasUnder = pygame.Surface((1260, 750), pygame.SRCALPHA)
screen_canvasUnderMore = pygame.Surface((1260, 750), pygame.SRCALPHA)
screen_canvasUnderMoreMore = pygame.Surface((1260, 750), pygame.SRCALPHA)

clock = pygame.time.Clock()  # get the clock

radius = 15
brushSize = 3

selectedColor = 'red'
font = pygame.font.SysFont('Comic Sans MS', 28)

textinp = pygame_textinput.TextInputVisualizer()
textinput = pygame_textinput.TextInputVisualizer()  # new thingy

# Lists
Colors_M2 = ['orange', 'red', 'yellow']
List_OF_colors = ['orange', 'red', 'yellow']
images = []
elements = []
P_lis = []
Strokes = []
num = 1
undo_stack = []
max_s = 10


def Snapshot():
    if len(undo_stack) >= max_s:
        undo_stack.pop(0)
    undo_stack.append(screen_canvasUnder.copy())


screen.fill('white')

# booleans
pp = None
Sidebar = None
questioning2 = None
content = None
last_pos = None
running = True
Mouse_CC = False
Mouse_Cur = False
lastFrameClicked = False
undoFrameClicked = False
new_w = False
mango_image = False
mango_marker_TF = None
Marker_2_TF = False
Which_marker = True
new_pos = None
Which_marker2 = None
Nww = None
Marker_2_mouse_vis = False
questioning = False  # new
opening = False  # new
opening2 = False
Water = None
opening3 = None
Button_1 = True
Button_2 = None
Button_3 = None
Image_upload = None
Back_no = None
Word_over = False
Saving_bg = None
Loading_bg = None
canDraw = True
screen_width, screen_height = 1260, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MANGO DRAW")

uploaded_image = None
image_rect = None
border = pygame.image.load(
    "AAA Mango Draw UI v.4.1.0 (FINAL).png")  # Get the UI file location and set it to the canvas image.
bor_rect = border.get_rect()
Mango_Icon = pygame.image.load('mangoicon (1).png')
ref = pygame.image.load(
    "mangoref.png")  # Get the UI file location and set it to the canvas image.
ref_rect = ref.get_rect()
pygame.display.update()
x_coordinate = 850
save_background = pygame.image.load("save.png")
saving_background = pygame.transform.scale(save_background, (600, 300))
load_back = pygame.image.load('load.png')
Loading_background = pygame.transform.scale(load_back, (600, 300))
mango_marker = pygame.image.load("mango67.png")  # gets the marker image
mango_rect_d = mango_marker.get_rect()  # finds the dimesions of the marker and makes it into a rectangle
mango_rect_d.topleft = (x_coordinate, 128)
pygame.display.flip()
mouse_pos = pygame.mouse.get_pos()  # get the mouse position
move_left_mango_m = mango_rect_d.x - 20  # here it takes the x value of the mango marker and moves it 20 pixels to the left

mango_cursor = pygame.image.load("mango67_use.png")
mango_cursor_rect = mango_cursor.get_rect()
Mouse_marker_2 = pygame.image.load('best_marker_use.png')
Marker_2 = pygame.image.load('best_marker.png')
Marker_2_rect = Marker_2.get_rect()
Marker_2_rect.topleft = (800, 150)
pygame.display.flip()
move_left = Marker_2_rect.x - 20
Drawing_mango_folder = 'MangoDrawings'

Mango_Sidebar = pygame.image.load("mango sidebar.png")
mango_rect_sidebar = Mango_Sidebar.get_rect()


def colors():
    import tkinter as tk
    from tkinter import colorchooser
    root = tk.Tk()
    root.withdraw()
    try:
        color = colorchooser.askcolor(title="Mango Draw Color Picker")
        root.destroy()
        if color and color[1]:
            return color[1]
        return None
    except Exception:
        root.destroy()
        return None


Drawing_sound = pygame.mixer.Sound('pencil-29272.mp3')
Max_wordcount = 26
if not os.path.exists(Drawing_mango_folder):
    os.mkdir(Drawing_mango_folder)
while running:  # runs when the game starts
    mX, mY = pygame.mouse.get_pos()  # acquire x and y coordinates of the mouse and save them into mX and mY accordingly
    events = pygame.event.get()
    for event in events:  # if the game is "quit", set running to false to exit the game loop #variable for get event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos
                Snapshot()
            if pygame.mouse.get_pressed()[0] and 0 <= mX <= 230 and 9 <= mY <= 711 and Sidebar is True:
                canDraw = False

            else:
                canDraw = True
                Drawing_sound = pygame.mixer.Sound('pencil-29272.mp3')
        if event.type == pygame.MOUSEBUTTONUP:
            Drawing_sound.stop()
        if event.type == pygame.MOUSEMOTION:
            last_pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_o and questioning is False:  # Press 'O' to open file dialog
                file_path = filedialog.askopenfilename(
                    filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
                )
                if file_path:
                    try:
                        Uploaded_Image = pygame.image.load(file_path).convert_alpha()
                        uploaded_image = pygame.transform.scale(Uploaded_Image, (500, 500))
                        image_rect = uploaded_image.get_rect(center=(screen_width // 2, screen_height // 2))
                        Back_no = True
                    except pygame.error as e:
                        uploaded_image = None
                        image_rect = None
            # time.sleep(.025)
        else:
            undoFrameClicked = False
    textinp.update(events)
    textinput.update(events)  # make the text input actually work

    MAX_CHARS = 27

    # For save dialog
    if len(textinput.value) > MAX_CHARS:
        textinput.value = textinput.value[:MAX_CHARS]

    # For load dialog (if you use textinp elsewhere, but in your code it's textinput for save/load)
    if len(textinp.value) > MAX_CHARS:
        textinp.value = textinp.value[:MAX_CHARS]

    if 1130 <= mX <= 1260 and 345 <= mY <= 407 and not lastFrameClicked:
        if mango_marker_TF is False:  # checking ig mango_marker_TF(this is a boolean) is False
            mango_rect_d.x -= 25  # moves left 20 pixels
            lastFrameClicked = False
        mango_marker_TF = True  # sets true if you hover over the marker
    else:
        if mango_marker_TF:  # applies the last comment if you move of the marker. Checks if True
            mango_rect_d.x += 25
        mango_marker_TF = False
    if pygame.mouse.get_pressed()[0] and mango_marker_TF is True:
        Mouse_Cur = True
        Marker_2_mouse_vis = False
        Which_marker = True
        Which_marker2 = False
        Nww = False
        new_w = False
        lastFrameClicked = False

    if 1118 <= mX <= 1260 and 442 <= mY <= 509 and not lastFrameClicked:
        if Marker_2_TF is False:
            Marker_2_rect.x -= 25
            lastFrameClicked = False
            Marker_2_TF = True
    else:
        if Marker_2_TF:
            Marker_2_rect.x += 25
        Marker_2_TF = False

    if pygame.key.get_pressed()[  # if the key f is pressed the screen will be cleared as well as saved strokes
        pygame.K_f] and questioning is False:
        screen_canvas.fill((0, 0, 0, 0))
        screen_canvasUnder.fill((0, 0, 0, 0))
        screen_canvasUnderMore.fill((0, 0, 0, 0))
        screen_canvasUnderMoreMore.fill((0, 0, 0, 0))
        Image_upload = False
        mango_image = False
        Back_no = False
        pygame.display.flip()
        elements.clear()

    if uploaded_image and image_rect:
        screen.blit(uploaded_image, image_rect)
    else:
        font = pygame.font.Font(None, 36)
        text = font.render("Press 'O' to open an image", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    #   {FOR INCREASING BRUSH SIZE}

    if pygame.key.get_pressed()[
        pygame.K_1]:
        radius = 5
        brushSize = 1
    if pygame.key.get_pressed()[pygame.K_2]:
        radius = 10
        brushSize = 2
    if pygame.key.get_pressed()[pygame.K_3]:
        radius = 15
        brushSize = 3
    if pygame.key.get_pressed()[pygame.K_4]:
        radius = 20
        brushSize = 4
    if pygame.key.get_pressed()[pygame.K_5]:
        radius = 25
        brushSize = 5
    if pygame.key.get_pressed()[pygame.K_6]:
        radius = 35
        brushSize = 6
    if pygame.key.get_pressed()[pygame.K_7]:
        radius = 50
        brushSize = 7
    if pygame.key.get_pressed()[pygame.K_8]:
        radius = 75
        brushSize = 8
    if pygame.key.get_pressed()[pygame.K_9]:
        radius = 100
        brushSize = 9

    # ----------------------------------------------------
    if pygame.mouse.get_pressed()[0] and 1118 <= mX <= 1260 and 442 <= mY <= 509 and not lastFrameClicked:
        Mouse_CC = True
        new_w = False
        Which_marker = False
        Nww = True

    if Mouse_CC and pygame.mouse.get_pressed()[0]:
        if canDraw is True and 635 >= mY >= 85 and 35 <= mX <= 1231 and new_w is False and Which_marker is False:  # make sure you are drawing inside the border not on it.
            Color_for_M2 = random.choice(Colors_M2)
            if not lastFrameClicked:
                lastFrameClicked = True
                elements.append('START')
                Drawing_sound.play(loops=-1)
                if Button_1 is False and Button_2 is False and Button_3 is False:
                    pygame.draw.circle(screen_canvasUnder, Color_for_M2, (mX, mY), radius)
                    elements.append(('b1', Color_for_M2, (mX, mY), radius))
                if Button_1 is True:
                    pygame.draw.circle(screen_canvasUnder, Color_for_M2, (mX, mY), radius)
                    elements.append(('b1', Color_for_M2, (mX, mY), radius))
                if Button_2 is True:
                    pygame.draw.circle(screen_canvasUnderMore, Color_for_M2, (mX, mY), radius)
                    elements.append(('b2', Color_for_M2, (mX, mY), radius))
                if Button_3 is True:
                    pygame.draw.circle(screen_canvasUnderMoreMore, Color_for_M2, (mX, mY), radius)
                    elements.append(('b3', Color_for_M2, (mX, mY), radius))
            else:
                steps = max(abs(mX - last_pos[0]), abs(mY - last_pos[1]))
                if steps > 0:
                    dx = (mX - last_pos[0]) / steps
                    dy = (mY - last_pos[1]) / steps
                    for i in range(int(steps), 0, -1):
                        inter_x = last_pos[0] + dx * i
                        inter_y = last_pos[1] + dy * i
                        if Button_1 is False and Button_2 is False and Button_3 is False:
                            pygame.draw.circle(screen_canvasUnder, Color_for_M2, (int(inter_x), int(inter_y)), radius)
                            elements.append(('b1', Color_for_M2, (int(inter_x), int(inter_y)), radius))
                        if Button_1 is True:
                            pygame.draw.circle(screen_canvasUnder, Color_for_M2, (int(inter_x), int(inter_y)), radius)
                            elements.append(('b1', Color_for_M2, (int(inter_x), int(inter_y)), radius))
                        if Button_2 is True:
                            pygame.draw.circle(screen_canvasUnderMore, Color_for_M2, (int(inter_x), int(inter_y)),
                                               radius)
                            elements.append(('b2', Color_for_M2, (int(inter_x), int(inter_y)), radius))
                        if Button_3 is True:
                            pygame.draw.circle(screen_canvasUnderMoreMore, Color_for_M2, (int(inter_x), int(inter_y))
                                               , radius)
                            elements.append(('b3', Color_for_M2, (int(inter_x), int(inter_y)), radius))

    if Mouse_CC and pygame.mouse.get_pressed()[0]:
        if canDraw is True and 635 >= mY >= 85 and 35 <= mX <= 1231 and Nww is True and Which_marker2 is False and new_w is True:  # make sure you are drawing inside the border not on it.
            if not lastFrameClicked:
                lastFrameClicked = True
                elements.append('START')
                Drawing_sound.play(loops=-1)
                if Button_1 is False and Button_2 is False and Button_3 is False:
                    pygame.draw.circle(screen_canvasUnder, selectedColor, (mX, mY), radius, radius)
                    elements.append(('b1', selectedColor, (mX, mY), radius))
                if Button_1 is True:
                    pygame.draw.circle(screen_canvasUnder, selectedColor, (mX, mY), radius, radius)
                    elements.append(('b1', selectedColor, (mX, mY), radius))
                if Button_2 is True:
                    pygame.draw.circle(screen_canvasUnderMore, selectedColor, (mX, mY), radius, radius)
                    elements.append(('b2', selectedColor, (mX, mY), radius))
                if Button_3 is True:
                    pygame.draw.circle(screen_canvasUnderMoreMore, selectedColor, (mX, mY), radius, radius)
                    elements.append(('b3', selectedColor, (mX, mY), radius))
            else:
                steps = max(abs(mX - last_pos[0]), abs(mY - last_pos[1]))
                if steps > 0:
                    dx = (mX - last_pos[0]) / steps
                    dy = (mY - last_pos[1]) / steps
                    for i in range(int(steps), 0, -1):
                        inter_x = last_pos[0] + dx * i
                        inter_y = last_pos[1] + dy * i
                        if Button_1 is False and Button_2 is False and Button_3 is False:
                            pygame.draw.circle(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)), radius)
                            elements.append(('b1', selectedColor, (int(inter_x), int(inter_y)), radius))
                        if Button_1 is True:
                            pygame.draw.circle(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)), radius)
                            elements.append(('b1', selectedColor, (int(inter_x), int(inter_y)), radius))
                        if Button_2 is True:
                            pygame.draw.circle(screen_canvasUnderMore, selectedColor, (int(inter_x), int(inter_y)),
                                               radius)
                            elements.append(('b2', selectedColor, (int(inter_x), int(inter_y)), radius))
                        if Button_3 is True:
                            pygame.draw.circle(screen_canvasUnderMoreMore, selectedColor, (int(inter_x), int(inter_y))
                                               , radius)
                            elements.append(('b3', selectedColor, (int(inter_x), int(inter_y)), radius))

        elif not lastFrameClicked and pygame.mouse.get_pressed()[0]:
            if 253 < mX < 324 and 665 < mY < 722:
                new_w = True
                selectedColor = 'red'
            if 683 < mX < 751 and 665 < mY < 722:
                new_w = True
                selectedColor = 'orange'
            if 340 < mX < 409 and 665 < mY < 722:
                new_w = True
                selectedColor = 'yellow'
            if 515 < mX < 575 and 665 < mY < 722:
                new_w = True
                selectedColor = 'green'
            if 425 < mX < 495 and 665 < mY < 722:
                new_w = True
                selectedColor = 'blue'
            if 858 < mX < 918 and 665 < mY < 722:
                new_w = True
                selectedColor = 'white'
            if 950 < mX < 1004 and 665 < mY < 722:
                new_w = True
                selectedColor = 'black'
            if 600 < mX < 662 and 665 < mY < 722:
                screen_canvas.blit(ref, (400, 100))
            if 769 < mX < 839 and 665 < mY < 722:
                new_w = True
                selectedColor = 'purple'

            if pygame.mouse.get_pressed()[0] and 33 <= mX <= 107 and 33 <= mY <= 99:
                opening3 = False
                selectedColorTest = colors()
                if not selectedColorTest is None:
                    selectedColor = selectedColorTest
                textinp.value = ""
                questioning2 = False

    if lastFrameClicked is False and pygame.mouse.get_pressed()[0] and 1130 <= mX <= 1260 and 345 <= mY <= 407:
        Mouse_CC = True
        new_w = False
        Which_marker = True
        Which_marker2 = True
        Nww = False
    if Mouse_CC and pygame.mouse.get_pressed()[0]:
        pos_m = pygame.mouse.get_pos()
        if canDraw is True and 635 >= mY >= 85 and 35 <= mX <= 1231 and Nww is False and Which_marker is True:  # make sure you are drawing inside the border not on it.
            if new_pos:
                if not lastFrameClicked:  # checking if lastFrameClicked is False
                    elements.append("START")  # saying the start of a line
                    lastFrameClicked = True
                    Drawing_sound.play(loops=-1)
                if Button_1 is False and Button_2 is False and Button_3 is False:
                    pygame.draw.line(screen_canvasUnder, selectedColor, (mX, mY), pos_m, radius)
                    elements.append(("Line1", selectedColor, (mX, mY), pos_m, radius))
                if Button_1 is True:
                    pygame.draw.line(screen_canvasUnder, selectedColor, (mX, mY), pos_m, radius)
                    elements.append(("Line1", selectedColor, (mX, mY), pos_m, radius))
                if Button_2 is True:
                    pygame.draw.line(screen_canvasUnderMore, selectedColor, (mX, mY), pos_m, radius)
                    elements.append(("Line2", selectedColor, (mX, mY), pos_m, radius))
                if Button_3 is True:
                    pygame.draw.line(screen_canvasUnderMoreMore, selectedColor, (mX, mY), pos_m, radius)
                    elements.append(("Line3", selectedColor, (mX, mY), pos_m, radius))
            else:
                steps = max(abs(mX - last_pos[0]), abs(mY - last_pos[1]))
                if steps > 0:
                    dx = (mX - last_pos[0]) / steps
                    dy = (mY - last_pos[1]) / steps
                    for i in range(int(steps), 0, -1):
                        inter_x = last_pos[0] + dx * i
                        inter_y = last_pos[1] + dy * i
                        try:
                            if Button_1 is False and Button_2 is False and Button_3 is False:
                                pygame.draw.line(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)),
                                                 radius)
                                elements.append(('Line1', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_1 is True:
                                pygame.draw.line(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)),
                                                 radius)
                                elements.append(('Line1', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_2 is True:
                                pygame.draw.line(screen_canvasUnderMore, selectedColor, (int(inter_x), int(inter_y)),
                                                 radius)
                                elements.append(('Line2', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_3 is True:
                                pygame.draw.line(screen_canvasUnderMoreMore, selectedColor
                                                 , (int(inter_x), int(inter_y)), radius)
                                elements.append(('Line3', selectedColor, (int(inter_x), int(inter_y)), radius))
                        except TypeError:
                            pass
            # elements.append((selectedColor, (mX, mY), pos_m, radius))
            new_pos = pos_m
        elif not lastFrameClicked and pygame.mouse.get_pressed()[0]:
            if 260 < mX < 318 and 699 < mY < 734:  # Fixed
                new_w = True
                Which_marker2 = False
                selectedColor = 'red'
            if 686 < mX < 747 and 700 < mY < 732:  # Fixed
                new_w = True
                Which_marker2 = False
                selectedColor = 'orange'
            if 345 < mX < 404 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'yellow'
            if 515 < mX < 575 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'green'
            if 422 < mX < 485 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'blue'
            if 858 < mX < 918 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'white'
            if 950 < mX < 1004 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'black'
            if 600 < mX < 662 and 665 < mY < 722:
                screen_canvas.blit(ref, (400, 100))
            if 773 < mX < 831 and 665 < mY < 722:
                new_w = True
                Which_marker2 = False
                selectedColor = 'purple'

    if Mouse_CC is False:
        if pygame.mouse.get_pressed()[0]:
            if canDraw is True and 635 >= mY >= 85 and 35 <= mX <= 1231:  # make sure you are drawing inside the border not on it.
                if not lastFrameClicked:  # checking if lastFrameClicked is False
                    elements.append("START")  # saying the start of a line
                    lastFrameClicked = True
                    Drawing_sound.play(loops=-1)
                    if Button_1 is False and Button_2 is False and Button_3 is False:
                        pygame.draw.circle(screen_canvasUnder, selectedColor, (mX, mY), radius, radius)
                        elements.append(('b1', selectedColor, (mX, mY), radius))
                    if Button_1 is True:
                        pygame.draw.circle(screen_canvasUnder, selectedColor, (mX, mY), radius)
                        elements.append(('b1', selectedColor, (mX, mY), radius))
                    if Button_2 is True:
                        pygame.draw.circle(screen_canvasUnderMore, selectedColor, (mX, mY), radius)
                        elements.append(('b2', selectedColor, (mX, mY), radius))
                    if Button_3 is True:
                        pygame.draw.circle(screen_canvasUnderMoreMore, selectedColor, (mX, mY), radius)
                        elements.append(('b3', selectedColor, (mX, mY), radius))

                else:
                    steps = max(abs(mX - last_pos[0]), abs(mY - last_pos[1]))
                    if steps > 0:
                        dx = (mX - last_pos[0]) / steps
                        dy = (mY - last_pos[1]) / steps
                        for i in range(int(steps), 0, -1):
                            inter_x = last_pos[0] + dx * i
                            inter_y = last_pos[1] + dy * i
                            if Button_1 is False and Button_2 is False and Button_3 is False:
                                pygame.draw.circle(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)),
                                                   radius)
                                elements.append(('b1', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_1 is True:
                                pygame.draw.circle(screen_canvasUnder, selectedColor, (int(inter_x), int(inter_y)),
                                                   radius)
                                elements.append(('b1', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_2 is True:
                                pygame.draw.circle(screen_canvasUnderMore, selectedColor, (int(inter_x), int(inter_y)),
                                                   radius)
                                elements.append(('b2', selectedColor, (int(inter_x), int(inter_y)), radius))
                            if Button_3 is True:
                                pygame.draw.circle(screen_canvasUnderMoreMore, selectedColor
                                                   , (int(inter_x), int(inter_y)), radius)
                                elements.append(('b3', selectedColor, (int(inter_x), int(inter_y)), radius))
            elif not lastFrameClicked:
                if 260 < mX < 318 and 699 < mY < 734:  # fixed
                    selectedColor = 'red'
                if 686 < mX < 747 and 700 < mY < 732:  # Fixed
                    selectedColor = 'orange'
                if 345 < mX < 404 and 665 < mY < 722:
                    selectedColor = 'yellow'
                if 515 < mX < 575 and 665 < mY < 722:
                    selectedColor = 'green'
                if 422 < mX < 485 and 665 < mY < 722:
                    selectedColor = 'blue'
                if 772 < mX < 832 and 665 < mY < 722:
                    selectedColor = 'purple'
                if 858 < mX < 918 and 665 < mY < 722:
                    selectedColor = 'white'
                if 950 < mX < 1004 and 665 < mY < 722:
                    selectedColor = 'black'
                if 600 < mX < 662 and 665 < mY < 722:
                    screen_canvas.blit(ref, (400, 100))
                if 1061 < mX < 1128 and 665 < mY < 722:
                    selectedColor = 'white'

                if pygame.mouse.get_pressed()[0] and 33 <= mX <= 107 and 33 <= mY <= 99 and not lastFrameClicked:
                    opening3 = False
                    selectedColorTest = colors()
                    if not selectedColorTest is None:
                        selectedColor = selectedColorTest
                    textinp.value = ""
                    questioning2 = False

    if pygame.mouse.get_pressed()[0] == False and lastFrameClicked is True:
        lastFrameClicked = False

    if pygame.key.get_pressed()[pygame.K_e]:  # when the key e is pressed
        selectedColor = 'white'  # the eraser is selected

    if pygame.key.get_pressed()[pygame.K_z] and pygame.key.get_pressed()[
        pygame.K_LCTRL]:  # debugging: if key K is pressed, set screen to orange (no longer working?)
        if not undoFrameClicked:
            Back_no = False
            undoFrameClicked = True
            time.sleep(0.12)
            screen_canvas.fill((0, 0, 0, 0))
            screen_canvasUnder.fill((0, 0, 0, 0))
            screen_canvasUnderMore.fill((0, 0, 0, 0))
            screen_canvasUnderMoreMore.fill((0, 0, 0, 0))
            screen_canvas.blit(border, (0, 0))
            mango_image = False
            if len(elements) > 0:
                for i in range(len(elements) - 1, -1, -1):

                    if elements[i] == "START":
                        elements.pop(i)  # removes the 'START' from the list elements
                        if len(elements) < 2:
                            pass
                        break
                    elements.pop(i)
            for i in elements:
                if not i == "START":
                    if i[0] == 'Line1':
                        pygame.draw.line(screen_canvasUnder, i[1], i[2], i[3], i[4])
                    elif i[0] == 'Line2':
                        pygame.draw.line(screen_canvasUnderMore, i[1], i[2], i[3], i[4])
                    elif i[0] == 'Line3':
                        pygame.draw.line(screen_canvasUnderMoreMore, i[1], i[2], i[3], i[4])
                    elif i[0] == 'b1':
                        pygame.draw.circle(screen_canvasUnder, i[1], i[2], i[3])
                    elif i[0] == 'b2':
                        pygame.draw.circle(screen_canvasUnderMore, i[1], i[2], i[3])
                    elif i[0] == 'b3':
                        pygame.draw.circle(screen_canvasUnderMoreMore, i[1], i[2], i[3])
            # time.sleep(.025)
    else:
        undoFrameClicked = False

    # {SAVING YOUR DRAWING - .MANGO FORMAT}
    if pygame.mouse.get_pressed()[
        0] and 1045 <= mX <= 1115 and 9 <= mY <= 67 and opening is False and opening2 is False and not lastFrameClicked:
        Screen_saving.blit(saving_background, (330, 215))
        textinput.value = ""
        questioning = True
        opening = True
        Saving_bg = True

    # {QUICK SAVE AS PNG - RED CIRCLE BUTTON}
    if pygame.mouse.get_pressed()[0] and not lastFrameClicked:
        dist_from_circle_center = ((mX - 980) ** 2 + (mY - 38) ** 2) ** 0.5
        if dist_from_circle_center <= 20:
            lastFrameClicked = True

            # Surface to composite canvas drawing without UI elements
            export_surface = pygame.Surface((1260, 750), pygame.SRCALPHA)
            export_surface.fill((255, 255, 255))  # White background

            if Image_upload and uploaded_image and image_rect:
                export_surface.blit(uploaded_image, image_rect)
            export_surface.blit(screen_canvasUnder, (0, 0))
            export_surface.blit(screen_canvasUnderMore, (0, 0))
            export_surface.blit(screen_canvasUnderMoreMore, (0, 0))

            timestamp = int(time.time())
            png_filename = os.path.join(Drawing_mango_folder, f"drawing_{timestamp}.png")

            pygame.image.save(export_surface, png_filename)
            print(f"Drawing saved as PNG to: {png_filename}")

    if pygame.key.get_pressed()[pygame.K_RETURN] and opening is True:
        opening = False
        New_Name_File = textinput.value
        textinput.value = ""
        questioning = False
        Saving_bg = False
        Screen_saving.fill((0, 0, 0, 0))
        try:
            Drawing_mango_folder = 'MangoDrawings'
            NEW_FILE_DIR = os.path.join(Drawing_mango_folder, New_Name_File)
            with open(NEW_FILE_DIR + '.mango', 'w') as file:
                Info = pyperclip.copy(zlib.compress(str(elements).encode(
                    'utf-8')))  # Saves your brushstrokes/elements in your clipboard and compresses it into utf-8
                file.write(str(pyperclip.paste()))
                Info = pyperclip.copy(zlib.compress(str(elements).encode(
                    'utf-8')))  # Saves your brushstrokes/elements in your clipboard and compresses it into utf-8
                file.write(str(pyperclip.paste()))
        except FileExistsError:
            pass
    if pygame.key.get_pressed()[pygame.K_ESCAPE] and Saving_bg is True:
        questioning = False
        opening = False
        Screen_saving.fill((0, 0, 0, 0))
    # {LOADING YOUR DRAWING}
    if 1162 <= mX <= 1208 and 8 <= mY <= 67 and pygame.mouse.get_pressed()[
        0] and opening2 is False and opening is False and not lastFrameClicked:
        Screen_Loading.blit(Loading_background, (330, 215))
        textinput.value = ""
        questioning = True
        opening2 = True
        Loading_bg = True
    if pygame.key.get_pressed()[pygame.K_RETURN] and opening2 == True:
        opening2 = False
        What_file = textinput.value
        textinput.value = ""
        questioning = False
        Loading_bg = False
        Screen_Loading.fill((0, 0, 0, 0))
        Drawing_mango_folder = 'MangoDrawings'
        NEW_FILE_DIR = os.path.join(Drawing_mango_folder, What_file)
        try:
            with open(NEW_FILE_DIR + '.mango', 'r') as file_b:
                content = file_b.read()
                content = str(zlib.decompress(ast.literal_eval(content)).decode('utf-8'))
                tempValue2 = ast.literal_eval(content)
                if type(tempValue2) == list:
                    elements = tempValue2
                    for i in tempValue2:
                        if not i == "START":
                            if i[0] == 'Line1':
                                pygame.draw.line(screen_canvasUnder, i[1], i[2], i[3], i[4])
                            elif i[0] == 'Line2':
                                pygame.draw.line(screen_canvasUnderMore, i[1], i[2], i[3], i[4])
                            elif i[0] == 'Line3':
                                pygame.draw.line(screen_canvasUnderMoreMore, i[1], i[2], i[3], i[4])
                            if i[0] == 'b1':
                                pygame.draw.circle(screen_canvasUnder, i[1], i[2], i[3])
                            if i[0] == 'b2':
                                pygame.draw.circle(screen_canvasUnderMore, i[1], i[2], i[3])
                            if i[0] == 'b3':
                                pygame.draw.circle(screen_canvasUnderMoreMore, i[1], i[2], i[3])
        except FileNotFoundError:
            Loading_bg = True
            questioning = True
            opening2 = True
            Screen_Loading.blit(Loading_background, (330, 215))
            textinput.value = ""

    if pygame.key.get_pressed()[pygame.K_ESCAPE] and Loading_bg is True:
        questioning = False
        opening2 = False
        Screen_Loading.fill((0, 0, 0, 0))
    if pygame.key.get_pressed()[pygame.K_z] and pygame.key.get_pressed()[pygame.K_LSHIFT] and not \
            pygame.key.get_pressed()[
                pygame.K_LCTRL]:  # debugging: if key K is pressed, set screen to orange (no longer working?)
        screen_canvas.fill((0, 0, 0, 0))
        screen_canvas.blit(border, (0, 0))
        # interaction between mango marker and drawing
    mango_cursor_rect.center = pygame.mouse.get_pos()
    mango_cursor_rect.x = mango_cursor_rect.x + 120

    screen.fill('white')

    if 600 < mX < 662 and 665 < mY < 722 and pygame.mouse.get_pressed()[0]:
        mango_image = True
    if mango_image:
        screen_canvas.blit(ref, (400, 100))

    if uploaded_image and image_rect and Back_no is True:
        pass
        Image_upload = True
    if Back_no is False:
        Image_upload = False
    if Image_upload:
        screen_canvasUnder.blit(uploaded_image, image_rect)
    if pygame.mouse.get_pressed()[0] and 0 <= mX <= 215 and 9 <= mY <= 711 and Sidebar is True:
        time.sleep(0.1)
        canDraw = False
    else:
        canDraw = True
    screen_canvas.blit(border, (0, 0))
    screen.blit(screen_canvasUnder, (0, 0))
    screen.blit(screen_canvasUnderMore, (0, 0))
    screen.blit(screen_canvasUnderMoreMore, (0, 0))
    screen.blit(screen_canvas, (0, 0))
    screen.blit(Screen_saving, (0, 0))
    screen.blit(Screen_Loading, (0, 0))

    # Render Red Circle PNG Save Button on top UI
    pygame.draw.circle(screen, (255, 0, 0), (980, 38), 20)

    if Which_marker is False:
        screen.blit(Mango_Icon, (50.6, 687.7))
    if Which_marker:
        pygame.draw.circle(screen, selectedColor, (int(75.6), int(712.7)), 17)
    if Which_marker or new_w is True:
        pygame.draw.circle(screen, selectedColor, (int(75.6), int(712.7)), 17)
    if questioning:
        screen.blit(textinput.surface, (380, 392))  # box
    if questioning2:
        screen.blit(textinp.surface, (100, 300))
    if pygame.mouse.get_pressed()[0] and 0 <= mX <= 45 and 309 <= mY <= 439 and not lastFrameClicked:
        Sidebar = True
    if Sidebar:
        screen.blit(Mango_Sidebar, mango_rect_sidebar)
    if pygame.mouse.get_pressed()[0] and 140 <= mX <= 199 and 286 < mY <= 415 and Sidebar is True:
        Sidebar = False
    screen.blit(Marker_2, Marker_2_rect)
    screen.blit(mango_marker, mango_rect_d)

    if pygame.mouse.get_pressed()[0] and 1130 <= mX <= 1260 and 345 <= mY <= 407 and not lastFrameClicked:
        Mouse_Cur = True
        Marker_2_mouse_vis = False
        Which_marker = True
        Which_marker2 = False
        Nww = False
        new_w = False
    if Mouse_Cur:
        if pygame.mouse.get_pressed()[0] and 635 >= mY >= 85 and 35 <= mX <= 1231 and lastFrameClicked:
            screen.blit(mango_cursor, mango_cursor_rect)
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)

    if pygame.mouse.get_pressed()[0] and 1118 <= mX <= 1260 and 442 <= mY <= 509 and lastFrameClicked:
        Marker_2_mouse_vis = True
        Mouse_Cur = False
    if Marker_2_mouse_vis:
        if pygame.mouse.get_pressed()[0] and 635 >= mY >= 85 and 35 <= mX <= 1231 and lastFrameClicked:
            screen.blit(Mouse_marker_2, (mX - 620, mY - 390))
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
    if 681 <= mX <= 736 and 13 <= mY <= 61 and not lastFrameClicked and pygame.mouse.get_pressed()[0]:
        Button_1 = True
        Button_2 = False
        Button_3 = False
    if pygame.key.get_pressed()[pygame.K_c]:
        Button_1 = False
    if 779 <= mX <= 828 and 13 <= mY <= 61 and not lastFrameClicked and pygame.mouse.get_pressed()[0]:
        Button_2 = True
        Button_1 = False
        Button_3 = False
    if 869 <= mX <= 921 and 13 <= mY <= 61 and not lastFrameClicked and pygame.mouse.get_pressed()[0]:
        Button_3 = True
        Button_1 = False
        Button_2 = False

    text = font.render("Current Layer: " + str(1), True, (59, 31, 4))
    if Button_1:
        text = font.render("Current Layer: " + str(1), True, (59, 31, 4))
    if Button_2:
        text = font.render("Current Layer: " + str(2), True, (59, 31, 4))
    elif Button_3:
        text = font.render("Current Layer: " + str(3), True, (59, 31, 4))
    text_rect = text.get_rect(center=(550, 40))
    screen.blit(text, text_rect)

    if 8 < mX < 125 and 137 < mY < 249 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 75
        brushSize = 8
    if 22 < mX < 110 and 278 < mY < 363 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 50
        brushSize = 7
    if 36 < mX < 102 and 380 < mY < 441 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 35
        brushSize = 6
    if 40 < mX < 95 and 459 < mY < 514 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 25
        brushSize = 5
    if 45 < mX < 90 and 530 < mY < 572 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 20
        brushSize = 4
    if 55 < mX < 81 and 594 < mY < 618 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 15
        brushSize = 3
    if 60 < mX < 77 and 630 < mY < 658 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 10
        brushSize = 2
    if 60 < mX < 77 and 665 < mY < 682 and pygame.mouse.get_pressed()[0] and Sidebar:
        radius = 5
        brushSize = 1

    clock.tick(1000)
    pygame.display.flip()