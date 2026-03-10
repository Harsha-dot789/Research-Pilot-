import streamlit as st
from index import summarize_text, extract_insights, search_papers
import PyPDF2

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("📚 AI Research Assistant")
st.write("Discover, organize, and interact with academic papers using AI")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Upload Paper", "Search Papers", "Summarize Paper", "Extract Insights"]
)

# Upload Paper
if menu == "Upload Paper":
    st.header("Upload Research Paper (PDF)")
    
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        st.success("Paper uploaded successfully!")
        st.session_state["paper_text"] = text


# Search Papers
elif menu == "Search Papers":
    st.header("🔎 Search Academic Papers")

    query = st.text_input("Enter research topic")

    if st.button("Search"):
        results = search_papers(query)
        st.write(results)


# Summarize Paper
elif menu == "Summarize Paper":
    st.header("📄 AI Paper Summary")

    if "paper_text" in st.session_state:
        if st.button("Generate Summary"):
            summary = summarize_text(st.session_state["paper_text"])
            st.write(summary)
    else:
        st.warning("Please upload a paper first")


# Extract Insights
elif menu == "Extract Insights":
    st.header("💡 Research Insights")

    if "paper_text" in st.session_state:
        if st.button("Generate Insights"):
            insights = extract_insights(st.session_state["paper_text"])
            st.write(insights)
    else:
        st.warning("Upload a research paper first")