pip install uvicorn
pip install fastapi
pip install pydantic
pip install pydantic[email]

alembic revision --autogenerate -m "****"

alembic upgrade head

python main.py
