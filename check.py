# python file to check number of GPUs available

import tensorflow as tf
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = 0

print("Num GPUs Available: ", len(tf.config.list_physical_devices("GPU")))
