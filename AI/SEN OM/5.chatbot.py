def chatbot():
    print('elementary chat bot')
    
    while True:
        user_ip=input('You: ').lower()
        
        if user_ip == 'bye':
            print('bye have a good day')
            break
        elif 'hello' in user_ip or 'hi' in user_ip:
            print('Chatbot: how can i help you')
            
        elif 'how are you' in user_ip :
            print('Chatbot: i am fine')
        
        elif 'color of sky' in user_ip :
            print('Chatbot: color of sky is blue')
        
        else:
            print('sorry i am not able to understand')
chatbot()
    
    
