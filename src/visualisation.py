from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(tokens_series, title="Word Cloud"):
    text = " ".join([" ".join(tokens) for tokens in tokens_series])

    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.show()
