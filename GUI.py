import pygame
import fifo_code
import lru_code
import optimal_code


# Initialize the pygame
pygame.init()
clock = pygame.time.Clock()

# Creating the screen
win = pygame.display.set_mode((1200, 800))

# Color
white = (255, 255, 255)
black = (0, 0, 0)
color_active = white
color_passive = pygame.Color("gray15")

# Title and Icon
pygame.display.set_caption("question 3")
icon = pygame.image.load("molecule.png")
pygame.display.set_icon(icon)

"--------------------No of frames--------------------------"
# Text - Input no. of frames
nframes = pygame.font.Font(None, 25)
text_nframes = "Enter no. of frames :"

# Input box - no. of frames
nframes_font = pygame.font.Font(None, 25)
ip_nframes = ''
input_rect_n = pygame.Rect(225, 45, 80, 25)
color_n = color_passive
active_n = False
"----------------------------------------------------------"

"-------------------Values - String------------------------"
# Text - Input Data
data = pygame.font.Font(None, 25)
text_data = "Enter data (space separated) :"

# Input box - Data
data_font = pygame.font.Font(None, 25)
ip_data = ''
input_rect_data = pygame.Rect(305, 75, 80, 25)
color_data = color_passive
active_data = False
"----------------------------------------------------------"

"-------------------------BUTTONS--------------------------"
button = pygame.font.Font(None, 25)
input_rect_but1 = pygame.Rect(710, 30, 60, 30)
input_rect_but2 = pygame.Rect(800, 30, 200, 30)
input_rect_but3 = pygame.Rect(1030, 30, 80, 30)
txt_but1 = "RUN"
txt_but2 = "Run with default Data"
txt_but3 = "RESET"

default_frames = 3
default_data = "1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 2 3 6"

click_but1 = False
click_but3 = False
click_but2 = False
"----------------------------------------------------------"

"--------------FIFO, LRU, and OPTIMAL text-----------------"
# Text - FIFO
fifo = pygame.font.Font(None, 40)
text_fifo = "First in First Out"

# Text - LRU
lru = pygame.font.Font(None, 40)
text_lru = "Last Recently Used"

# Text - OPTIMAL
optimal = pygame.font.Font(None, 40)
text_optimal = "Optimal"
"----------------------------------------------------------"

"----------------Hit, Miss and Memory Text-----------------"
# Text - Memory
memory = pygame.font.Font(None, 30)
text_mem = "CACHE MEMORY :"

# Text - HIT
hit = pygame.font.Font(None, 25)
text_hit_fifo = "Total Hits    =    "
text_hit_lru = "Total Hits    =    "
text_hit_optimal = "Total Hits    =    "

# Text - MISS
miss = pygame.font.Font(None, 25)
text_miss_fifo = "Total Misses    =    "
text_miss_lru = "Total Misses    =    "
text_miss_optimal = "Total Misses    =    "

# Text - HIT Ratio
ratio = pygame.font.Font(None, 25)
text_ratio_fifo = "Hit Ratio    =    "
text_ratio_lru = "Hit Ratio    =    "
text_ratio_optimal = "Hit Ratio    =    "

x = 1
"----------------------------------------------------------"

"---------------------Table Contents-----------------------"
head_frames = pygame.font.Font(None, 25)
text_frames = "Frames"

head_val = pygame.font.Font(None, 25)
text_val = "Value Stored"
"----------------------------------------------------------"


