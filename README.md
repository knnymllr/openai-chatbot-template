# OpenAI Chatbot Template

This is a simple example of a chatbot application built with [Django](https://docs.djangoproject.com/en/5.0/) for storing conversations between a user and a chatbot. The chatbot accepts a customizable system prompt to limit the scope of the chatbot's answers on a particular subject. It was developed for the purposes of research and was designed with local hosting in mind. 

**OPENAI IS NOT HIPAA COMPLIANT.** See [Azure template](https://github.com/knnymllr/azure-chatbot-template). See [Channels template](https://github.com/knnymllr/channels-chatbot-template).

User registration is not forward facing and can only be performed by a superuser in the admin panel. User accounts are created by researcher and distributed to participants.  

## Virtual Environment

1) Create virtual environment in Root directory

- Format: `[py/python3/python] -m venv .{venv_name}`
- Example (PowerShell): `python -m venv .myvenv`

2) Activate virtual environment
   
- PowerShell: ```.myvenv\Scripts\activate.ps1```
- Windows Command Prompt: ```cd .myvenv\Scripts; activate```
- Linux/macOS: ```source .myvenv/bin/activate```

3) Install from requirements.txt

- ```pip install -r requirements.txt```

4) Update requirements.txt after ```pip install...```
- ```pip freeze > requirements.txt```

## Localhost

### First time
1) ```cd application```
2) ```python manage.py migrate```
3) ```python manage.py createsuperuser```
4) ```python manage.py runserver```

### Run Application
1) ```cd application```
2) ```python manage.py runserver```
3) Styles bug?? 
   - Press `ctrl`+`f5` or `ctrl`+`fn`+`f5` to reload styles cookies

### Changed Models?
1) ```cd application```
2) ```python manage.py makemigrations```
3) ```python manage.py migrate```
4) ```python manage.py runserver```

## Guidelines and Limitations

Add your API key on line 10 in `.\application\chat\views.py`. Edit the system prompt on line 16. Switch between Davinci and GPT-4 on lines 84/85.

Install SQLiteViewer extension (VSCode) to view database in IDE. You can also view Learn_Session and Learn_Message entries in the [Admin Panel](http://127.0.0.1:8000//admin).

## Further Improvements

- Django REST Framework for more complex model querying
- Store API Key in .env for easier local dev
- Store prompts in .json file for easy swaps or combinations
