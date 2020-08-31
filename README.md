# Iris Classifier based on Flask using Pytorch neural networks

__________

**Four sliders** to enter data.

![Homepage](https://github.com/CosmoSt4r/Iris-Classification/blob/master/readme/Homepage.jpg?raw=true)

__________

Enter data and press **"Calculate"**.

_________

![Iris-types](https://github.com/CosmoSt4r/Iris-Classification/blob/master/readme/Iris-types.jpg?raw=true)

_________

<br>

## How to install?



### Clone

Clone this repo to your local machine using `git clone https://github.com/CosmoSt4r/Iris-Classification`

### Required packages

To start the server you need the following packages: 

 - Flask
 - Pytorch
 - Pandas
 - Scikit-learn

To install packages:

```py
pip install flask torch pandas scikit-learn 
```

### Starting the server

```py
python main.py
```
> or just open `main.py`

### Opening app in browser

Open your browser and go to the `127.0.0.1:5000` address. You will see the login page.

## Neural network

Neural network is built using **Pytorch** and named **IrisNet**. 

______________________

- **Structure**: 4 x 16 x 16 x 3
- **Activation functions**: 2 _Sigmoid_ functions and _Softmax_ on output
- **Loss function**: Cross entropy loss
- **Optimizer**: Adam
- **Learning rate**: _0.001_

<br>

You can change parameters as you want for better accuracy. Now **average accuracy** is _95-97%_.

______________________
