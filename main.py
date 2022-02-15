
import cv2 as cv
import numpy as np
import pyautogui

cv.namedWindow("result");
cv.moveWindow("result", 0, 500);

img_dino = cv.imread('data/dino.png', cv.IMREAD_COLOR)
img_wall = cv.imread('data/wall.png', cv.IMREAD_COLOR)
img_bird = cv.imread('data/bird.png', cv.IMREAD_COLOR)

dino_h, dino_w = img_dino.shape[:2]
wall_h, wall_w = img_wall.shape[:2]
bird_h, bird_w = img_bird.shape[:2]

while 1:
    pic = pyautogui.screenshot(region=(0, 0,1280, 720))
    img_frame = np.array(pic)
    img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)
    meth = 'cv.TM_CCOEFF'
    method = eval(meth)

    res_dino = cv.matchTemplate(img_dino, img_frame, method)
    res_wall = cv.matchTemplate(img_wall, img_frame, method)
    #res_bird = cv.matchTemplate(img_bird, img_frame, method)

    dino_min_val, dino_max_val, dino_min_loc, dino_max_loc = cv.minMaxLoc(res_dino)
    wall_min_val, wall_max_val, wall_min_loc, wall_max_loc = cv.minMaxLoc(res_wall)
    #bird_min_val, bird_max_val, bird_min_loc, bird_max_loc = cv.minMaxLoc(res_bird)

    dino_top_left = dino_max_loc
    dino_bottom_right = (dino_top_left[0] + dino_w, dino_top_left[1] + dino_h)
    wall_top_left = wall_max_loc
    wall_bottom_right = (wall_top_left[0] + wall_w, wall_top_left[1] + wall_h)
    #bird_top_left = bird_max_loc
    #bird_bottom_right = (bird_top_left[0] + bird_w, bird_top_left[1] + bird_h)

    cv.rectangle(img_frame, dino_top_left, dino_bottom_right, (0, 255, 0), 2)
    cv.rectangle(img_frame, wall_top_left, wall_bottom_right, (255, 0, 0), 2)
    #cv.rectangle(img_frame, bird_top_left, bird_bottom_right, (0, 0, 255), 2)

    cv.imshow('result', img_frame)

    dino_center = (dino_top_left[0] + dino_bottom_right[0]) // 2
    wall_center = (wall_top_left[0] + wall_bottom_right[0]) // 2
    #bird_center = (bird_top_left[0] + bird_bottom_right[0]) // 2

    if wall_center<dino_center+20:
        # pyautogui.press('space',presses=1)
        print("press SpaceBar")
    # if bird_center<dino_center+20:
    #     # pyautogui.press('down',presses=1)
    #     print("press Down")


    key = cv.waitKey(1)
    if key == 27:
        break