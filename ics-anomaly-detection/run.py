import os
import numpy as np
import subprocess
# import subprocess
# layer_list = [1, 2, 3, 4, 5]
# datasets = ["BATADAL", "WADI"]
# his_length=[50,100,200]
# units = [4, 8, 16, 32, 64, 128, 256]
# for dataset in datasets:
#     for layer in layer_list:
#         for unit in units:
#             for history in his_length:

#                 run_name = f"exp_modelCNN_{dataset}_{layer}layer_{unit}unit_{history}historyLen_3kernel"
#                 run_name= run_name.replace(".","_")
#                 print(run_name[-1] == '\r')
#                 result = subprocess.run(
#                 ["bash", "setup_run_name.sh", run_name],
#                 check=False 
#                 )
#                 if result.returncode != 0:
#                     print(f"setup_run_name.sh lỗi với {run_name}")
#                     continue
#                 subprocess.run([
#                     "python", "main_train.py", "CNN", dataset,
#                     "--run_name", run_name,
#                     "--cnn_model_params_layers", str(layer),
#                     "--cnn_model_params_units", str(unit),
#                     "--cnn_model_params_kernel", "3",
#                     "--cnn_model_params_history", str(history)
                    
#                 ], check=True)

#                 subprocess.run([
#                     "python", "main_eval.py", "CNN", dataset,
#                     "--run_name", run_name,
#                     "--cnn_model_params_layers", str(layer),
#                     "--cnn_model_params_units", str(unit),
#                     "--cnn_model_params_kernel", "3",
#                     "--cnn_model_params_history", str(history),
#                     "--detect_params_windows", "1", "3", "5", "10", "20", "50", "100",
#                     "--detect_params_percentile", "0.95", "0.99", "0.995", "0.999", "0.99995"
#                 ], check=True)

#                 subprocess.run([
#                     "python", "main_model_tuning.py", "CNN", dataset,
#                     "--run_name", run_name,
#                     "--cnn_model_params_layers", str(layer),
#                     "--cnn_model_params_units", str(unit),
#                     "--cnn_model_params_kernel", "3",
#                     "--cnn_model_params_history", str(history),
#                     "--detect_params_hp_metrics", "F1",
#                     "--detect_params_eval_metrics", "F1"
#                 ], check=True)

