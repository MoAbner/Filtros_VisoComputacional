from flask import Flask, render_template, request
import base64
import cv2
import numpy as np
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def extensao_permitida(nome_arquivo):
    return (
        "." in nome_arquivo and
        nome_arquivo.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/", methods=["GET", "POST"])
def index():
    imagens = False
    erro = None
    sobel_b64 = None
    laplaciano_b64 = None
    canny_b64 = None

    if request.method == "POST":
        arquivo = request.files.get("imagem")

        if not arquivo or arquivo.filename == "":
            erro = "Nenhum arquivo foi selecionado."

        elif not extensao_permitida(arquivo.filename):
            erro = "Arquivo recusado. Envie apenas imagens PNG ou JPG."

        else:
            dados = arquivo.read()
            imagem_buffer = np.frombuffer(dados, np.uint8)
            imagem = cv2.imdecode(imagem_buffer, cv2.IMREAD_GRAYSCALE)

            if imagem is None:
                erro = "O arquivo enviado não é uma imagem válida."
            else:
                sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
                sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
                sobel = np.uint8(np.sqrt(sobel_x**2 + sobel_y**2))

                laplaciano = np.uint8(
                    np.absolute(cv2.Laplacian(imagem, cv2.CV_64F))
                )

                canny = cv2.Canny(imagem, 100, 200)

                _, sobel_png = cv2.imencode(".png", sobel)
                _, laplaciano_png = cv2.imencode(".png", laplaciano)
                _, canny_png = cv2.imencode(".png", canny)

                sobel_b64 = base64.b64encode(sobel_png).decode("ascii")
                laplaciano_b64 = base64.b64encode(laplaciano_png).decode("ascii")
                canny_b64 = base64.b64encode(canny_png).decode("ascii")

                imagens = True

    return render_template(
        "index.html",
        imagens=imagens,
        erro=erro,
        sobel_b64=sobel_b64,
        laplaciano_b64=laplaciano_b64,
        canny_b64=canny_b64,
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

