import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing
import time
import requests

class_names = ['Abra',
               'Aerodactyl',
               'Alakazam',
               'Alolan Sandslash',
               'Arbok',
               'Arcanine',
               'Articuno',
               'Beedrill',
               'Bellsprout',
               'Blastoise',
               'Bulbasaur',
               'Butterfree',
               'Caterpie',
               'Chansey',
               'Charizard',
               'Charmander',
               'Charmeleon',
               'Clefable',
               'Clefairy',
               'Cloyster',
               'Cubone',
               'Dewgong',
               'Diglett',
               'Ditto',
               'Dodrio',
               'Doduo',
               'Dragonair',
               'Dragonite',
               'Dratini',
               'Drowzee',
               'Dugtrio',
               'Eevee',
               'Ekans',
               'Electabuzz',
               'Electrode',
               'Exeggcute',
               'Exeggutor',
               'Farfetchd',
               'Fearow',
               'Flareon',
               'Gastly',
               'Gengar',
               'Geodude',
               'Gloom',
               'Golbat',
               'Goldeen',
               'Golduck',
               'Golem',
               'Graveler',
               'Grimer',
               'Growlithe',
               'Gyarados',
               'Haunter',
               'Hitmonchan',
               'Hitmonlee',
               'Horsea',
               'Hypno',
               'Ivysaur',
               'Jigglypuff',
               'Jolteon',
               'Jynx',
               'Kabuto',
               'Kabutops',
               'Kadabra',
               'Kakuna',
               'Kangaskhan',
               'Kingler',
               'Koffing',
               'Krabby',
               'Lapras',
               'Lickitung',
               'Machamp',
               'Machoke',
               'Machop',
               'Magikarp',
               'Magmar',
               'Magnemite',
               'Magneton',
               'Mankey',
               'Marowak',
               'Meowth',
               'Metapod',
               'Mew',
               'Mewtwo',
               'Moltres',
               'MrMime',
               'Muk',
               'Nidoking',
               'Nidoqueen',
               'Nidorina',
               'Nidorino',
               'Ninetales',
               'Oddish',
               'Omanyte',
               'Omastar',
               'Onix',
               'Paras',
               'Parasect',
               'Persian',
               'Pidgeot',
               'Pidgeotto',
               'Pidgey',
               'Pikachu',
               'Pinsir',
               'Poliwag',
               'Poliwhirl',
               'Poliwrath',
               'Ponyta',
               'Porygon',
               'Primeape',
               'Psyduck',
               'Raichu',
               'Rapidash',
               'Raticate',
               'Rattata',
               'Rhydon',
               'Rhyhorn',
               'Sandshrew',
               'Sandslash',
               'Scyther',
               'Seadra',
               'Seaking',
               'Seel',
               'Shellder',
               'Slowbro',
               'Slowpoke',
               'Snorlax',
               'Spearow',
               'Squirtle',
               'Starmie',
               'Staryu',
               'Tangela',
               'Tauros',
               'Tentacool',
               'Tentacruel',
               'Vaporeon',
               'Venomoth',
               'Venonat',
               'Venusaur',
               'Victreebel',
               'Vileplume',
               'Voltorb',
               'Vulpix',
               'Wartortle',
               'Weedle',
               'Weepinbell',
               'Weezing',
               'Wigglytuff',
               'Zapdos',
               'Zubat']

fig = plt.figure()

st.title('PokeDex!')
st.subheader("Gotta catch 'em all..")

st.markdown(
    '''This tool will help you identify :the Pokemon you encounter in your way in the **Kanto Region.** *Generation 1.* :jp:
Just click an image :camera: and upload it to see which Pokemon it is.'''
)




def main():
    file_uploaded = st.file_uploader(
        "Choose File", type=["png", "jpg", "jpeg"])
    class_btn = st.button("Classify")
    if file_uploaded is not None:
        image = Image.open(file_uploaded)
        st.image(image, caption='Uploaded Image', use_column_width=True)

    if class_btn:
        if file_uploaded is None:
            st.write("Invalid command, please upload an image")
        else:
            with st.spinner('Model working....'):
                predictions = predict(image)
                time.sleep(1)
                st.success('Classified')
                print_data(predictions)
    st.markdown('## How it works?')
    st.caption('''The model uses Transfer Learning from the DenseNet201 model to classify the images into 150 different classes.
    First the images are resized according to the model input and then using a Softmax layer at the end, we compute the probability of the image to be one of 150 Pokemon. 
The model might have some difficulty in differentiating between evolved forms of a Pokemon for example Pidgeotto and Pidgeot!.''')


def predict(image):
    classifier_model = "model_pokemon.h5"
    IMAGE_SHAPE = (128, 128, 3)
    model = load_model(classifier_model)
    test_image = image.convert("RGB").resize((128, 128))
    test_image = np.array(test_image)
    test_image = test_image / 255.0
    img_array = tf.expand_dims(test_image, 0)

    predictions = model.predict(img_array)
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    highest = scores.argsort()[-5:][::-1]
    result = []
    for i in range(5):
        # result += f"{class_names[highest[i]]} with a { (100 * scores[highest[i]]).round(2) } % confidence."
        # result += '\n'
        result.append(class_names[highest[i]])
        i += 1

    return result, highest


def print_data(pokelist):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    df = pd.DataFrame(data=np.zeros((5, 3)),
                      columns=['Name',  'Type', 'Description'],
                      index=np.linspace(1, 5, 5, dtype=int)
                      )
    i = 0
    for poke in pokelist:
        response = requests.get(url+poke.lower())
        if(response.status_code != 200):
            # st.markdown(f'''1. Pokemon is: **{poke}**\n
            # **Error fetching data for Pokemon from the API. Please try again later**
            # ''')
            df.iloc[i, 0] = poke
            df.iloc[i, 1] = 'Error fetching data from API'
            df.iloc[i, 2] = 'Error fetching data from API'

        else:
            jresponse = response.json()
            type = jresponse['types'][0]['type']['name']
            species_url = jresponse['species']['url']
            species_response = requests.get(species_url)
            species_response = species_response.json()
            description = ''
            for d in species_response['flavor_text_entries']:
                if d['language']['name'] == 'en':
                    description = d['flavor_text']
                    break
            df.iloc[i, 0] = poke.capitalize()
            df.iloc[i, 1] = type.capitalize()
            df.iloc[i, 2] = description.replace('\n', ' ')
        i += 1

    st.title("Here are the five most likely Pokemons")
    st.caption("in decreasing order of confidence..")
    st.write(df.to_html(escape=False), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
