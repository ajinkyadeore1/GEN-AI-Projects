# Document Q&A with Gemma Model

## Overview

This project is a Document Q&A system built using the Gemma2-9B-IT model via Groq and Google Generative AI embeddings. It enables users to query multiple PDF documents and retrieve intelligent, context-based responses.

## Use Case

The application is useful for:

- Extracting and analyzing text from PDFs.
- Answering document-specific questions using AI.
- Enhancing research and document comprehension.

## Features

- **Streamlit UI**: Interactive and user-friendly interface.
- **Gemma2-9B-IT Model**: Used for generating intelligent responses.
- **Google Generative AI Embeddings**: Efficient document retrieval with FAISS.
- **PDF Processing**: Extracts text from multiple PDFs.
- **Vector Search with FAISS**: Enables efficient and accurate document-based retrieval.

## Tools & Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web-based interface.
- **Groq API**: For utilizing the Gemma2-9B-IT model.
- **Google Generative AI SDK**: For embeddings and vector search.
- **PyPDFDirectoryLoader**: For processing and loading PDFs.
- **FAISS**: For document similarity search.
- **dotenv**: For managing API keys securely.

## Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload multiple PDF documents into the `./DOC` directory.
2. Click the **"Creating Vector Store"** button to process the documents.
3. Enter a question related to the uploaded PDFs.
4. View AI-generated answers and document similarity search results.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.




