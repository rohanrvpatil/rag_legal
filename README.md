**Note: "Insights obtained" section of the README includes only my learnings from project implementation.**

## Table of Contents:

- [About](#about)
- [Implementation](#implementation)
- [Screenshots](#screenshots)
- [Insights obtained](#insights-obtained)

## About:

### **Description of Upwork gig:**
Needs to hire 4 Freelancers
Here's your revised job posting with defined sample projects and the extended application deadline:

**Job Posting: RAG ChatGPT Engineer**

**Position Title:** RAG ChatGPT Engineer

**Location:** Remote

**Type:** Freelance/Contract

**Company:** Keensight Analytics LLC

**About Us:**
Keensight Analytics LLC is at the forefront of innovative AI and data analytics solutions. We specialize in developing cutting-edge technologies to meet our clients' diverse needs across various industries. We are looking for a talented RAG (Retrieval-Augmented Generation) ChatGPT Engineer to join our team and create tailored RAG models on demand.

**Job Description:**
We are seeking a skilled RAG ChatGPT Engineer to develop, implement, and optimize Retrieval-Augmented Generation models using various state-of-the-art technologies such as ChatGPT, Claude, LLaMA, and other models available from HuggingFace. The ideal candidate will have a strong background in natural language processing, machine learning, and experience with these GPT models. Over the course of six months, you will be expected to build 40-50 applications, ensuring high performance and customization to meet our specific needs.

**Responsibilities:**
- Design, develop, and deploy RAG models using ChatGPT, Claude, LLaMA, and other HuggingFace models for various applications.
- Customize RAG models based on specific client requirements.
- Optimize and fine-tune models to ensure high performance and accuracy.
- Collaborate with team members to integrate RAG models into existing systems.
- Conduct thorough testing and validation of models to ensure reliability.
- Stay updated with the latest advancements in NLP and machine learning technologies.
- Provide documentation and support for implemented models.
- Advanced Prompt Engineering

**Sample Projects:**
1. Customer Service Bot for eCommerce
2. Real-time News Summarization Engine
3. Financial Forecasting Model for Stock Market Trends
4. Healthcare Patient Intake and Diagnostic Assistant
5. Educational Content Personalization Engine
6. Legal Document Analysis and Summarization Tool
7. Social Media Sentiment Analysis for Brand Monitoring
8. Recipe Generator and Nutritional Advisor
9. Custom Travel Itinerary Planner
10. Fraud Detection System for Online Transactions

**Requirements:**
- Proven experience in developing RAG models or similar NLP technologies.
- Strong proficiency in Python and relevant machine learning libraries (e.g., TensorFlow, PyTorch).
- In-depth knowledge of ChatGPT, Claude, LLaMA, and other HuggingFace models.
- Familiarity with information retrieval techniques and tools.
- Ability to understand and implement client requirements effectively.
- Excellent problem-solving skills and attention to detail.
- Strong communication and collaboration skills.
- Ability to work independently and manage multiple projects simultaneously.
- Commitment to building 40-50 applications over a six-month period.

**Preferred Qualifications:**
- Experience with cloud platforms such as AWS, Azure, or Google Cloud.
- Knowledge of containerization and orchestration (Docker, Kubernetes).
- Background in data analytics and understanding of different industry needs.
- Previous experience in a remote or freelance work environment.

**How to Apply:**
If you are passionate about NLP and AI, and have a track record of creating high-quality RAG models, we want to hear from you! Please submit your resume, a cover letter detailing your relevant experience, and any examples of previous work or projects in your proposal. We have a list of 50 projects to choose from, and you will pick 10 RAGS to build for this contract for the budget stated. **$25 per 10 unique RAGs. No exceptions.** Best candidates have a chance to join the firm serving US clients at their hourly rate.

**Application Deadline:** August 31, 2024

Join Keensight Analytics LLC and be part of a team that is shaping the future of Generative AI.


### Models implemented:
BART (pretrained facebook/bart-large)

### Upwork gig link:
[Upwork gig link](https://www.upwork.com/jobs/~01b0b2671bf33fd4e9)

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


insert image

Preprocessed data

## Insights obtained:
**Note: This section of the README includes only my learnings from project implementation.**

1) Fine-tuning BART large model on textual data requires huge amounts of RAM