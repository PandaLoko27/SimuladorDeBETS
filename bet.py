from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'meu-segredo-ultra-seguro'

SALDO_INICIAL = 100
RODADAS_VITORIA_FORCADA = 5
SIMBOLOS = ["🍒", "🍋", "🔔", "🍇", "💎", "7️⃣"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("reset") == "1":
            session.clear()
            return redirect(url_for("index"))

    session.setdefault("saldo", SALDO_INICIAL)
    session.setdefault("rodadas_jogadas", 0)
    session.setdefault("fase_vitoria", True)
    session.setdefault("resultado", ["❓", "❓", "❓"])

    mensagem = ""
    ganho = 0
    aposta = 0

    if request.method == "POST" and not request.form.get("reset"):
        try:
            aposta = int(request.form.get("aposta", 0))
        except:
            aposta = 0

        if aposta <= 0:
            mensagem = "Faça uma aposta válida maior que zero."
        elif aposta > session["saldo"]:
            mensagem = "Você não tem saldo suficiente para essa aposta."
        elif session["saldo"] == 0:
            mensagem = ""
        else:
            session["rodadas_jogadas"] += 1

            if session["fase_vitoria"]:
                # Símbolos iguais para vitória forçada
                simbolo = random.choice(SIMBOLOS)
                resultado = [simbolo, simbolo, simbolo]
                ganho = aposta * 2
                session["saldo"] += ganho
                mensagem = f"🎉 Parabéns! Você ganhou R$ {ganho}!"
                if session["rodadas_jogadas"] >= RODADAS_VITORIA_FORCADA:
                    session["fase_vitoria"] = False
            else:
                # Símbolos aleatórios normais para perda
                resultado = [random.choice(SIMBOLOS) for _ in range(3)]
                perda = aposta
                session["saldo"] -= perda
                ganho = 0
                mensagem = f"😞 Você perdeu R$ {perda}."

            session["resultado"] = resultado

            if session["saldo"] <= 0:
                session["saldo"] = 0
                mensagem = ""  # Tirar mensagem repetida

    return render_template("bet.html",
                           saldo=session["saldo"],
                           mensagem=mensagem,
                           aposta=aposta,
                           resultado=session["resultado"])

if __name__ == "__main__":
    app.run(debug=True)