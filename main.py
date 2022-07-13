from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
  
@app.route('/cardapio')
def cardapio(): 
    return render_template('cardapio.html', promoçao =False)
    arquivo = open("static/pizza.json")
    pizzas = json.load(arquivo)
    return render_template('cardapio.html', promocao = False, pizzas = pizzas)
@app.route( '/avaliacoes')
def avaliacoes():
     clientes = [ 
       {'nome':'Cristiano Ronaldo', 'nota': 5 } , 
       {'nome':'Messi', 'nota': 2 }, 
       {'nome':'Sharapova', 'nota': 3},
       {'nome':'Serena', 'nota': 4 },
       {'nome': 'Neymar', 'nota': 5 },
     ]
     return render_template('avaliacoes.html', clientes = clientes)
 
@app.route('/faleconosco.html')
def faleconosco():
    return render_template('faleconosco.html')
  
@app.route('/login')
def login():
    return render_template('login.html')

 
app.run(host='0.0.0.0', port=81)