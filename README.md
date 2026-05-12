# Hotel Review Analysis (TripAdvisor)

## Overview

This project performs basic Natural Language Processing (NLP) on hotel reviews to identify commonly used words and generate a word cloud visualisation. The objective is to explore patterns in customer feedback and build a structured, modular data analysis pipeline.

The workflow includes:
- Loading review data from a CSV file
- Cleaning and preprocessing text
- Tokenising and removing stopwords
- Analysing word frequency
- Visualising results using a word cloud

---

## Skills Used

### Programming & Tools
- Python
- pandas
- NLTK (Natural Language Processing)
- matplotlib
- wordcloud
- Git & GitHub

### Data Processing & Analysis
- Data ingestion from CSV files
- Text preprocessing (cleaning, normalisation)
- Tokenisation and stopword removal
- Word frequency analysis
- Grouped analysis (e.g. by region)

### Software Engineering Practices
- Modular project structure (separation of concerns)
- Reusable functions and pipelines
- File-based data persistence (CSV outputs)
- Use of virtual environments
- Version control with Git

### Concepts Demonstrated
- Natural Language Processing (NLP)
- Exploratory Data Analysis (EDA)
- Data pipeline design
- Reproducible workflows

---

## Project Structure

```
hotel-review-analysis/
│
├── data/
│   └── tripadvisor_hotel_reviews.csv
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── analysis.py
│   ├── visualisation.py
│   └── outputs.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. Data Loading
The dataset is loaded from the `data/` directory using a dedicated data loader module.

### 2. Text Cleaning
- Converts all text to lowercase
- Removes punctuation and non-alphabetic characters

### 3. Tokenisation
- Splits text into individual words
- Removes common stopwords (e.g. "the", "and")
- Filters out very short words

### 4. Analysis
- Counts word frequency across all reviews

### 5. Visualisation
- Generates a word cloud highlighting the most frequently used words

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/hotel-review-analysis.git
cd hotel-review-analysis
```

### 2. Create and activate a virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install required packages

```
pip install -r requirements.txt
```

### 4. Download required NLTK data

NLTK requires additional datasets that are not installed via `pip`. Run the following command once:

```
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

---

## Usage

Run the main script:

```
python main.py
```

This will:
- Load the dataset
- Clean and process the text
- Perform word frequency analysis
- Display a word cloud

---

## Dependencies

The main libraries used in this project are:

- pandas
- nltk
- matplotlib
- wordcloud

All dependencies are listed in `requirements.txt`.

---

## Notes

- The dataset file must be placed in the `data/` directory before running the project.
- NLTK data is stored in a global directory (typically `C:\Users\<username>\AppData\Roaming\nltk_data` on Windows).
- The project is designed with modular components to support future expansion.

---

## Future Improvements

- Analyse reviews by region or location
- Add sentiment analysis (positive vs negative reviews)
- Extract common phrases using n-grams (e.g. "friendly staff")
- Export results to Tableau or Power BI
- Integrate with Databricks for scalable processing

---

## Author

Alexander Sainsbury

---

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction. This includes, without limitation, the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

