# Dashboard de Fundos

Protótipo mínimo em Python 3.11 + Dash.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crie o arquivo `.env` baseado em `.env.example`.

## Uso

```bash
python manage.py init-db
python manage.py etl --adm EXEMPLO --start 2024-01-01 --end 2024-01-10
python manage.py run --reload
```

## Testes

```bash
pytest -q
```

