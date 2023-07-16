import requests
import matplotlib.pyplot as plt
# wb = write in binary


def get_pokemon_data():
    poke_name = input("Enter the name of Pokemon: ")
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(poke_name)
    response = requests.get(url)
    return response.json()


def plot_pokemon_image(received_data):
    url_data = requests.get(received_data["cards"][1]["imageUrl"])
    with open('./poke.png', 'wb') as f:
        for item in url_data.iter_content(1024):
            f.write(item)

    image_data = plt.imread('./poke.png')
    plt.imshow(image_data)
    plt.show()


if __name__ == "__main__":
    received_data = get_pokemon_data()
    plot_pokemon_image(received_data)
