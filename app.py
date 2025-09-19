from dash import Dash

from src.layout import layout
from src.callbacks import get_callbacks


def create_app():
    app = Dash(
        __name__,
        title='SVD-visualizer',
        suppress_callback_exceptions=True
    )

    app.layout = layout()

    get_callbacks(app)

    return app


def main():
    app = create_app()
    app.run()


if __name__ == '__main__':
    main()