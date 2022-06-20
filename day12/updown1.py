def updown(user_input,answer,max_v,min_v):
    if user_input==answer:
        result=1
    elif user_input<answer:
        min_v=user_input
        result='UP'
    else:
        max_v=user_input
        result='Down'
    return result,max_v,min_v