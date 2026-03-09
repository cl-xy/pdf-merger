import streamlit as st
from pypdf import PdfWriter
import io

def merge_pdfs(pdf_files):
    """
    Merge a list of uploaded PDF files into a single BytesIO object.
    Preserves the order of files as provided in the list.
    """
    merger = PdfWriter()
    
    # Merge PDFs in the order they were uploaded
    for pdf_file in pdf_files:
        # pypdf can read directly from a file-like object
        merger.append(pdf_file)
    
    output_stream = io.BytesIO()
    merger.write(output_stream)
    merger.close()
    
    output_stream.seek(0)
    return output_stream

def main():
    st.set_page_config(page_title="PDF Merger", page_icon="📄")
    
    st.title("📄 PDF Merger")
    st.write("Upload multiple PDF files and merge them into a single document.")

    # File uploader allows multiple files
    uploaded_files = st.file_uploader(
        "Choose PDF files", 
        type="pdf", 
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"Selected {len(uploaded_files)} files:")
        
        # Display selected files with an option to see their names
        for i, file in enumerate(uploaded_files):
            st.text(f"{i+1}. {file.name}")

        # Add a merge button
        if st.button("Merge PDFs"):
            if len(uploaded_files) < 2:
                st.warning("Please upload at least 2 PDF files to merge.")
            else:
                with st.spinner("Merging PDFs..."):
                    try:
                        merged_pdf_stream = merge_pdfs(uploaded_files)
                        
                        st.success("PDFs merged successfully!")
                        
                        # Provide download button for the merged file
                        st.download_button(
                            label="Download Merged PDF",
                            data=merged_pdf_stream,
                            file_name="merged_document.pdf",
                            mime="application/pdf"
                        )
                    except Exception as e:
                        st.error(f"An error occurred during merging: {str(e)}")
    else:
        st.info("Please upload PDF files to get started.")

if __name__ == "__main__":
    main()
