# nltk-learn

## Quickstart

for solution.py script only that produces ./processed/data.csv:

```sh
pip install -r requirements.txt
python solution.py
```

with pipenv

```sh
pipenv install
pipenv shell
python solution.py
# or
jupyter notebook
```

### Table from another project

To run script, build react app with table & serve it and data from flask in docker container

```sh
./start.sh
```

## Motivation

Produce list of the most frequent interesting words and summary table showing where they appear.

* Making a dictionary of the top 150 most frequent interesting words, mapping them back to their orignial sentences and storing them as CSV & JSON
* Left arrays/lists inside csv to preserve commas
* was going to do tf-idf, but it wouldn't have shown most frequent words/outside of scope

### React Table on Flask

> Added React table from another project, hosted on Flask with word filtering and sorting on different fields

Needs data.json from solution.py in ./flask-server in order to initialize db. To run:

```sh
docker build -t sol .
docker run -it --publish 8080:8080 sol
```
