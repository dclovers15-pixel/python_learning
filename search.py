import requests


def main():
    artwork = input("enter an artwork name: ")
    artworks = get_artworks(query=artwork, limit=5)
    for artwork in artworks:
        print(artwork)


def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        content = response.json()
        return [artwork["title"] for artwork in content["data"]]
    except requests.HTTPError:
        return []
print("Error: Unable to fetch artworks from the API.")


main()