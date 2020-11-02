# nltk-learn

> Data discovery/initial work in solution.ipynb, cleaned in solution.py - both produce .csv & .json

## Motivation

Produce list of the most frequent interesting words and summary table showing where they appear.

* Making a dictionary of the top 150 most frequent interesting words, mapping them back to their orignial sentences and storing them as CSV & JSON
* Left arrays/lists inside csv to preserve commas
* was going to do tf-idf, but it wouldn't have shown most frequent words/outside of scope
* removed some frequent words while removing punctuation

## Quickstart

for solution.py script only:

```sh
pip install -r requirements.txt
python solution.py
# data in ./processed/data.csv
```

with pipenv

```sh
pipenv install
pipenv shell
python solution.py
# data in ./processed/data.csv
# or run jupyter
jupyter notebook
```

### Table from another project

> Added a React table with word filtering and sorting on different fields from another project; hosted on Flask

To run script, build react app with table & serve it and data from flask in docker container

```sh
./start.sh
# it will be listening at http://localhost:8080
# Needs data.json from solution.py in ./flask-server
```

### To build react & flask container after generating word frequency

Needs data.json from solution.py in ./flask-server in order to initialize db. To run:

```sh
docker build -t sol .
docker run -it --publish 8080:8080 sol
# it will be listening at http://localhost:8080
```
