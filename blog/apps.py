"""Import app configuration library from django"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Describe the type of app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
