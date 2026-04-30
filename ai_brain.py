import wikipedia


def smart_reply(query):
    query = query.lower()

    if "your name" in query:
        return "I am EPick, your voice assistant."

    if "how are you" in query:
        return "I am working perfectly fine."

    if "who made you" in query:
        return "I was created by you."

    return None


def wiki_reply(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return None


def get_ai_response(query):

    reply = smart_reply(query)
    if reply:
        return reply

    reply = wiki_reply(query)
    if reply:
        return reply

    return "Sorry, I don't have enough information about that."