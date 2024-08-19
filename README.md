# Article Recommendation System

This script reads a dataset of articles, computes the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) between them, and provides recommendations based on this similarity.

## Features

- **Input**: A CSV file (data.csv) containing articles with at least two columns: Title and Article.
- **Output**: The script appends a new column, Recommended Articles, which contains a list of recommended articles for each article in the dataset.

## Usage

```
# install packages
pip install -r requirements.txt

# run the script
python main.py
```

## Note

1. The script assumes that data.csv is encoded in latin1.
2. Ensure that the Article column contains meaningful text for accurate recommendations.
