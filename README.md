# ML Model Deployment to AWS EC2 Using Flask API

Deployment of an ML model to an Amazon EC2 instance using Flask, with a basic HMTL web interface for making individual predictions.

![Header Image](header_img.jpg 'Application Screenshot')
 
## Data

The labeled dataset can be downloaded from [here](https://drive.google.com/file/d/1h_jl9xqqqHflI5PsuiQd_soNYxzFfjKw/view?usp=sharing).

## Project Overview

This project seeks to automate the loan eligibiltiy vetting process from the perspective of a large bank. A model was trained and optimized on a dataset of customers who have been approved or denied loans. The training process consisted of EDA, training, and tuning of the model via gridsearch and data pipeline. 

The model was pickled and deployed via Flask API to an Amazon Web Services EC2 instance. A HTML landing page was developed to work with the API to make individual predictions based on input criteria.

## Repository Overview

This repository contains the following files:

```
├───model  
│   └───clf.p 
├───model  
│   └───main.html
├───.gitattributes  
├───.gitignore  
├───ExplorationAndModeling.ipynb
├───LoanPredictionDeployment.pptx
├───README.md
└───app.py  
```  

* **model** contains the pickled model for deployment.
* **templates** contains the HTML file for the landing page.
* **ExplorationAndModeling.ipynb** was used to perform EDA, train, and optimize the model.
* **LoanPredictionDeployment.pptx** contains presentation slides detailing the project.
* **app.py** contains the Flask API and application logic.