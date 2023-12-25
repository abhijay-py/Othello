#TUPLE OPERATIONS
ADD_TUPLE = 0
SUB_TUPLE = 1
MULT_TUPLE = 2
ADD_DIGIT = 3
SUB_DIGIT = 4
MULT_DIGIT = 5

#STATES
MENU_STATE = 0
CREATE_GAME_STATE = 1
GAME_STATE = 2
MENU_MIDGAME_STATE = 3
INFO_STATE = 4
CREDITS_STATE = 5
QUIT_STATE = 6

#COLORS
BOARD_GREEN = (29, 171, 72)
LIGHT_BOARD_GREEN = (31, 184, 130)
BACKGROUND_BLUE = (91, 132, 199)
BACKGROUND_GREEN = (113, 168, 145)
BORDER_RED = (120, 16, 28)
TEXT_BOX_ORANGE = (189, 154, 42)
TEXT_BOX_GREEN = (63, 153, 79)
TEXT_BOX_YELLOW = (191, 181, 63)

#TIMING
TIME_IDLE_QUIT = 300 #Seconds
FPS = 100 #Frames Per Second

#OTHER
ANTIALIAS_SETTING = True



#DIMENSIONS
#Screen
SCREEN_DIMENSIONS = (1280, 720)

#Board
BOARD_EDGE_RADIUS = 7
BOARD_DIMENSIONS = (648, 648)
BOARD_START = (316, 36)
BORDER_THICKNESS = 5
LINE_THICKNESS = 2

#Game Text
TURN_LOCATION = (40, 20)
BLACK_SCORE_LOCATION = (100, 625)
WHITE_SCORE_LOCATION = (1075, 625)

#Pieces
PIECE_OFFSET = 10
PIECE_BORDER_THICKNESS = 2
PIECE_RADIUS = (BOARD_DIMENSIONS[0] / 16) - PIECE_OFFSET
FIRST_PIECE = (BOARD_START[0] + PIECE_RADIUS + PIECE_OFFSET, BOARD_START[1] + PIECE_RADIUS + PIECE_OFFSET)
NEXT_PIECE_OFFSET = PIECE_OFFSET * 2 + PIECE_RADIUS  * 2

#Menu Texts
TEXT_BOX_OFFSET = (10, 10)
TITLE_BORDER = BORDER_THICKNESS
TEXT_BOX_CORNER = BOARD_EDGE_RADIUS
OPTION_BORDER = 2
NEXT_BOX_OFFSET_MM = 125
NEXT_BOX_OFFSET = 100
TEXT_OFFSET = 50


#Specific Text Detail
MENU_TITLE_LOCATION_MM = (SCREEN_DIMENSIONS[0]/2 - 180, SCREEN_DIMENSIONS[1] * .1)
MIDMENU_TITLE_BOX = (370, 85)
MENU_TITLE_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 108, SCREEN_DIMENSIONS[1] * .1)
MENU_TITLE_BOX = (255, 85)
RG_BOX = (225, 65)
RG_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 105, SCREEN_DIMENSIONS[1] * .1 + 150)
MIDMENU_BOX = (225, 65)
MIDMENU_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 105, SCREEN_DIMENSIONS[1] * .1 + 150 + NEXT_BOX_OFFSET_MM)
QUIT_BOX = (80, 65)
MM_QUIT_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 30, SCREEN_DIMENSIONS[1] * .1 + 150 + 2* NEXT_BOX_OFFSET_MM)

NG_BOX = (185, 65)
NG_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 80, SCREEN_DIMENSIONS[1] * .1 + 150)
INFO_BOX = (188, 65)
INFO_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 80, SCREEN_DIMENSIONS[1] * .1 + 150 + NEXT_BOX_OFFSET)
CRED_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 50, SCREEN_DIMENSIONS[1] * .1 + 150 + 2*NEXT_BOX_OFFSET)
CRED_BOX = (125, 65)
QUIT_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 30, SCREEN_DIMENSIONS[1] * .1 + 150 + 3*NEXT_BOX_OFFSET)

INFO_TITLE_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 123, SCREEN_DIMENSIONS[1] * .1)
INFO_TITLE_BOX = (265, 85)
INFO_TEXT_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 273, SCREEN_DIMENSIONS[1] * .1 + 125)

BACK_I_LOC = (SCREEN_DIMENSIONS[0]/2 - 30, SCREEN_DIMENSIONS[1] * .1 + 550)
BACK_BOX = (95, 65)

CRED_TITLE_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 68, SCREEN_DIMENSIONS[1] * .1)
CRED_TITLE_BOX = (170, 85)
CRED_TEXT_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 213, SCREEN_DIMENSIONS[1] * .1 + 125)
BACK_C_LOC = (SCREEN_DIMENSIONS[0]/2 - 30, 350)

CG_TITLE_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 183, SCREEN_DIMENSIONS[1] * .1)
CG_TITLE_BOX = (440, 85)

DIFF_S_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 100, SCREEN_DIMENSIONS[1] * .1 + 100)
COLOR_S_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 75, SCREEN_DIMENSIONS[1] * .1 + 300)
PVP_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 430, SCREEN_DIMENSIONS[1] * .1 + 200)
PVP_BOX = (125, 60)
EASY_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 230, SCREEN_DIMENSIONS[1] * .1 + 200)
EASY_BOX = (100, 60)
MEDIUM_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 40, SCREEN_DIMENSIONS[1] * .1 + 200)
MEDIUM_BOX = (150, 60)
HARD_LOCATION = (SCREEN_DIMENSIONS[0]/2 + 200, SCREEN_DIMENSIONS[1] * .1 + 200)
HARD_BOX = (100, 60)
EXPERT_LOCATION = (SCREEN_DIMENSIONS[0]/2 + 400, SCREEN_DIMENSIONS[1] * .1 + 200)
EXPERT_BOX = (125, 60)
BLACK_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 100, SCREEN_DIMENSIONS[1] * .1 + 375)
BLACK_BOX = (105, 60)
WHITE_LOCATION = (SCREEN_DIMENSIONS[0]/2 + 65, SCREEN_DIMENSIONS[1] * .1 + 375)
WHITE_BOX = (105, 60)
START_LOCATION = (SCREEN_DIMENSIONS[0]/2 - 90, SCREEN_DIMENSIONS[1] * .1 + 500)
START_BOX = (90, 60)
BACK_CG_LOC = (SCREEN_DIMENSIONS[0]/2 + 70, SCREEN_DIMENSIONS[1] * .1 + 500)
BACK_CG_BOX = (90, 60)
