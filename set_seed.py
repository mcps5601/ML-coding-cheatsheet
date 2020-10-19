##### PyTorch #####
import torch
import os, random
import numpy as np

# This function can be successfully used in PyTorch v.1.6.0 for reproducibility.
def set_seed(seed):
    """
    Args:
        seed: an integer number to initialize a pseudorandom number generator
    """
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        #torch.cuda.manual_seed_all(seed)  # if using more than one GPUs
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


##### TensorFlow1 #####
import tensorflow.compat.v1 as tf

# This function can be successfully used in TensorFlow 1.x for reproducibility.
def tf1_set_seed(seed):
    """
    Args:
        seed: an integer number to initialize a pseudorandom number generator
    """
    tf.random.set_seed


##### TensorFlow2 #####
import tensorflow as tf
import os, random
import numpy as np

# This function can be successfully used in TensorFlow 2.x and Keras for reproducibility.
def tf2_set_seed(seed):
    """
    Args:
        seed: an integer number to initialize a pseudorandom number generator
    """
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED']=str(seed)
    random.seed(seed)
    np.random.seed(seed)
