import tensorflow as tf

from beta.nncf.tensorflow.functions import logit

default_rb_mask_value = logit(tf.ones(1) * 0.99)
