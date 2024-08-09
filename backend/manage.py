#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

# Calculate the project root directory (one level up from manage.py)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root directory to sys.path
sys.path.append(project_root)


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_course.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
