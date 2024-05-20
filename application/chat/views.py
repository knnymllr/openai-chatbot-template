from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Chat_Message, Chat_Session
import openai

openai_api_key = ''
openai.api_key = openai_api_key

SYSTEM_PROMPT = "I only want to talk about tabletop board games."
PREV_RESPONSE = ""
SYSTEM_PROMPT_SENT = False

def ask_davinci(message):
    response = openai.completions.create(
        model='davinci-002',
        prompt=message,
        temperature=1,         
        max_tokens=256,         
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answer = response.choices[0].text.strip()
    return answer


def ask_chatgpt(message):
    global SYSTEM_PROMPT_SENT, PREV_RESPONSE
    if not SYSTEM_PROMPT_SENT:
        # @see https://platform.openai.com/docs/api-reference/chat/create
        response = openai.chat.completions.create(
            model='gpt-4',
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': message},
            ],
            temperature=1,        
            max_tokens=256,         
            top_p=1,
            frequency_penalty=0,    
            presence_penalty=0,             
        )
        SYSTEM_PROMPT_SENT = True
        PREV_RESPONSE = response
    else:
        print(PREV_RESPONSE.choices[0].message.content)
        response = openai.chat.completions.create(
            model='gpt-4',
            messages=[
                {'role': 'system',
                    'content': PREV_RESPONSE.choices[0].message.content},
                {'role': 'user', 'content': message},
            ],
            temperature=1,          
            max_tokens=256,         
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,     
        )
        PREV_RESPONSE = response
    answer = response.choices[0].message.content
    return answer


@login_required(redirect_field_name=None)
def chat_view(request):

    if request.method == 'GET':
        previous_sessions = handle_get_request(request)
        return render(request, 'chat/chat.html', {'previous_sessions': previous_sessions})

    if request.method == 'POST':
        message = request.POST.get('message')
        if (openai_api_key == ''):
            response = 'You have not entered a valid OpenAI key.'
        else:
            response = ask_davinci(message)
            # response = ask_chatgpt(message)

        current_session = Chat_Session.objects.get(session_id=request.session['session_id'])
        new_message = Chat_Message.objects.create(
            session_id=current_session,
            message=message,
            response=response
        )

        return JsonResponse({'message_id': new_message.message_id, 'response': response,})

    return render(request,
                  'chat/chat.html',
                  {'previous_sessions': previous_sessions}
                  )


def handle_get_request(request):
    create_session = Chat_Session(user_id=request.user)
    create_session.save()
    request.session['session_id'] = create_session.session_id
    previous_sessions = get_previous_sessions(request)
    return previous_sessions


def get_previous_sessions(request):
    session_id = request.session['session_id']

    previous_sessions = Chat_Session.objects.exclude(
        session_id=session_id)

    previous_messages = Chat_Message.objects.exclude(
        session_id=request.session['session_id'])

    formatted_sessions = {}
    for s in previous_sessions:
        _id = s.session_id
        formatted_sessions[_id] = {
            'date': s.date.strftime("%Y/%m/%d %H:%M %p"),
            'messages': []
        }

    for m in previous_messages:
        _id = m.session_id.session_id

        if _id in formatted_sessions:
            formatted_sessions[_id]['messages'].append(
                {'id': m.message_id, 'message': m.message, 'response': m.response})

    return formatted_sessions

@login_required(redirect_field_name=None)
def logout(request):
    auth.logout(request)
    return redirect('login')
