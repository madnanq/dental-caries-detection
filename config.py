EPOCHS = 50 # Number of the epochs
SAVE_EVERY = 5 # after how many epochs to save a checkpoint
LOG_EVERY = 1 #  log training and validation metrics every `LOG_EVERY` epochs
BATCH_SIZE = 2 
DEVICE = 'cuda:1'  
LR = 0.0001
ROOT_PATH = '/home/adnan/Atif/Misc/Dental/Data/mandibular data/'

CLASSES_TO_TRAIN = ['canal','bg']

#CLASSES_TO_TRAIN = ['sky', 'bridge', 'building', 'wall', 'electric_pole', 'street light', 'pavedroad', 'unpaved_road', 'solid yellow line', 'pavement_sidewalk', 'concrete_barrier', 'fence', 'traditional truck', 'container truck', 'hino_bus', 'traditional bus', 'car', 'van', 'mini_van', 'rickshaw', 'pickup', 'mini-pickup', 'motor_bike', 'tree', 'vegetationmisc', 'signboard', 'speedlimit', 'directionboard' ,'distanceboard' ,'pedestrian', 'mountains', 'grassy_road_divider']

# DEBUG for visualizations
DEBUG = True
