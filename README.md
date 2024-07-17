# Pretrained Image Classifier for Identifying Dog Breeds

# Overview
<br>
This project leverages pretrained Convolutional Neural Network (CNN) models to classify images of dogs and identify their breeds. The project compares the performance of three different CNN architectures: ResNet, AlexNet, and VGG, to determine the most accurate model for this classification task. The script processes images, extracts true labels from filenames, classifies images using a chosen CNN model, and evaluates the classifier's performance.
<br>
<br>

# Table of Contents
~Overview <br>
~Installation <br>
~Usage<br>
~Project Structure <br>
~Contributing <br>
~License <br>

# Installation

Prerequisites <br>
Ensure you have Python 3.x installed. You can download it from the official website.

# Clone the Repository 
<br> 
git clone https://github.com/yourusername/pretrained-image-classifier.git
cd pretrained-image-classifier

<br>
<br>

# Install Dependencies
<br>
Install the required Python packages using pip:
<br>
pip install -r requirements.txt
<br>

# Usage
<br>
# Command Line Arguments
<br>
The script check_images.py accepts the following command line arguments:
<br>

--dir: Directory with pet images <br>
--arch: CNN model architecture to use (resnet, alexnet, vgg) <br>
--dogfile: File that contains dog breed names <br>
<br>

# Output 
<br>
The script will classify the images, compare the results with the true labels, and output the classification performance, including metrics like accuracy, percentage of correct breed classifications, and other relevant statistics. <br>


<br>
<br>
<br>
<br>

pretrained-image-classifier/
│
├── pet_images/                   # Directory containing pet images
│
├── dognames.txt                  # File containing the list of dog breed names
│
├── get_input_args.py             # Function to get command line arguments
├── get_pet_labels.py             # Function to extract pet labels from filenames
├── classify_images.py            # Function to classify images using a CNN model
├── adjust_results4_isadog.py     # Function to adjust results to determine if the classifier correctly identified dogs
├── calculates_results_stats.py   # Function to calculate classification statistics
├── print_results.py              # Function to print results
├── check_images.py               # Main script to run the classification process
│
├── requirements.txt              # List of required Python packages
├── README.md                     # Project README file

<br>
<br>

# Contributing
<br>

Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
<br>

Fork the Project <br>
Create your Feature Branch (git checkout -b feature/YourFeature) <br>
Commit your Changes (git commit -m 'Add some feature') <br>
Push to the Branch (git push origin feature/YourFeature) <br>
Open a Pull Request <br>



