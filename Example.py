from chatbot import Chat, register_call
import wikipedia
import os
import warnings
import datetime

warnings.filterwarnings("ignore")


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query, sentences=2)

    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query, sentences=2)
            except Exception:
                pass

    return "Sorry, I don't know about " + query


@register_call("timeNow")
def time_now(session, query):
    return "Current time is: " + datetime.datetime.now().strftime("%H:%M:%S")


first_question = "Hello! I am Pavani's AI Placement Assistant. How can I help you today?"


chat = Chat(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Example.template"
    )
)

chat.converse(first_question)