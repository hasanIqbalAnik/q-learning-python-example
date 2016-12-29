import sys

from pygame.locals import *
from utils import *

FPS = 20  # frames per second setting
fpsClock = pg.time.Clock()

pg.init()  # pygame initialization

window = pg.display.set_mode((windowWidth, windowHeight))  # width, height
pg.display.set_caption('Catch the ball!')

rct = pg.Rect(rctLeft, rctTop, rctWidth, rctHeight)  # Rect(left, top, width, height)

action = 1  # 0 means stay, 1 means left, 2 means right

score = 0
missed = 0
reward = 0
font = pg.font.Font(None, 30)

# set learning rate
lr = .85
y = .99

i = 0

while True:
    for event in pg.event.get():
        if event.type == QUIT:  # for the quitting button on the window
            pg.quit()
            sys.exit()

    window.fill(BLACK)  # window background

    # at this position, the rectangle should be here. else loses
    if crclCentreY >= windowHeight - rctHeight - crclRadius:  # check if the rectangle is under the circle or not
        reward = calculate_score(rct, Circle(crclCentreX, crclCentreY))  # +1 or -1
        crclCentreX = circle_falling(crclRadius)  #
        crclCentreY = 50
    else:
        reward = 0  # no reward if the ball wasn't missed
        crclCentreY += crclYStepFalling  # let the circle fall freely

    s = State(rct, Circle(crclCentreX, crclCentreY))
    act = get_best_action(s)  # get the best action so far in this state
    r0 = calculate_score(s.rect, s.circle)  # get the immediate reward of this step
    s1 = new_state_after_action(s, act)  # new state after taking the best action
    # build the Q table, indexed by (state, action) pair
    Q[state_to_number(s), act] += lr * (r0 + y * np.max(Q[state_to_number(s1), :]) - Q[state_to_number(s), act])

    rct = new_rect_after_action(s.rect, act)  # new position of the rectangle
    crclCentreX = s.circle.circleX  # put the ball where it originally was before the experiment
    crclCentreY = s.circle.circleY

    pg.draw.circle(window, RED, (crclCentreX, crclCentreY),
                   crclRadius)  # circle(Surface, color, pos(x, y), radius, width=0)
    pg.draw.rect(window, GREEN, rct)  # rect(Surface, color, Rect, width=0)

    if reward == 1:  # got it!
        score += reward  # add the reward to the total score
    elif reward == -1:  # missed
        missed += reward  # add the reward to the missed count

    text = font.render('score: ' + str(score), True, (238, 58, 140))  # update the score on the screen
    text1 = font.render('missed: ' + str(missed), True, (238, 58, 140))  # update the score on the screen
    window.blit(text, (windowWidth - 120, 10))  # render score
    window.blit(text1, (windowWidth - 280, 10))  # render missed

    pg.display.update()  # update display
    fpsClock.tick(FPS)
    if i == 10000:  # stopping condition
        break
    else:
        i += 1
