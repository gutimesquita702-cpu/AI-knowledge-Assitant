# AI Knowledge Assistant

A command-line question-answering application that searches a local PDF and uses
the Google Gemini API to generate an answer from the most relevant text chunk.

## How it works

1. `app/main.py` extracts text from the configured PDF.
2. `app/text_splitter.py` divides the text into chunks of 500 words, with a
   50-word overlap between consecutive chunks.
3. `app/retrieval.py` selects the chunk containing the greatest number of
   question words.
4. `app/IA_.py` sends the question and selected chunk to Gemini and prints the
   generated answer.

## Requirements

- Python 3
- A Google Gemini API key
- A PDF with extractable text

Install the Python dependencies:

```powershell
python -m pip install google-genai pypdf
```

## Configuration

Set the `GEMINI_API_KEY` environment variable. In PowerShell, for the current
terminal session:

```powershell
$env:GEMINI_API_KEY = "your-api-key"
```

In `app/main.py`, update `pdf_path` to the location of the PDF you want to
search. The current value is a machine-specific path.

## Run

From the project root, run:

```powershell
python -m app.main
```

Enter a question when prompted. The application prints the answer returned by
Gemini. If no chunk shares any words with the question, it reports that no
relevant chunk was found.

## Project structure

```text
app/
  IA_.py              Gemini response generation
  document_loader.py  PDF text extraction
  main.py             Application entry point and workflow
  retrieval.py        Keyword-based chunk selection
  text_splitter.py    Text chunking with overlap
documents/            Sample PDF documents
```

## Current limitations

- Retrieval uses simple, case-insensitive word matching, not embeddings or
  semantic search. It does not normalize punctuation or word forms.
- Only the single best-matching chunk is sent to Gemini.
- Scanned PDFs without an embedded text layer require OCR, which is not
  currently implemented.
- Gemini output depends on API availability, model access, and the configured
  API key.