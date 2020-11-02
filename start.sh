pip install -r requirements.txt
python solution.py
docker build -t sol .
docker run -it --publish 8080:8080 sol