from setuptools import setup, find_packages

setup(
    name='gemini-n-db',
    version='0.1.0',
    author='PJ',
    author_email='piyankara.jayadewa@gmail.com',
    license='MIT',  
    install_requires=[
        "streamlit",
        "python-dotenv",
        "google-cloud-aiplatform"
    ],
    packages=find_packages(),
)


