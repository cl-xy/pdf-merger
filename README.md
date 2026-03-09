# PDF Merger (Streamlit)

A simple Streamlit app to upload multiple PDF files and merge them into one downloadable PDF.

## Features

- Upload multiple `.pdf` files from your browser
- Merge files in the same order they are uploaded
- Download the merged file instantly

## Requirements

- Python 3.9+ (recommended)
- Dependencies listed in `requirements.txt`

## Setup

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## Project Structure

- `app.py`: Streamlit app entry point and PDF merge logic
- `requirements.txt`: Python dependencies

## Notes

- The app processes uploaded files in memory.
- No persistent upload folder is required.
