# Use a imagem base do Python
FROM python:3.12.5-slim

# Defina o diretório de trabalho
WORKDIR /projeto-flask 

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta que a aplicação irá rodar
EXPOSE 3001

# Comando para rodar a aplicação
CMD ["python", "appflask.py"]
