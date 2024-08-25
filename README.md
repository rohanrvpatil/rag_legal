**Note: "Insights obtained" section of the README includes only my learnings from project implementation.**

## Table of Contents:

- [About](#about)
- [Implementation](#implementation)
- [Screenshots](#screenshots)
- [Insights obtained](#insights-obtained)

## About:

### Models implemented:
BART (pretrained facebook/bart-large)

### Datasets used:
IN-Abs legal dataset: https://zenodo.org/records/7152317#.Yz6mJ9JByC0 from the GitHub repository: https://github.com/Law-AI/summarization from the link: 

### Note:
1. playground.ipynb contains code snippets that I will reuse as a developer.
2. check.py contains code to check Number of GPUs available in a device
3. rag_legal contains code for the actual project

### Project:
Legal Document Analysis and Summarization Tool using RAG

### Overview:
In this project, I have used a subset of a legal dataset consisting of 7030 judgement, summary pairs in training folder and 100 judgement, summary pairs in testing folder. I have preprocessed the data and used BART-large model of Facebook for Generative part of this project. However, I was not able to complete the project due to insufficient RAM in Google Colab and my local device.

## Implementation:

1) Dataset is downloaded from https://github.com/Law-AI/summarization from the link: https://zenodo.org/records/7152317#.Yz6mJ9JByC0
IN-Abs data is used. I used a subset of train-data of 10 documents (.txt files) for training and 100 documents (.txt files) for testing
I took a small subset for training since sufficient RAM wasn't available on my local device and Google Colab as well.

2) Imported judgement and summary files from train-data and test-data and preprocessed it

3) facebook/bart-large model is downloaded to work as the Generative component of this project
from Hugging Face

4) Input and output tensors are prepared for training and testing a sequence-to-sequence model
by tokenizing text data.

5) TextDataset class for handling tokenized input and output pairs, and uses a collate_fn function to
pad sequences to uniform length within batches. It then creates DataLoader instances for training
and testing, which handle batching and shuffling of the data. 

6) Model is trained for 3 epochs using GPU. However, training was not possible since sufficient RAM wasn't
available on my local device and Google Colab as well.


## Screenshots:

<mark><strong>Preprocessed data</strong><mark>

![Preprocessed data](https://github.com/rohanrvpatil/rag_model/blob/main/screenshots/preprocessed_data.png?raw=true)


## Insights obtained:
**Note: This section of the README includes only my learnings from project implementation.**

1) Fine-tuning BART large model on textual data requires huge amounts of RAM
