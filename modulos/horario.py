import json

class Horario:
    def __init__(self):
        self.horarios = [
            {
                "nomeDoProfessor": "Prof. Christopher",
                "horarioDeAtendimento": "Seg 17:30 - 19:10",
                "periodo": "integral",
                "sala": "5",
                "predio": "1"
            },
            {
                "nomeDoProfessor": "Prof. Jonas",
                "horarioDeAtendimento": "Ter 19:30 - 21:10",
                "periodo": "noturno",
                "sala": "3",
                "predio": "14"
            }
        ]

    def to_json_string(self):
        return json.dumps(self.horarios)

