#KHADRAOUI Mohamed El Bachir (CHPS Master2)

#This sets up ROMEO to execute edge-connect
#But still doesn't work becaise of compatibility issues with Python3.6

pip install -r requirements.txt
pip install torchvision 
pip install opencv-python
pip install numpy==1.16.4
pip install ipykernel
pip install pyyaml==5.4.1

chmod +x ./scripts/download_model.sh
./scripts/download_model.sh
