# Multiple PDF Chatbot with Gemini AI

## Overview

This project is an AI-powered chatbot application that allows users to interact with multiple PDF documents using Google's Gemini Pro model. Built with Streamlit, it enables intelligent Q&A based on document content.

## Use Case

The chatbot is designed for:

- Extracting and analyzing text from multiple PDFs.
- Answering document-specific questions using AI.
- Enhancing research and document comprehension with conversational AI.

## Features

- **Streamlit UI**: A simple and interactive frontend for user interaction.
- **Google Gemini Pro API**: Integration with the Gemini Pro model for intelligent responses.
- **PDF Processing**: Extracts text from multiple uploaded PDFs.
- **Vector Search with FAISS**: Efficient document-based retrieval for better responses.
- **Real-Time AI Responses**: Generates meaningful insights based on user queries.

## Tools & Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For creating the web-based user interface.
- **Google Generative AI SDK**: To access Gemini Pro capabilities.
- **PyPDF2**: For extracting text from PDFs.
- **FAISS**: For vector search and efficient document retrieval.
- **dotenv**: For managing API keys securely.

## Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload multiple PDF documents using the sidebar.
2. Enter a text-based question related to the uploaded PDFs.
3. Click the "Submit & Process" button to extract and analyze the document content.
4. Ask questions, and the AI will generate relevant responses based on the documents.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.




