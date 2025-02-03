class Docente:
    def __init__(self, nome, matricula, departamento, creditos, iea, email):
        self.nome = nome
        self.matricula = matricula
        self.departamento = departamento
        self.creditos = creditos
        self.iea = iea
        self.email = email

    def apresentar(self):
        return (f"Nome: {self.nome}\n"
            f"Matrícula: {self.matricula}\n"
            f"Departamento: {self.departamento}\n"
            f"Credito: {self.creditos}\n"
            f"IEA: {self.iea}\n"
            f"E-mail: {self.email}")
        
class main:
    print(Docente)
        