Create a virtual enviroment in python3.12

python3.10 venv <Name_Of_Your_Virtual_Enviroment>

source ./Name_Of_Your_Virtual_Enviroment/bin/activate


Before Installing RealtimeSTT do these steps first

1. sudo apt-get update
2. sudo apt-get install python3-dev
3. sudo apt-get install portaudio19-dev

then install torch with cuda depending on your cuda version
check nvidia-smi to figure out which version you have

cuda 12.8:
pip install typing-extensions==4.10.0
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

then install 

cuda 12 latest toolkit
https://developer.nvidia.com/cuda-toolkit-archive

and install cuda 12 cuDNN
https://developer.nvidia.com/cudnn-downloads

then install ffmpeg
Ubuntu:
sudo apt update && sudo apt install ffmpeg

and install ffmpeg-python

pip install ffmpeg-python

then install python3.X dev tools

sudo apt install python3.10-dev

and then install RealtimeSTT

pip install RealtimeSTT

