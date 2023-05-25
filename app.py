from flask import Flask, render_template, request
from requests import get
from flask_babel import Babel, gettext

import os
import requests
import json

app = Flask(__name__)

def get_locale():
    return request.accept_languages.best_match(['fr', 'en'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    content = get('https://tmare.ndelpech.fr/tps/pokemons')
    pokemons=content.json()
    pokemon=get('https://tmare.ndelpech.fr/tps/pokemons/{}'.format(pokemons[150]['id'])).json()
    return pokemon['name']['fr']

@app.route('/maison')
def maison():
    return render_template ('maison.jinja')

@app.route('/poke')
def corp():
    content = get('https://studies.delpech.info/pbi/pokemons/dataset/json')
    pokemons=content.json()
    return render_template ('corp.jinja',pokemons=pokemons)

@app.route('/pokeInfo2/<string:i>')
def pokeInfo2(i):
    content = get('https://studies.delpech.info/pbi/pokemons/dataset/' + i + '/json')

    pokemons=content.json()
    translated_message = gettext(pokemons['description']['fr'])
    translated_name = gettext(pokemons['name']['fr'])
    print(translated_message)
    return render_template ('pagePokemon.jinja',pokemons=pokemons,translate_description=translated_message,translated_name=translated_name)

