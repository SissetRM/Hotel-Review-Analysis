from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Finds the appropriate path for the file to be output to.
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_wordcloud(tokens_series, title="Word Cloud"):
    """
    Generates a word cloud of the most common words used in reviews.
    :param tokens_series: A pandas series of strings containing words from the reviews.
    :param title: String
    :return: None
    """
    # Converts the pandas series into a long string of text.
    text = " ".join([" ".join(tokens) for tokens in tokens_series])

    # Sets the dimensions fo the words cloud and the colour then generate it from the text.
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Sets the figure dimensions and title.
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)

    # Save image
    file_path = OUTPUT_DIR / title
    plt.savefig(file_path)

    # Shows the image on screen.
    plt.show()
