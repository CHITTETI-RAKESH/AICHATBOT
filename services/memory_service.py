MAX_CONTEXT = 10

def build_context(
history,
new_message
):

    messages = []

    for chat in history[-MAX_CONTEXT:]:

        messages.append(
            {
                "role":"user",
                "content":
                chat.question
            }
        )

        messages.append(
            {
                "role":"assistant",
                "content":
                chat.answer
            }
        )

    messages.append(
        {
            "role":"user",
            "content":new_message
        }
    )

    return messages
