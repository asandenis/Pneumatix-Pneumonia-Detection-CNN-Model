import kagglehub
import config

def download_dataset():
    path = kagglehub.dataset_download("tolgadincer/labeled-chest-xray-images")
    print("Dataset downloaded to:", path)
    config.DATASET_PATH = path
    return path

download_dataset()