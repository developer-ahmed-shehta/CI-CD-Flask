# CI/CD Flask Application

## Description
A Flask application demonstrating continuous integration and continuous deployment (CI/CD) with GitHub Actions, uWSGI, and Nginx. This project showcases how to set up a Flask app for production deployment and includes performance testing with Apache Benchmark.

## Installation
Follow these steps to install and set up the project:

```sh
# Clone the repository
git clone https://github.com/developer-ahmed-shehta/CI-CD.git

# Navigate to the project directory
cd CI-CD

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
