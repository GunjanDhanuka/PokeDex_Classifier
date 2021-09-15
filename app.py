import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing
import time

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

with open("custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title('Pokemon Classifier')

st.markdown("Welcome to this simple web application that classifies bags. The bags are classified into six different classes namely: Backpack, Briefcase, Duffle, Handbag and Purse.")


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
                st.write(predictions)


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
    # results = {
    #     'Backpack': 0,
    #     'Briefcase': 0,
    #     'Duffle': 0,
    #     'Handbag': 0,
    #     'Purse': 0
    # }
    # print(scores*100)
    # st.success(class_names[np.argmax(scores)])
    result = ''
    for i in range(5):
        result += f"{class_names[highest[i]]} with a { (100 * scores[highest[i]]).round(2) } % confidence."
        result += '\n'
        i+=1
    
    return result


if __name__ == "__main__":
    main()