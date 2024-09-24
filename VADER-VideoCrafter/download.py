from huggingface_hub import snapshot_download
import os

model_id = "VideoCrafter/VideoCrafter2" 

target_dir = "/home/wenhao/Project/greatxue/mj_models/VADER/VADER-VideoCrafter/checkpoints/base_512_v2"
os.makedirs(target_dir, exist_ok=True)

local_model_path = snapshot_download(repo_id=model_id, local_dir=target_dir)
print(f"Model downloaded to: {local_model_path}")