import numpy as np

windowWidth = 800
windowHeight = 400

# setup colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# specify circle properties
crclCentreX = 400
crclCentreY = 50
crclRadius = 20

crclYStepFalling = windowHeight / 10  # 40 pixels each time

# specify rectangle properties
rctLeft = 400
rctTop = 350
rctWidth = 200
rctHeight = 50

QIDic = {}

Q = np.zeros(
    [5000, 3])  # number of states = (windowWidth / 8) * (windowHeight / circleYStep) * (windowWidth / rectWidth)
