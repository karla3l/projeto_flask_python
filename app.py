from crypt import methods
from csv import reader
from distutils.log import debug
from flask import Flask, request, render_template

meu_app = Flask(__name__) 

@meu_app.route('/form')
def main():
    return render_template('form.html')



@meu_app.route('/user',methods=['POST'])
def user():
    if request.method == 'POST':
        nome = request.form.get('nome')
    
        return render_template('user.html', nome=nome)
    

if __name__ == '__main__':
     meu_app.run(debug=True) 


""" def main():
    ka=30
    #return '<h2>Retorno da função principal - rota sobre </h2>'
    return render_template('form.html',ka=ka)
    #meu_app.run(debug=True,port=6000)

if request.method=='POST':
    
     #nome = request.form.get('nome')
    try:
        nome['nome'] = request.POST.get('nome')
        novo_nome = Nome.objects.create(**nome)
    except Exception as e:
        mensagem['mensagem_usuario'] = e
    else:
        mensagem['mensagem_usuario'] = "cadastro realizado com sucesso"
        
    return render(request, 'form.html') """

    

   



   