# projeto-flask
Projeto novo depois da formatação do desktop


Resumo para README.md
# Projeto Flask

Este projeto é uma aplicação Flask que serve um arquivo `index.html` na porta 3001.

## Estrutura do Projeto


c:/projetos/projeto-flask/ 
│ 
├── site/ 
│ └── index.html 
│ 
├── app.py 
├── Dockerfile 
├── requirements.txt 
└── .github/ 
    └── workflows/ 
        └── docker-image.yml


## Configuração do Ambiente Virtual

1. Crie o ambiente virtual:
   ```bash
   cd c:/projetos/projeto-flask
   python -m venv venv

Ative o ambiente virtual:
No Windows:
venv\Scripts\activate

No Unix ou MacOS:
source venv/bin/activate

Instale o Flask:
pip install flask

Gere o arquivo requirements.txt:
pip freeze > requirements.txt

Docker
Construa a imagem Docker:
docker build -t seu-usuario/projeto-flask .

Teste a aplicação localmente:
docker run -p 3001:3001 seu-usuario/projeto-flask

Envie a imagem para o DockerHub:
docker push seu-usuario/projeto-flask

GitHub Actions
Crie o arquivo .github/workflows/docker-image.yml:
name: Docker Image CI

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Login to DockerHub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: seu-usuario/projeto-flask:latest

Adicione as credenciais do DockerHub no GitHub:
Vá para Settings > Secrets no repositório GitHub.
Adicione DOCKER_USERNAME e DOCKER_PASSWORD.
Trivy e SonarCloud
Instale o Trivy:
brew install aquasecurity/trivy/trivy

Escaneie a imagem Docker:
trivy image seu-usuario/projeto-flask

Configure o SonarCloud:
Crie uma conta no SonarCloud.
Adicione o repositório ao SonarCloud.
Gere um token e adicione como segredo no GitHub (SONAR_TOKEN).
Adicione a análise ao GitHub Actions:
- name: SonarCloud Scan
  uses: SonarSource/sonarcloud-github-action@v1
  with:
    projectKey: seu-usuario_projeto-flask
    organization: seu-usuario
    token: ${{ secrets.SONAR_TOKEN }}

    