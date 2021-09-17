![PokeDex_Classifier](https://socialify.git.ci/GunjanDhanuka/PokeDex_Classifier/image?description=1&descriptionEditable=Your%20friend%20in%20the%20Kalos%20Region!%20Built%20with%20the%20power%20of%20DenseNet201%20and%20Streamlit!&logo=https%3A%2F%2Fgithub.com%2FGunjanDhanuka%2FPokeDex_Classifier%2Fblob%2Fmaster%2Fgit_images%2Fpokedex.png%3Fraw%3Dtrue&owner=1&pattern=Diagonal%20Stripes&stargazers=1&theme=Light)

**Before moving on the documentation, check out the app live at [here](https://pokedexgd.herokuapp.com/)**

I have always been an avid Pokemon fan and spent a lot of my time on the FireRed and Emerald games :p

![Kanto](git_images/kanto.png)

So after learning about Image Classification using CNNs and about Transfer Learning, this idea of making a real-life PokeDex struck my mind.

## About the Model
The data for training was collected from [this Kaggle Dataset](https://www.kaggle.com/lantian773030/pokemonclassification) and Tensorflow framework was used for Data Augmentation and Model building. 

The model achieved an accuracy of approximately 87% on the test dataset.

Here is an overview of the DenseNet201 Model:
![DenseNet201](git_images/densenet.jpeg).
You can read more about the architecture over [here](https://arxiv.org/pdf/1608.06993).

## About the Application
So after building the model, I wanted to make it to some use for everyone *(and also for some show-off)*. I read about the Streamlit framework that allows you to create beautiful apps for your ML/DL projects. 

Then I deployed the model on Heroku as it is a popular free choice for us students and is reasonably good for the use-case.

### Future additions:
- Add more verbosity to the model.
- Print images of Pokemon in the results.
- Work on the theme of the app.


*Feel free to give suggestions or point out flaws in the application. I am only learning and would love to make this better.*