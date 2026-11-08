from flask import Flask  
from db import init_db  
from upload_route import upload_bp  
from download_route import download_bp  
import os  

app = Flask(__name__)  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  

if not os.path.exists(UPLOAD_FOLDER):  
    os.makedirs(UPLOAD_FOLDER)  

init_db()  

app.register_blueprint(upload_bp, url_prefix='/uploads')  
app.register_blueprint(download_bp, url_prefix='/downloads')  

@app.route('/')
def index():
    return {
        "mensagem": "API de upload e download no ar",
        "rotas": {
            "upload": "POST /uploads/upload (campo 'file')",
            "download": "GET /downloads/download/<filename>"
        }
    }


if __name__ == '__main__':
    # Execução local. Em produção o Render usa o gunicorn (ver Procfile).
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)  
