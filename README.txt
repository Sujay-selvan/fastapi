"alembic upgrade"
alembic revision --autogenerate -m "create user table"

"push a code like a git push"
alembic upgrade head