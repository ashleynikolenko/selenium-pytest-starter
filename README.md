# Selenium + Pytest Starter

This is a starter project for writing automated tests with [Selenium](https://www.selenium.dev/) and [Pytest](https://docs.pytest.org/).

## Setup

Clone this repo and create a virtual environment (optional but recommended):

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python3 -m venv .venv
source .venv/bin/activate   # On Windows use .venv\Scripts\activate
pip install -r requirements.txt
```
## Running Tests
To run all tests:

```bash
pytest -q
```
The included sample test will:



* Open python.org
* Check the page title
* Perform a simple search


selenium-pytest-starter/

│

├── tests/

│   └── test_python_org.py   

├── requirements.txt

└── README.md

