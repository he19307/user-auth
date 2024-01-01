from quart import Quart
from .config import Config  # Import configuration
#from app.auth import routes  # Import the `routes` module from the `auth` package
from .auth.routes import bp as auth_bp
from quart_auth import  QuartAuth
from quart_rate_limiter import RateLimiter, limit_blueprint


auth_manager = QuartAuth()
rate_limiter = RateLimiter()

def create_app():
    """Create and configure the Quart application."""
    
    # Create the app instance
    app = Quart(__name__)
    
    
    app.secret_key = "awe3rwasfasf"  # Do not use this key
    auth_manager.init_app(app)
    rate_limiter.init_app(app)
    # Load configuration from the config module
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
      # Initialize auth after app creation

    #app.register_blueprint(routes.bp)  # Assuming a routes.py file exists

    
    return app

if __name__ == "__main__":
    app = create_app()
    
    app.run(debug=True, host='0.0.0.0', port=8080)

