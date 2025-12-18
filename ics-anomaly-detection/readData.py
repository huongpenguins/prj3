import numpy as np

data = np.load("outputs/exp_modelAE_BATADAL_5layer_4_0cf/AE-BATADAL-l5-cf4.0-F1.npy", allow_pickle=True)

print("Shape:", data.shape)
print("Type:", type(data))
print(data)
