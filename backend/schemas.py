# schemas.py - Define os modelos de dados que a API espera receber ou enviar

from pydantic import BaseModel  # BaseModel permite criar classes que validam os dados automaticamente
from datetime import date  # Importa o tipo de dado 'date' para uso nas classes

# Modelo de dados para registro de jogatina
class Jogatina(BaseModel):
    jogo: str  # Nome do jogo
    duracao_em_minutos: int  # Tempo da sessão de jogo em minutos
    humor_antes: str  # Estado emocional antes de jogar
    humor_depois: str  # Estado emocional depois de jogar
    data: date  # Data em que a jogatina ocorreu

# Modelo de dados para registro de tarefa ou estudo
class Tarefa(BaseModel):
    tipo: str  # Tipo da tarefa (ex: estudo de Python, leitura)
    duracao_em_minutos: int  # Tempo gasto na tarefa
    produtividade: str  # Nível de produtividade percebido (baixa, média, alta)
    data: date  # Data da tarefa