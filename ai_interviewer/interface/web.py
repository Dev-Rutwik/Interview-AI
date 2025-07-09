import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO
import os
import sys
from resume_parser import extract_resume_details

    

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file"""
    pdf_reader = PdfReader(BytesIO(pdf_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""  # Handle pages with no text
    return text

def main():
    st.title("PDF Chat App")
    
    # Initialize session state for PDF text
    if 'pdf_text' not in st.session_state:
        st.session_state.pdf_text = None
    
    # Show uploader in expander only if no PDF has been processed yet
    if st.session_state.pdf_text is None:
        with st.expander("Upload PDF", expanded=True):
            uploaded_file = st.file_uploader(
                "Upload a PDF file", 
                type=["pdf"],
                key='file_upload_widget'
            )
            
            if uploaded_file is not None:
                with st.spinner("Processing PDF..."):
                    st.session_state.extracted_text = extract_text_from_pdf(uploaded_file)
                    st.session_state.pdf_text = extract_resume_details(st.session_state.extracted_text)
                st.success("PDF processed successfully!")
                st.rerun()  # Refresh to hide the expander
    
    # Display extracted text (you can remove this if you don't want to show it)
    if st.session_state.pdf_text:
        st.subheader("AI Questions")
        st.text_area("PDF Content", st.session_state.extracted_text,height=300)

if __name__ == "__main__":
    main()