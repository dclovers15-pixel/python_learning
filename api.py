import requests


def main():
    print("welcome to the art search engine")
    artist = input("enter an artist name: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
        content = response.json()
        for artwork in content["data"]:
            print(artwork["title"])
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")


main()
