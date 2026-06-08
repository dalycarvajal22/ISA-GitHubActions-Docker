from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dalyana Carvajal J</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }

            .container {
                max-width: 800px;
                width: 100%;
                background: white;
                border-radius: 24px;
                box-shadow: 0 20px 35px rgba(0, 0, 0, 0.1);
                overflow: hidden;
                text-align: center;
                padding: 2rem;
                transition: transform 0.3s ease;
            }

            .container:hover {
                transform: translateY(-5px);
            }

            h1 {
                font-size: 2.8rem;
                color: #2c3e50;
                margin-bottom: 1rem;
                letter-spacing: 1px;
                border-bottom: 3px solid #3498db;
                display: inline-block;
                padding-bottom: 10px;
            }

            .subtitulo {
                font-size: 1.2rem;
                color: #7f8c8d;
                margin-top: 0.5rem;
                margin-bottom: 2rem;
            }

            .contenido {
                text-align: left;
                background-color: #f9f9fc;
                padding: 1.5rem;
                border-radius: 16px;
                margin-top: 1rem;
            }

            .contenido p {
                font-size: 1rem;
                color: #34495e;
                line-height: 1.6;
                margin-bottom: 1rem;
            }

            .emoji {
                font-size: 3rem;
                margin: 1rem 0;
            }

            footer {
                margin-top: 2rem;
                font-size: 0.8rem;
                color: #95a5a6;
                border-top: 1px solid #ecf0f1;
                padding-top: 1.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">✨</div>
            <h1>Dalyana Carvajal</h1>
            <div class="subtitulo">Bienvenido a mi espacio personal</div>
            <div class="contenido">
                <p>Hola, mi nombre es <strong>Dalyana Carvajal</strong>. Esta es una página web creada con <strong>Python y Flask</strong>.</p>
                <p>Diseñada con HTML5 y CSS básico, se sirve desde el puerto <code>5000</code>.</p>
                <p>💡 Puedes modificar el contenido, colores y estilos fácilmente.</p>
            </div>
            <footer>
                Flask · Puerto 5000 · Dalyana Carvajal
            </footer>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')