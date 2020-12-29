import requests
from flask import Flask, render_template, request, redirect

app = Flask("HackerNews")

@app.route('/')
def home():
  order_by = request.args.get('order_by')

  if order_by == None:
    noticias = requests.get('https://hn.algolia.com/api/v1/search?tags=story').json()
    return render_template('index.html', noticias=noticias, order_by=order_by)

  elif order_by == 'new':
    noticias = requests.get('https://hn.algolia.com/api/v1/search_by_date?tags=story').json()
    return render_template('index.html', noticias=noticias, order_by=order_by)

  elif order_by == 'popular':
    noticias = requests.get('https://hn.algolia.com/api/v1/search?tags=story').json()
    return render_template('index.html', noticias=noticias, order_by=order_by)

  else:
    return redirect('/')

  return render_template('index.html')



@app.route('/<id>')
def func(id):
  c = requests.get('https://hn.algolia.com/api/v1/items/' + id).json()
  comentarios = c['children']
  return render_template('id.html', comentarios=comentarios, c = c)

app.run(host='0.0.0.0')

