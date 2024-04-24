# PDF-Search [RAG-based-context-AI]

### Scope of Project
The scope of this exercise is to build a simple step within a data pipeline to help with data collection and transformation for an AI assistant based system. The primary data source will be a PDF document for this pipeline, and multiple documents can be used. The objective is that these steps are delivering a RAG based context for the AI assistant to answer questions based on the contents within the document(s).

### How to Run 
1. Clone the repo.
2. Create a Virtual Env using the command `python3 -m venv venv`
3. Activate the environment. `source venv/bin/activate`
4. Install required packages. `pip install -r requirements.txt`
5. Open the python notebook [pipeline_run](https://github.com/Anshumank399/RAG-based-context-AI/blob/main/pipeline_run.ipynb)
6. Input the OPENAI_API_KEY in the first cell.

### Steps Involved

1. Pick a source document or can be a handful of documents that are PDF format. This will be the primary data source for this exercise. You can use any PDFs from this location: https://arxiv.org/list/cs/recent Or you can use any PDF of your
choice for this exercise.
2. Read the file from a source location (local folder under `data/`).
3. The document from this location is parsed, using a ocr library called `surya-ocr`. It is one of the better OCR libraries, but any other library can be used. The OCR outputs are saved in the `data/results/<file-name>/results.json`
   - [pdf_ocr](https://github.com/Anshumank399/RAG-based-context-AI/blob/main/pipeline/pdf_ocr.py) script is used to OCR or direct shell command `surya_ocr data/sample2.pdf --langs en --results_dir data/results/` can be used.
   - [text_extraction](https://github.com/Anshumank399/RAG-based-context-AI/blob/main/pipeline/text_extraction.py) script is used to transform and get only text data along with metadata as page number, file name. 
4. Implement preprocessing steps as you see necessary based on the sample document. These will be data cleansing tasks that might be necessary.
   - Due to use of a good ocr library, the level of cleansing required is not intense. 
5. Create vector embeddings out of the text chunks that are extracted. If there are any images in the document, those can be ignored. You can use any embeddings model for the vectorization. ChromaDB can be used to store the embeddings and any other choices can be used.
6. Write a function to search these vectors with a query to return similar results. In this function, convert the query to vector form and return results based on the nearest similar result.
7. Build a LLM based retriever with examples.

### Improvements for the future
1. Add more parameters for meta data like paragraph number, etc. for better tracebility and catching hallucinations quickly.
2. Understand the use case better and tune the similarity based on that, using threshold or number of outputs required or the type of similarity function. 
3. Study text splitter parameters and how it affects the output.
4. Clean data to remove the citations in the end of file if its not required, and some minor data cleaning.
5. Build a UI for the users to be able to search on an interface rather than a notebook.
6. Build data pipeline scripts and not use the python notebook to be used in production.
7. Model needs to better decide between general knowledge and the given context. Example below: 
   ![image](https://github.com/Anshumank399/RAG-based-context-AI/assets/21052254/2fc1b659-c799-4329-8980-1c13af93a41b)

