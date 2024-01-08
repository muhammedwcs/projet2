import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.title('Analyse de corrélation et de distribution des données de voitures')


# Afficher les données brutes
st.header('Données brutes')
st.write(df_cars)

# Analyse de corrélation
st.header('Analyse de corrélation')
correlation = df_cars.corr()
st.write('Matrice de corrélation :')
st.write(correlation)

# Visualisation de la matrice de corrélation avec heatmap
st.write('Heatmap de la matrice de corrélation :')
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()

# Analyse de distribution
st.header('Analyse de distribution')
st.write('Pairplot pour visualiser les relations et distributions :')
pairplot = sns.pairplot(df_cars)
st.pyplot(pairplot)

# Graphiques de distribution pour chaque colonne 
st.write('Graphiques de distribution :')
for column in df_cars.select_dtypes(include='number').columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df_cars[column], kde=True)
    plt.title(f'Distribution de {column}')
    plt.xlabel(column)
    plt.ylabel('Fréquence')
    st.pyplot()

# Commentaires
st.header('Commentaires')
st.write('L\'analyse de corrélation met en évidence les relations entre les variables.')
st.write('Le pairplot permet de visualiser les relations et distributions des variables.')
st.write('Les graphiques de distribution montrent la répartition des valeurs pour chaque variable.')



st.title('Filtrage des données par région')

# Créer des boutons pour filtrer par région
region = st.radio('Sélectionner une région :', ('US', 'Europe', 'Japan', 'Toutes'))

if region == 'Toutes':
    st.write("Affichage des voitures de toutes les régions :")
    st.write(df_cars)
else:
    filtered_data = df_cars[df_cars['continent'] == region]
    st.write(f"Affichage des voitures de la région {region} :")
    st.write(filtered_data)
