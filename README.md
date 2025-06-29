# Python data processing

## Courses Context
I decided to enroll into 2-pack course of data processing with Python. When I took this courses I already had almost 10 years of experience with Python as programming language since my days at University of Santiago. Also, I had some work experience with Python in my prevoius jobs. 

As a Software Engineer with Computer Sciense formation through this courses I could revisit again the fundamentals of Python and basic and intermediate data analysis.

### Course 1: Python programming tools for data processing

Course goal: Learn and apply basic programming tools focused in data processing

### Course 2: Python for data handling: intermediate

Course goal: Learn and apply advanced data processing tools and techniques in professional environments. Gather skills to facilitate analysis tasks completion and problem solving.

## What to expect from this repo?
In this repository you will find exercises made in the context of my 2 courses.

You will find all the instructions to clone, run the environment and check the results of the basic and intermediate exercises of the course.

## Skills

- Programming (codding) in Python language
- Use of basic and advanced mathematical tools and techniques to process data
- Critical thinking to transform data into information
- Gather knowledge from the resulting information transformation process
- Solve problems with real world data

## Instructions to check results

### Run Jupiter Notebook from Github
You can browse and read the notebooks directly on GitHub. Jupyter notebooks are rendered automatically and you will see code, outputs, and visualizations.

Access /notebooks folder and select the desired noteebok with ```*.ipynb``` extension. **You should be able to read every description and run every codeblock inside the notebook directly from the Github interface**.


> Note: You won't be able to run or modify the code this way.

### Run Jupyter Notebook from local Jupyter Server

#### Pre requirements

Make sure you have installed:
- ```python``` (I used ```pyenv 2.6.3``` to install global version of ```python 3.12.11```)


#### Instructions

1. Clone this repository and checkout into ```main``` branch.
  ```bash
  git clone https://github.com/neolivaresgonzalez/data-science-with-python-course.git
  git checkout -b main
  cd data-science-with-python-course
  ```
2. (Recommended) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run Jupyter Notebook Server
```bash
jupyter notebook
```
1. Access to browser into ```https://localhost:8888```. **You should be able to read every description and run every codeblock inside the notebook directly from the deployed interface**.


### Run Jupyter Notebook from Visual Studio Code

#### Pre requirements

Make sure you have installed:
- [Visual Studio Code](https://code.visualstudio.com/Download)
- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

#### Instructuons

1. Clone this repository and checkout into ```main``` branch.
  ```bash
  git clone https://github.com/neolivaresgonzalez/data-science-with-python-course.git
  git checkout -b main
  cd data-science-with-python-course
  ```

2. Open any .ipynb notebook and select the appropriate Python interpreter (e.g., Python 3.12.11 from pyenv or virtual environment). **If you created your own virtual environment you could select it in this step**

3. Run cells interactively within VS Code. **You should be able to read every description and run every codeblock inside the notebook directly from the Visual Studio interface**.





