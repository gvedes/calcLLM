# Calculadora de Compatibilidade para LLMs

Projeto Django para verificar compatibilidade de modelos de linguagem com hardware local.

## Como rodar

1. Clone o repositório
2. Crie e ative um ambiente virtual:
   ```
   python -m venv env
   env\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install django
   ```
4. Execute as migrações:
   ```
   python manage.py migrate
   ```
5. Inicie o servidor:
   ```
   python manage.py runserver
   ```

## Cadastro de modelos e configurações

Acesse `/admin` para cadastrar novos modelos LLM e configurações de hardware.

---