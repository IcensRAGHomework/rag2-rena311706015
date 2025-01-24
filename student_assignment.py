from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
import re

    
q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    pdf = loader.load()
    c_splitter = CharacterTextSplitter(chunk_overlap= 0)
    chunk = c_splitter.split_documents(pdf)
    return chunk[len(chunk) - 1]
    

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    pdf = loader.load()
    full_text = "\n".join([page.page_content for page in pdf])
    r_splitter = RecursiveCharacterTextSplitter(
        separators=[r'第 +[一二三四五六七八九十0-9\-]+ +[章條]'],
        chunk_size=10,
        chunk_overlap=0,
        is_separator_regex=True,
    )
    chunk = r_splitter.split_text(full_text)

    return len(chunk)

    

# print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))
