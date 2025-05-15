# Dockerfile
FROM python:3.9

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements.txt et installer les dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . /app/

# Exposer le port 8080
EXPOSE 8080

# Commande par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
