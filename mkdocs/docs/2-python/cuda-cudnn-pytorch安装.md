

## 安装内容

win10环境下安装

```
cuda
cudnn
pytorch
```



## 1.安装CUDA

##### 显卡对应的cuda版本

```
# 查看是nvidia驱动是否安装  
“我的电脑”-“设备管理器”-“显示卡”-“驱动程序”


# 查看本机显卡
C:\Program Files\NVIDIA Corporation\NVSMI				# 添加环境变量
nvidia-smi												# cmd查看
# 本次查到的driver Version为445.87

# 查看显卡驱动对应的cuda版本
https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
# 官网地址，注意查看Table 2. CUDA Toolkit and Compatible Driver Versions
# 在win64系统上，cuda10.0.130要求的driver Version>411.31，cuda11.0.1 GA要求的driver 
# Version>451.48
```

##### 下载对应版本cuda

```
# 下载cuda（ 建议用迅雷下载，直接复制链接地址 ）
https://developer.nvidia.com/cuda-toolkit-archive
# 各个版本的cuda,根据显卡匹配的cuda版本，操作系统等信息，下载相应版本
```

##### 安装、环境和系统变量

```
# 安装（默认路径即可），
# 添加环境变量
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\lib\x64
# 检查系统变量path 
CUDA_PATH: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
CUDA_PATH_V10_0: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
# 验证安装
nvcc -V
```



## 2.安装CUDNN

```
参考：https://blog.csdn.net/qq_36653505/article/details/83932941
# 版本对应
https://developer.nvidia.com/rdp/cudnn-archive

### 下载解压后，cudnn将对应文件,复制到cuda的对应安装路径下，如：
C:\cuda\bin\cudnn64_7.dll 
—------> C:\Program Files\NVIDIA GPUComputing

Toolkit\CUDA\v9.1\binC:\cuda\include\cudnn.h 
—--------> C:\Program Files\NVIDIA GPUComputing

Toolkit\CUDA\v9.1\includeC:\cuda\lib\x64\cudnn.lib 
—-------> C:\Program Files\NVIDIA GPUComputing Toolkit\CUDA\v9.1\lib\x64
```



## 3.安装pytorch

```
# 进入pytorch官网，下载对应版本的pytorch安装包
https://download.pytorch.org/whl/torch_stable.html
# 找到对用包，参考https://blog.csdn.net/water19111213/article/details/104352503
搜索：cu100/，找到cuda10.0对应的版本，下载whl文件后pip安装
# 安装torchvison, torchtext, torchaudio,同样的，下载对应的whl文件到本地后pip安装

# 或者直接Pip安装
pip install torch===1.7.0 torchvision===0.8.1 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```



## 4.测试

```
import torch

import torchvision
from PIL import Image
import torchvision.transforms as transforms
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.to(device)
model.eval()
loader = transforms.Compose([transforms.ToTensor()])
image = Image.open('xxx.jpg').convert('RGB')
image = loader(image)
image = image.to(device, torch.float)
x = [image]
predictions = model(x)
print(predictions)
```

