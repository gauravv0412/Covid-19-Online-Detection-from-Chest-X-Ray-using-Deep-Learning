# Covid-19-Online-Detection-from-Chest-X-Ray-using-Deep-Learning
This project is based on detecting covid-19 infection from Chest X-ray(front view). 

Site Link: http://covid19-online-detection.herokuapp.com

It is a **Deep Learning Neural Network model** which consists of 2D-Convolution and Dense Layers with over 1 million trained parameters and accuracy of 97.7%. 

AI Model is built on **Keras** and **Tensorflow** as backend. Website is built using **Django** framework for backend and Materialise for frontend.

## Installation Documentation



Step - 1: Install git on your desktop(for Mac donwload from [here](https://sourceforge.net/projects/git-osx-installer/files/) , for Windows donwload from [here](https://git-for-windows.github.io/) , for Linux run this command - `sudo apt-get install git`) and after installing verify the installation and clone this repository.

    git --version
    git clone https://github.com/gauravv0412/Covid-19-Online-Detection-from-Chest-X-Ray-using-Deep-Learning.git
    
![Alt text](/Screenshots/1.png)
    
Step - 2: Create virtual environment and install all the required libraries from requirements.txt. Use apt-get in case of linux and [homebrew](https://brew.sh) (`brew install`) in case of windows and linux. Refer to this [site](https://brew.sh) for Homebrew installation. Install Pyhton version == 3.7.1

    cd Covid-19-Online-Detection-from-Chest-X-Ray-using-Deep-Learning/
    
    sudo apt-get install python3.7
    sudo apt-get install python3-pip

![Alt text](/Screenshots/2.png)
![Alt text](/Screenshots/3.png)

    pip3 install virtualenv
    virtualenv env
    
![Alt text](/Screenshots/4.png)
    
    source env/bin/activate
    pip3 install -r requirements.txt
    
![Alt text](/Screenshots/5.png)
 
Step - 3: Launch Django app by: 

    python3 manage.py migrate
    python3 manage.py runserver
  
![Alt text](/Screenshots/6.png)
![Alt text](/Screenshots/7.png)

## Demo of Application

Upload the X-Ray scan and click on "Predict" to make prediction.
You can use sample images provided in the [Sample_Images](https://github.com/gauravv0412/Covid-19-Online-Detection-from-Chest-X-Ray-using-Deep-Learning/tree/master/Sample%20Images) directory.

![Alt text](/Screenshots/9.png)

    
