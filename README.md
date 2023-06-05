# Este é o meu projeto Tech News desenvolvido na Trybe
O Tech News é um web scrapper que busca as notícias do blog da Trybe, e salva em um banco de dados. Você pode pesquisar a notícia usando vários filtros, como tempo de leitura, melhor avaliação, tema, etc.

## Como rodar o projeto
### Para executar este projeto, você vai precisar do python3 instalado na sua maquina

1. Abra o terminal e crie um diretório no local de sua preferência com o comando **mkdir**:
```javascript
  mkdir tech_news
```

2. Entre no diretório que acabou de criar e depois clone o projeto:
```javascript
  cd tech_news
  git clone git@github.com:ViParis0/project-tech-news.git
```

3. Crie o ambiente virtual para o projeto:
```javascript
  cd project-tech-news
  python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependencias do projeto:
```javascript
  python3 -m pip install -r dev-requirements.txt
```
