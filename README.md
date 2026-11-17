# Python no mundo do RPG

Projeto didático dividido em três etapas: combate por turnos, loja com persistência JSON e arena com histórico/ranking SQLite.

## Requisitos
- Python 3.10 ou superior
- Nenhuma biblioteca externa

## Como testar
Execute na pasta do projeto:

```bash
python testes_ex1.py
python testes_ex2.py
python testes_ex3.py
```

Resultado esperado: 16/16, 11/11 e 8/8 testes aprovados, respectivamente.

## Como executar
- `python batalha.py` — demonstração da batalha
- `python main.py` — loja do herói; salva os dados em `heroi.json`
- `python arena.py` — arena; registra partidas em `arena.db`

Para usar a arena pela primeira vez, execute a loja e saia pela opção 0 para criar `heroi.json`. Os arquivos `batalha.py` e `arquivos.py` já estão na mesma pasta do projeto.

Os arquivos `heroi.json` e `arena.db` são criados durante a execução e não fazem parte do repositório.
