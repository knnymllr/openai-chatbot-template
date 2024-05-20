# System Prompt Chatbot Template

This is a simple example of a chatbot application built with [Django](https://docs.djangoproject.com/en/5.0/) for storing conversations between a user and a chatbot. The chatbot accepts a customizable system prompt to limit the scope of the chatbot's answers on a particular subject. It was developed for the purposes of research and was designed with local hosting in mind. 

**OPENAI IS NOT HIPAA COMPLIANT. SEE AZURE REPOSITORY. SEE CHANNELS VERSION**

User registration is not forward facing and can only be performed by a superuser in the admin panel. User accounts are created by researcher and distributed to participants.  

## Virtual Environment

1) Create virtual environment in Root directory

- Format: `[py/python3/python] -m venv .{venv_name}`
- Example (PowerShell): `python -m venv .myvenv`

2) Activate virtual environment
   
- PowerShell: `.myvenv\Scripts\activate.ps1`
- Windows Command Prompt: `cd myvenv\Scripts; activate`
- Linux/macOS: `source myvenv/bin/activate`

3) Install from requirements.txt

- `pip install -r requirements.txt`
  
## Adding packages

Don't forget to update requirements.txt!

- `pip freeze > requirements.txt`

## Localhost

- `cd application`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`