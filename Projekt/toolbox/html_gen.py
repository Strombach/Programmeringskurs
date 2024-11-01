from bs4 import BeautifulSoup

def main():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.title.string
    print(f"Title of the page: {title}")

if __name__ == "__main__":
    main()
