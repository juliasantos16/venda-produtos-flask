from flask import Flask

from src.models.redis.settings.connection import RedisConnectionHandle
from src.models.sqlite.settings.connection import SqliteConnectionHandle

redis_connection_handle = RedisConnectionHandle()
sqlite_connection_handle = SqliteConnectionHandle()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

from src.main.routes.products_routes import products_routes_bp  # cadastrando rotas

app = Flask (__name__)

app.register_blueprint(products_routes_bp)
