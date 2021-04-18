import requests
import tkinter as tk


def getNews():
    api_key = "fdd806b4914d4cb296d57d434d11dfa4"  # enter your own api key
    url = f"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = []
    my_news = "Top 10 news: \n"

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news+f"{i+1}."+" "+my_articles[i]+"\n"

    # print(my_news)
    label.config(text=my_news, bg="cyan", fg="darkOrchid4")


canvas = tk.Tk()
canvas.geometry("1100x600")
canvas.title("News app")
canvas.config(bg="cyan")

button = tk.Button(canvas, font=("ds-digital", 24), text="Reload", command=getNews)
button.config(bg="SeaGreen1")
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

getNews()

canvas.mainloop()
