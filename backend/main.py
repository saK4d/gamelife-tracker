from fastapi import FastAPI  # Importa o FastAPI para criar a API
from backend.db.database import database  # Importa o objeto de conexão com o banco de dados
from backend.models import jogatina, tarefa, metadata  # Importa as tabelas do banco definidas no models.py
from backend.schemas import Jogatina, Tarefa  # Importa os modelos de dados (validação) do schemas.py
from datetime import date, timedelta  # Importa tipos de data e manipulação de tempo
from collections import Counter  # Importa contador para contar repetições (como humor ou dias de atividade)

app = FastAPI(title="GameLife Tracker")  # Cria a instância da aplicação FastAPI com um título personalizado

# Evento que é executado quando a aplicação é iniciada
@app.on_event("startup")
async def startup():
    await database.connect()  # Conecta ao banco de dados

# Evento que é executado quando a aplicação é finalizada
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()  # Desconecta do banco de dados

# Rota inicial de teste para verificar se a API está funcionando
@app.get("/")
async def root():
    return {"message": "GameLife Tracker funcionando!"}  # Retorna uma mensagem simples

# Rota POST para registrar uma sessão de jogo
@app.post("/jogatina")
async def registrar_jogatina(entry: Jogatina):
    # Prepara a query de inserção no banco com os dados recebidos
    query = jogatina.insert().values(
        jogo=entry.jogo,
        duracao_em_minutos=entry.duracao_em_minutos,
        humor_antes=entry.humor_antes,
        humor_depois=entry.humor_depois,
        data=entry.data
    )
    last_record_id = await database.execute(query)  # Executa a inserção e armazena o ID do último registro inserido
    return {**entry.dict(), "id": last_record_id}  # Retorna os dados enviados + o ID salvo

# Rota GET para listar todas as sessões de jogatina salvas
@app.get("/jogatina")
async def listar_jogatinas():
    query = jogatina.select()  # Cria a query para selecionar todos os registros da tabela jogatina
    results = await database.fetch_all(query)  # Executa a consulta
    return results  # Retorna os registros encontrados

# Rota POST para registrar uma tarefa ou estudo
@app.post("/tarefa")
async def registrar_tarefa(entry: Tarefa):
    query = tarefa.insert().values(
        tipo=entry.tipo,
        duracao_em_minutos=entry.duracao_em_minutos,
        produtividade=entry.produtividade,
        data=entry.data
    )
    last_record_id = await database.execute(query)  # Executa a inserção e retorna o ID
    return {**entry.dict(), "id": last_record_id}  # Retorna os dados salvos com o ID

# Rota GET para listar todas as tarefas registradas
@app.get("/tarefa")
async def listar_tarefas():
    query = tarefa.select()  # Seleciona todos os registros da tabela tarefa
    results = await database.fetch_all(query)  # Executa a consulta
    return results  # Retorna os registros encontrados

# Rota GET para gerar um relatório semanal baseado nas datas dos registros
@app.get("/relatorio/semana")
async def gerar_relatorio_semanal():
    hoje = date.today()  # Pega a data de hoje
    inicio_semana = hoje - timedelta(days=hoje.weekday())  # Calcula a segunda-feira da semana atual
    fim_semana = inicio_semana + timedelta(days=6)  # Calcula o domingo da mesma semana

    # Query para buscar jogatinas na semana
    query_jogatina = jogatina.select().where(jogatina.c.data.between(inicio_semana, fim_semana))
    # Query para buscar tarefas na semana
    query_tarefa = tarefa.select().where(tarefa.c.data.between(inicio_semana, fim_semana))

    # Executa as queries
    jogatinas = await database.fetch_all(query_jogatina)
    tarefas = await database.fetch_all(query_tarefa)

    # Soma o tempo jogado e estudado
    total_jogado = sum([j["duracao_em_minutos"] for j in jogatinas])
    total_estudo = sum([t["duracao_em_minutos"] for t in tarefas])

    # Conta os humores pós-jogo
    humores = Counter([j["humor_depois"] for j in jogatinas])

    # Conta em quais dias teve mais atividade
    dias_jogo = Counter([str(j["data"]) for j in jogatinas])
    dias_estudo = Counter([str(t["data"]) for t in tarefas])

    # Retorna o relatório com os dados processados
    return {
        "semana": f"{inicio_semana} até {fim_semana}",
        "tempo_total_jogado": total_jogado,
        "tempo_total_estudado": total_estudo,
        "humores_apos_jogatina": humores,
        "dias_mais_jogo": dias_jogo.most_common(3),
        "dias_mais_estudo": dias_estudo.most_common(3)
    }
