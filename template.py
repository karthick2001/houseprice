import os
from pathlib import Path

list_of_files=[
".github/workflows/cicd.yaml",
"src/_init_.py",
"src/data/data_loader.py",
"src/model/train.py",
"src/model/inference.py",
"configs/config.yaml",
"configs/eks-deployment.yaml",
"Dockerfile",
"requirements.txt",
"buildspec.yaml",
"app.py",
"templates/home.html",
"templates/predict.html"



]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass