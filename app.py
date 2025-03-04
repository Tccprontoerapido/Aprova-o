from flask import Flask, render_template
app = Flask(__name__)

class AprovaçãoSaladeEstudos:
    def __init__(self):
        self.nome = "Aprovação Sala de Estudos"
        self.endereco = ""
        self.telefone = "5581997064169"
        self.email = "contato@example.com"
        self.site = "https:///"
        self.horários = {
            "manha": "06h/12h",
            "tarde": "12h/18h",
            "noite": "18h/00h",
        }
        self.planos = {
            "um_turno": {
                "seg_a sex": "100",
                "sab_e_dom": "150",
                "todos_os_dias": "200",
            },
            "dois_turnos": {
                "seg_a_sex": "180",
                "sab_e_dom": "250",
                "todos_os_dias": "300",
            },
            "tres_turnos": {
                "seg_a_sex": "250",
                "sab_e_dom": "350",
                "todos_os_dias": "400",
            },
        }

@app.route('/')
def index():
    sala = AprovaçãoSaladeEstudos()
    return render_template('index.html', sala=sala)

if __name__ == "__main__":
    app.run(debug=True)
