from flask_babel import Babel, gettext

babel = Babel()


def supportMultilingual(app):
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits. The best match wins.
        return request.accept_languages.best_match(['en', 'es', 'de', 'fr'])

    @app.route('/')
    def index():
        return gettext('Hello, world!')
