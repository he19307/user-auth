from quart import Quart, g
from .config import Config
from .auth.routes import bp as auth_bp
from quart_auth import QuartAuth
from quart_rate_limiter import RateLimiter
import os

auth_manager = QuartAuth()
rate_limiter = RateLimiter()

def create_app():
    """Create and configure the Quart application."""
    
    # Create the app instance
    app = Quart(__name__)
    
    # Use environment variables for configuration
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "awe3rwasfasf"),
        MONGODB_SETTINGS={
            "db": os.environ.get("DB_NAME", "your_default_db_name"),
            "host": os.environ.get("DB_HOST", "localhost"),
            "port": int(os.environ.get("DB_PORT", 27017)),
            "username": os.environ.get("DB_USERNAME", ""),
            "password": os.environ.get("DB_PASSWORD", ""),
            "authentication_source": os.environ.get("DB_AUTH_SOURCE", "admin"),
        },
    )

    auth_manager.init_app(app)
    rate_limiter.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

if __name__ == "__main__":
    app = create_app()
    
    # Use Gunicorn as the production-ready server
    # Example command: gunicorn -w 4 -k uvicorn.workers.UvicornWorker yourapp:app
    app.run(debug=True, host='0.0.0.0', port=8080)

