"""Histórico e ranking das batalhas no SQLite."""
import sqlite3
from datetime import date
import arquivos

NOME_ARQUIVO = "arena.db"


def conectar(nome_arquivo=NOME_ARQUIVO):
    conn = sqlite3.connect(nome_arquivo)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jogador TEXT NOT NULL,
            inimigo TEXT NOT NULL,
            resultado TEXT NOT NULL,
            turnos INTEGER NOT NULL,
            vida_restante INTEGER NOT NULL,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def registrar_partida(conn, jogador, inimigo, resultado, turnos, vida_restante, data=None):
    if data is None:
        data = date.today().isoformat()
    cursor = conn.execute(
        """INSERT INTO partidas
        (jogador, inimigo, resultado, turnos, vida_restante, data)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (jogador, inimigo, resultado, turnos, vida_restante, data)
    )
    conn.commit()
    return cursor.lastrowid


def historico(conn, jogador):
    cursor = conn.execute(
        """SELECT id, inimigo, resultado, turnos, vida_restante, data
        FROM partidas WHERE jogador = ? ORDER BY id""",
        (jogador,)
    )
    return cursor.fetchall()


def contar_resultados(conn, jogador):
    contagem = {"vitoria": 0, "derrota": 0, "fuga": 0}
    for linha in historico(conn, jogador):
        resultado = linha[2]
        if resultado in contagem:
            contagem[resultado] += 1
    return contagem


def ranking(conn, limite=5):
    cursor = conn.execute(
        """SELECT jogador, inimigo, turnos, vida_restante
        FROM partidas
        WHERE resultado = 'vitoria'
        ORDER BY vida_restante DESC, turnos ASC
        LIMIT ?""",
        (limite,)
    )
    return cursor.fetchall()


def exportar_ranking(conn, caminho, limite=5):
    lista = []
    for posicao, linha in enumerate(ranking(conn, limite), start=1):
        jogador, inimigo, turnos, vida_restante = linha
        lista.append({
            "posicao": posicao,
            "jogador": jogador,
            "inimigo": inimigo,
            "turnos": turnos,
            "vida_restante": vida_restante
        })
    arquivos.salvar_json(caminho, lista)
    return lista
