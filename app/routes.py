from flask import Blueprint, request, render_template
from .utils import caesar_encrypt, caesar_decrypt

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        shift = int(request.form.get('shift'))
        choice = request.form.get('choice')
        
        if choice == 'encrypt':
            result = caesar_encrypt(text, shift)
        elif choice == 'decrypt':
            result = caesar_decrypt(text, shift)
    
    return render_template('index.html', result=result)
