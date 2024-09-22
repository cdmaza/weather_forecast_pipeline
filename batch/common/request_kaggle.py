import pandas as pd
import os
import opendatasets as od
import zipfile

# from google.cloud import bigquery

dataset = 'https://www.kaggle.com/datasets/shahmirvarqha/weather-data-malaysia'

save_path = os.path.join(os.path.dirname(__file__), '..', 'data')

os.makedirs(save_path, exist_ok=True)

od.download(dataset, path=save_path)