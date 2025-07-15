# order/test/conftest.py

import os
import django

# Define onde está o módulo de configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")

# Inicializa o Django para que ele reconheça os apps e models
django.setup()
