import flask
from flask import Flask, render_template
from apimercadopago import create_payment
app = Flask(__name__)


@app.route('/')
def homepage():
    link_iniciar_pagamento = create_payment()
    return render_template('index.html', link_pagamento=link_iniciar_pagamento)

@app.route('/compracerta')
def about_page():
    return render_template('download.html')
@app.route('/compraerrada')
def contact_page():
    return render_template('compraerrada.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
