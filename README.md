# 🎰 Simulador de Bets - Caça Níquel Conscientizador

> Um projeto interativo desenvolvido com Flask, HTML e CSS para conscientizar sobre os **malefícios das apostas online**.

---

## 📌 Objetivo

Este projeto simula um caça-níquel com aparência moderna de cassino. Seu propósito **não é incentivar apostas**, mas **mostrar como os jogos de azar manipulam o comportamento do jogador** — começando com ganhos e terminando em perdas totais.

> Ao final, a frase **"Enquanto você tenta recuperar o que perdeu, a casa enriquece."** é exibida, reforçando o alerta.

---
## 🧠 Como funciona
* Começa com R$100 de saldo.

* As primeiras 5 rodadas garantem vitória com símbolos iguais.

* Depois, o jogo força perdas até o saldo zerar.

* Quando o saldo zera, aparece a frase:
"Enquanto você tenta recuperar o que perdeu, a casa enriquece."

---
## Estrutura do projeto:

SimuladorDeBET/
│
├── bet.py
├── templates/
│   └── bet.html
├── static/
│   └── style.css


---
## ⚠️ Aviso
Este projeto é educacional e visa alertar sobre os perigos do vício em jogos de azar e apostas online.
Ele não envolve dinheiro real nem incentiva o uso de plataformas de apostas.

---
## 🚀 Como usar o projeto

Execute os comandos abaixo no seu terminal:

```bash
git clone https://github.com/PandaLoko27/SimuladorDeBETS.git
cd SimuladorDeBETS
python -m venv venv
source venv/bin/activate  # ou: venv\Scripts\activate (no Windows)
pip install flask
python bet.py

depois abra no navegador:
http://127.0.0.1:5000/
````

---


## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Feito com ❤️ por Otávio Guedes
