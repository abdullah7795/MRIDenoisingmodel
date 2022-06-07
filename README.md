# MRI Denoising Model

Presenting a CNN-based algorithm with the help of encoders and decoders to estimate the original image by suppressing noise from a noise-contaminated version of the image and by applying our efficient algorithm to denoise the image with the highest SSIM and PSNR values with low processing time. We fetch our MRI datasets (around 7200 images) from Brainweb. The collected MRI datasets are segregated into datasets of original image, noisy image, and denoised image for the purpose of training and testing. Our CNN model is created with the help of encoders and decoders. The concept of maxpooling2D and convo2D layers is implied to create autoencoders and decoders. Where in the model, Relu and Sigmoid are implemented as activation functions and Adam is used as an optimizer for autoencoders. Finally, we capture the desired output value of PSNR, which is sufficient to denoise an image and excels over other existing models, and proceed to build an application to denoise medical images.

# To Run this Model on your Machine Please Follow the Steps given Below

## 1. Download The Repository

Type the command : \
git clone https://github.com/abdullah7795/MRIDenoisingmodel.git \
cd MRIDenoisingmodel 



## 2. Install Python3

install python \
Linux: \
sudo apt install python3.8 

check the version using command: \
python --version 

Windows: \
download and run from [https://www.python.org/downloads/](https://www.python.org/downloads/) 



## 3. Install Anaconda From The Link:

Linux: \
[https://docs.anaconda.com/anaconda/install/linux/](https://docs.anaconda.com/anaconda/install/linux/) 

Windows: \
[https://docs.anaconda.com/anaconda/install/windows/](https://docs.anaconda.com/anaconda/install/windows/) 


## 4. Open Terminal In Repository:

open cmd/terminal in the repository. \
run: python3 model_test.py 

## 5. The Output Will Be Saved As Denoised_Output_Image.tiff And Denoised_Output_Image.tif

you can change the names in model_test.py file. 
### Run:  python model_test.py 


# Access Model Directly from the Website
If you want to denoise your image without any hassle of installing the above mentioned libraries and running the commands please visit our website link given below: 
https://mohammedsaif001.github.io/Medical-Image-Denoising/ 
