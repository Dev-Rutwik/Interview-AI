from setuptools import setup, find_packages

setup(
    name="Interview-AI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langgraph",
        "langchain-mistralai",
        "python-dotenv",
        "scikit-learn",
        "nltk",
        "pdfminer.six",
        "streamlit"
    ],
    include_package_data=True,
)
