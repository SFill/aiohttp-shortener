from shortener.utils.pg import setup_pg, config as default_config
from shortener.api import HANDLERS
from shortener.api.error_callback import error_handler
from aiohttp.web_app import Application
from aiohttp_apispec import validation_middleware, setup_aiohttp_apispec


def create_app(config=None) -> Application:
    app = Application(
        middlewares=[validation_middleware]
    )
    app['config'] = config or default_config
    app.cleanup_ctx.append(setup_pg)

    for handler in HANDLERS:
        app.router.add_route('*', handler.URL_PATH, handler)

    setup_aiohttp_apispec(app=app, title='API',
                          swagger_path='/', error_callback=error_handler)
    return app
