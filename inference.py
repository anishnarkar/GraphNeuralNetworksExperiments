from doubleunet_multiclass import double_Unet
from matplotlib import pyplot as plt
import numpy as np
from utils import load_images_from_folder

def generate_segmentation(model,
                          source_image,
                          location = 0,
                          model_name='double_unet'):

    
    if location == 1:
        images = load_images_from_folder(source_image)
        target = np.array(images)
        target = target/255
        target = target.reshape([1,128,128,3])
    else:
        target = source_image/255
        target = target.reshape([1,128,128,3])        
    
    segmentation = model.predict(target)
    
    return segmentation
    
    
    
    
    
    

