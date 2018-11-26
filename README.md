# Detecting frauds with a Self Orginzed Map (SOM)

## Introduction
This project consists in detecting from a bank dataset, which users are potentially frauds. As from the beginning I do not know which users are frauds (I do not have labels), I think that a good approach would be use unsupervised learning. To be more specific, I will use a Self Organized Map (SOM).

## Dataset
The dataset comes from [here](http://archive.ics.uci.edu/ml/datasets/statlog+(australian+credit+approval)). It has 15 independent variables and one dependent variable which consist in whether the client was given the credit card or no. You can see a deeper description about each variable in the link provided above.
As this dataset is not scaled, that is one of the first things that we have to do. 

## Self Organized Map
To build the SOM, I had two posibilities:
- Buid it completely by my own
- Use one built by another person
To keep things simple, I decided to use the second option.
I decided to use [Minisom](https://pypi.org/project/MiniSom/).
This is a 10 by 10 units SOM which I train for 100 epochs as there is not too much data in the dataset. 

## Results
To plot the results, I created a class called Som_Plotter. This class is responsable of after the SOM it’s been trained, plotting the result SOM together with some marks to know wheter the clients for each unit received the credit card or not.

<p align="center">
    <img width="413" alt="Result SOM" src="https://user-images.githubusercontent.com/15388747/48998397-49ee5f00-f14b-11e8-8f86-bdf05dcd775f.PNG">
</p>

Finally, to indentify the clients that could potentially be frauds, I get all the clients contained in the white units of the SOM, undo the scalling and print them.
