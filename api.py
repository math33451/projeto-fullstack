from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/media/')
def media():
    primeiraNota = request.args.get('nota1')
    segundaNota = request.args.get('nota2')

    media = (float(primeiraNota) + float(segundaNota))/2

    if media < 4:
        resultado = 'Reprovado'
    elif media >= 4 and media < 7:
        resultado = 'Recuperação'
    else:
        resultado = 'Aprovado'
    return render_template('notas.html')


if __name__ == '__main__':
    app.run(debug=True)