run = True
while run:

    # BG Fill
    win.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect_n.collidepoint(event.pos):
                active_n = True
            else:
                active_n = False

            if input_rect_data.collidepoint(event.pos):
                active_data = True
            else:
                active_data = False

            if input_rect_but1.collidepoint(event.pos):
                click_but1 = True

            if input_rect_but2.collidepoint(event.pos):
                click_but2 = True

            if input_rect_but3.collidepoint(event.pos):
                click_but2 = False
                click_but1 = False
                click_but3 = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                active_data = False
                active_n = False

            if active_n:
                if event.key == pygame.K_BACKSPACE:
                    ip_nframes = ip_nframes[:-1]
                else:
                    ip_nframes += event.unicode

            if active_data:
                if event.key == pygame.K_BACKSPACE:
                    ip_data = ip_data[:-1]
                else:
                    ip_data += event.unicode

    "------------------------Border----------------------------"
    pygame.draw.aaline(win, white, (0, 10), (1200, 10))
    pygame.draw.aaline(win, white, (10, 0), (10, 800))
    pygame.draw.aaline(win, white, (0, 790), (1200, 790))
    pygame.draw.aaline(win, white, (1190, 0), (1190, 800))
    "----------------------------------------------------------"

    "--------------------No of frames--------------------------"
    # Blit Text - Input no. of frames
    txtsurf_nframes = nframes.render(text_nframes, True, (white))
    win.blit(txtsurf_nframes, (50, 50))

    # Blit Input box - no. of frames
    if active_n:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(win, color, input_rect_n, 3)
    txtsurf_ipn = nframes_font.render(ip_nframes, True, (white))
    win.blit(txtsurf_ipn, (input_rect_n.x + 5, input_rect_n.y + 5))
    input_rect_n.w = max(40, txtsurf_ipn.get_width() + 10)
    "----------------------------------------------------------"

    "-------------------Values - String------------------------"
    # Blit Text - DATA
    txtsurf_data = data.render(text_data, True, (white))
    win.blit(txtsurf_data, (50, 80))

    # Blit Input box - DATA
    if active_data:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(win, color, input_rect_data, 3)
    txtsurf_ipdata = data_font.render(ip_data, True, (white))
    win.blit(txtsurf_ipdata, (input_rect_data.x + 5, input_rect_data.y + 5))
    input_rect_data.w = max(40, txtsurf_ipdata.get_width() + 10)
    "----------------------------------------------------------"

    "-------------------------BUTTONS--------------------------"
    mouse = pygame.mouse.get_pos()

    if 710 + 60 > mouse[0] > 710 and 30 + 30 > mouse[1] > 30:
        pygame.draw.rect(win, white, (710, 30, 60, 30))
        txtsurf_but1 = button.render(txt_but1, True, (black))
        win.blit(txtsurf_but1, (720, 35))
    else:
        pygame.draw.rect(win, (255, 0, 0), (710, 30, 60, 30))
        txtsurf_but1 = button.render(txt_but1, True, (white))
        win.blit(txtsurf_but1, (720, 35))

    if 800 + 200 > mouse[0] > 800 and 30 + 30 > mouse[1] > 30:
        pygame.draw.rect(win, white, (800, 30, 200, 30))
        txtsurf_but2 = button.render(txt_but2, True, (black))
        win.blit(txtsurf_but2, (810, 35))
    else:
        pygame.draw.rect(win, (255, 0, 0), (800, 30, 200, 30))
        txtsurf_but2 = button.render(txt_but2, True, (white))
        win.blit(txtsurf_but2, (810, 35))

    if 1030 + 80 > mouse[0] > 1030 and 30 + 30 > mouse[1] > 30:
        pygame.draw.rect(win, white, (1030, 30, 80, 30))
        txtsurf_but3 = button.render(txt_but3, True, (black))
        win.blit(txtsurf_but3, (1040, 35))
    else:
        pygame.draw.rect(win, (255, 0, 0), (1030, 30, 80, 30))
        txtsurf_but3 = button.render(txt_but3, True, (white))
        win.blit(txtsurf_but3, (1040, 35))
    "----------------------------------------------------------"

    "--------------FIFO, LRU, and OPTIMAL text-----------------"
    # Partitions
    pygame.draw.aaline(win, white, (0, 150), (1200, 150))

    pygame.draw.aaline(win, white, (400, 150), (400, 800))
    pygame.draw.aaline(win, white, (800, 150), (800, 800))

    # Blit Text - FIFO
    txtsurf_fifo = fifo.render(text_fifo, True, (white))
    win.blit(txtsurf_fifo, (80, 180))

    # Blit Text - LRU
    txtsurf_lru = lru.render(text_lru, True, (white))
    win.blit(txtsurf_lru, (470, 180))

    # Blit Text - Optimal
    txtsurf_optimal = optimal.render(text_optimal, True, (white))
    win.blit(txtsurf_optimal, (950, 180))
    "----------------------------------------------------------"

    "-------------------MAIN BODY------------------------------"
    if click_but3:
        x = 0
        click_but3 = False
        ip_data = ''
        ip_nframes = ''

    if click_but1 or click_but2:

        "--------------------------Call Solutions--------------------------------"
        if click_but1:
            frames = int(ip_nframes)

            hit_fifo, miss_fifo, memory_fifo, hit_ratio_fifo = fifo_code.fifo_c(ip_data, frames)
            hit_lru, miss_lru, memory_lru, hit_ratio_lru = lru_code.lru_c(ip_data, frames)
            hit_optimal, miss_optimal, memory_optimal, hit_ratio_optimal = optimal_code.optimal_c(ip_data, frames)

        else:
            frames = default_frames
            hit_fifo, miss_fifo, memory_fifo, hit_ratio_fifo = fifo_code.fifo_c(default_data, frames)
            hit_lru, miss_lru, memory_lru, hit_ratio_lru = lru_code.lru_c(default_data, frames)
            hit_optimal, miss_optimal, memory_optimal, hit_ratio_optimal = optimal_code.optimal_c(default_data, frames)
        "------------------------------------------------------------------------"

        "----------------------------Update Values-------------------------------"
        if x == 1:
            text_hit_fifo += str(hit_fifo)
            text_hit_lru += str(hit_lru)
            text_hit_optimal += str(hit_optimal)

            text_miss_fifo += str(miss_fifo)
            text_miss_lru += str(miss_lru)
            text_miss_optimal += str(miss_optimal)

            text_ratio_fifo += str(hit_ratio_fifo)
            text_ratio_lru += str(hit_ratio_lru)
            text_ratio_optimal += str(hit_ratio_optimal)
            x = 0
        "------------------------------------------------------------------------"

        "--------------------------Cache Memory Table----------------------------"
        y = 300
        txtsurf_frames = head_frames.render(text_frames, True, black)
        txtsurf_val = head_val.render(text_val, True, black)


        pygame.draw.rect(win, white, (40, 290, 320, 35 + frames*35))
        pygame.draw.line(win, black, (150, 290), (150, y + (35+frames*35)))
        win.blit(txtsurf_val, (200, 300))
        win.blit(txtsurf_frames, (60, 300))

        pygame.draw.rect(win, white, (440, 290, 320, 35 + frames*35))
        pygame.draw.aaline(win, black, (550, 290), (550, y + (35+frames*35)))
        win.blit(txtsurf_val, (600, 300))
        win.blit(txtsurf_frames, (460, 300))

        pygame.draw.rect(win, white, (840, 290, 320, 35 + frames*35))
        pygame.draw.aaline(win, black, (950, 150), (950, y + (35+frames*35)))
        win.blit(txtsurf_val, (1000, 300))
        win.blit(txtsurf_frames, (860, 300))

        for i in range(frames):
            y += 35
            txtsurf = head_frames.render(str(i), True, (black))
            win.blit(txtsurf, (85, y))
            txtsurf = head_frames.render(str(i), True, (black))
            win.blit(txtsurf, (485, y))
            txtsurf = head_frames.render(str(i), True, (black))
            win.blit(txtsurf, (885, y))

        y = 300

        for i in range(len(memory_fifo)):
            y += 35
            txtsurf = head_val.render(str(memory_fifo[i]), True, (black))
            win.blit(txtsurf, (250, y))

        y = 300
        for i in range(len(memory_lru)):
            y += 35
            txtsurf = head_val.render(str(memory_lru[i]), True, (black))
            win.blit(txtsurf, (650, y))

        y = 300
        for i in range(len(memory_optimal)):
            y+=35
            txtsurf = head_val.render(str(memory_optimal[i]), True, (black))
            win.blit(txtsurf, (1050, y))
        "------------------------------------------------------------------------"

        "---------------------------Display all texts----------------------------"
        # Blit Text - Optimal
        txtsurf_mem = memory.render(text_mem, True, (white))
        win.blit(txtsurf_mem, (20, 250))
        win.blit(txtsurf_mem, (420, 250))
        win.blit(txtsurf_mem, (820, 250))

        txtsurf_hit_fifo = hit.render(text_hit_fifo, True, (white))
        win.blit(txtsurf_hit_fifo, (20, 25 + (290 + 35 + frames*35)))

        txtsurf_hit_lru = hit.render(text_hit_lru, True, (white))
        win.blit(txtsurf_hit_lru, (420, 25 + (290 + 35 + frames*35)))

        txtsurf_hit_optimal = hit.render(text_hit_optimal, True, (white))
        win.blit(txtsurf_hit_optimal, (820, 25 + (290 + 35 + frames*35)))

        txtsurf_miss_fifo = miss.render(text_miss_fifo, True, (white))
        win.blit(txtsurf_miss_fifo, (20, 50 + (290 + 35 + frames*35)))

        txtsurf_miss_lru = miss.render(text_miss_lru, True, (white))
        win.blit(txtsurf_miss_lru, (420, 50 + (290 + 35 + frames*35)))

        txtsurf_miss_optimal = miss.render(text_miss_optimal, True, (white))
        win.blit(txtsurf_miss_optimal, (820, 50 + (290 + 35 + frames*35)))

        txtsurf_ratio_fifo = ratio.render(text_ratio_fifo, True, (white))
        win.blit(txtsurf_ratio_fifo, (20, 75 + (290 + 35 + frames*35)))

        txtsurf_ratio_lru = ratio.render(text_ratio_lru, True, (white))
        win.blit(txtsurf_ratio_lru, (420, 75 + (290 + 35 + frames*35)))

        txtsurf_ratio_optimal = ratio.render(text_ratio_optimal, True, (white))
        win.blit(txtsurf_ratio_optimal, (820, 75 + (290 + 35 + frames*35)))
        "------------------------------------------------------------------------"

    "----------------------------------------------------------"

    pygame.display.update()
    clock.tick(30)

print(ip_data, ip_nframes)
# pygame.quit()
