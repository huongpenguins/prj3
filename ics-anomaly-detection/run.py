import os
import numpy as np
import subprocess

model_types =["cnn","ae", "lstm"]
for model_type in model_types:
    datasets = ["BATADAL", "WADI"]
    if model_type =="cnn" or model_type == "lstm":
        
        if model_type =="cnn":
            layer_list = [1, 2, 3, 4, 5]
            his_length=[50,100,200]
            units = [4, 8, 16, 32, 64, 128, 256]
        else:
            layer_list = [1,2,3,4]
            his_length=[50,100]
            units = [4, 8, 16, 32, 64, 128]
        for dataset in datasets:
            for layer in layer_list:
                for unit in units:
                    for history in his_length:

                        run_name = f"exp_model{model_type}_{dataset}_{layer}layer_{unit}unit_{history}historyLen_3kernel"
                        run_name= run_name.replace(".","_")
                        if os.path.exists(f"outputs/{run_name}"):
                            continue
                        result = subprocess.run(
                        ["bash", "setup_run_name.sh", run_name],
                        check=False 
                        )
                        if result.returncode != 0:
                            print(f"setup_run_name.sh lỗi với {run_name}")
                            continue
                        subprocess.run([
                            "python", "main_train.py", model_type.upper(), dataset,
                            "--run_name", run_name,
                            f"--{model_type}_model_params_layers", str(layer),
                            f"--{model_type}_model_params_units", str(unit),
                            f"--{model_type}_model_params_kernel", "3",
                            f"--{model_type}_model_params_history", str(history),
                            
                        ], check=True)

                        subprocess.run([
                            "python", "main_eval.py", model_type.upper(), dataset,
                            "--run_name", run_name,
                            f"--{model_type}_model_params_layers", str(layer),
                            f"--{model_type}_model_params_units", str(unit),
                            f"--{model_type}_model_params_kernel", "3",
                            f"--{model_type}_model_params_history", str(history),
                            "--detect_params_windows", "1", "3", "5", "10", "20", "50", "100",
                            "--detect_params_percentile", "0.95", "0.99", "0.995", "0.999", "0.99995",
                            "--eval_plots"
                        ], check=True)

                        subprocess.run([
                            "python", "main_model_tuning.py", model_type.upper(), dataset,
                            "--run_name", run_name,
                            f"--{model_type}_model_params_layers", str(layer),
                            f"--{model_type}_model_params_units", str(unit),
                            f"--{model_type}_model_params_kernel", "3",
                            f"--{model_type}_model_params_history", str(history),
                            "--detect_params_hp_metrics", "F1",
                            "--detect_params_eval_metrics", "F1", "SF1", "SFB13", "SFB31",
                            "--eval_plots"
                        ], check=True)
    if model_type =="ae":
        layer_list = [1, 2, 3, 4, 5]
        cf_list = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
        for dataset in datasets:
            for layer in layer_list:
                for cf in cf_list:
                    run_name = f"exp_model{model_type}_{dataset}_{layer}layer_cf{cf}"
                    run_name= run_name.replace(".","_")
                    result = subprocess.run(
                    ["bash", "setup_run_name.sh", run_name],
                    check=False 
                    )
                    if os.path.exists(f"models/{run_name}"):
                            continue
                    if result.returncode != 0:
                        print(f"setup_run_name.sh lỗi với {run_name}")
                        continue
                    subprocess.run([
                        "python", "main_train.py", model_type.upper(), dataset,
                        "--run_name", run_name,
                        f"--{model_type}_model_params_layers", str(layer),
                        f"--{model_type}_model_params_cf", str(cf),
                        
                    ], check=True)

                    subprocess.run([
                        "python", "main_eval.py", model_type.upper(), dataset,
                        "--run_name", run_name,
                        f"--{model_type}_model_params_layers", str(layer),
                        f"--{model_type}_model_params_cf", str(cf),
                        "--detect_params_windows", "1", "3", "5", "10", "20", "50", "100",
                        "--detect_params_percentile", "0.95", "0.99", "0.995", "0.999", "0.99995",
                        "--eval_plots"
                    ], check=True)

                    subprocess.run([
                        "python", "main_model_tuning.py", model_type.upper(), dataset,
                        "--run_name", run_name,
                        f"--{model_type}_model_params_layers", str(layer),
                        f"--{model_type}_model_params_cf", str(cf),
                        "--detect_params_hp_metrics", "F1",
                        "--detect_params_eval_metrics", "F1", "SF1", "SFB13", "SFB31",
                        "--eval_plots"
                    ], check=True)