# Iris Model Inference Streamlit App

This Streamlit app allows users to perform inference on an Iris classification model using their own data. The app provides an intuitive interface for uploading data, viewing predictions, and downloading results.

## Features

-   **Data Upload**: Users can upload their own CSV files containing Iris feature data.
-   **Model Inference**: The app uses a pre-trained Random Forest Classifier to make predictions on the uploaded data.
-   **Results Display**: Predictions are displayed in a user-friendly format.
-   **Download Option**: Users can download the prediction results as a CSV file.


## Requirements

To run this app, you need to install the required Python libraries. A `requirements.txt` file is provided in the project repository. You can install all the dependencies using pip:

`pip install -r requirements.txt` 

## Usage

1.  To run the Streamlit app on local machine run the command:
    
    `streamlit run app.py` 

2.  Alternatively the deployed app can be accessed using this link: [https://iris-model-deploy.streamlit.app](https://iris-model-deploy.streamlit.app/)
    
3.  Click on the "Let's get started" button.
4.  Upload a CSV file containing Iris feature data.
5.  View the sample of uploaded data and predicted probabilities.
6.  Download the prediction results if desired.

## Data Format

The app expects the input data to be in the following format:

-   CSV file (UTF-8 encoded)
-   Comma-separated values
-   Decimal points as delimiters
-   First row as header
-   Four columns representing Iris features (column names are not important)

## Model

The app uses a pre-trained Random Forest Classifier model stored in

`model.joblib`

This model predicts the probabilities of an Iris sample belonging to each of the three Iris species: setosa, versicolor, and virginica.

## Output

The app generates probability predictions for each Iris class:

-   setosa_probability
-   versicolor_probability
-   virginica_probability

Users can download these predictions as a CSV file.

## Development

This app was developed using Streamlit, a powerful library for creating data apps in Python. The main components of the app include:

-   Sidebar with data requirements and developer information
-   File uploader for CSV input
-   Data preview functionality
-   Model inference using joblib
-   Results display and download option

## Future Improvements

-   Add data validation to ensure uploaded files meet the required format
-   Implement error handling for various edge cases
-   Include visualizations of prediction results
-   Allow users to choose different machine learning models

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or feature requests.