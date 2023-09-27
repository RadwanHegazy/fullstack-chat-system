from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from chat_app.models import Chat, Message

class OnlineOffline(WebsocketConsumer) :

    def connect(self):

        self.user = self.scope['user']

        self.GROUP_NAME = 'main'

        if self.user.is_anonymous :
            self.close()
            return
        self.accept()

        self.user.is_online = True
        self.user.save()
        
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME,self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.GROUP_NAME,{'type':'online_or_offline','message':{'user_id':self.user.id,"status":'online'}}
        )


    
    

    def receive(self, text_data):
        print(text_data)
        pass


    def online_or_offline (self,event) :
        message = event['message']
        self.send(text_data=json.dumps(message))


    def disconnect(self, code):
        if not self.user.is_anonymous:
            
            self.user.is_online = True
            self.user.save()
            
            async_to_sync(self.channel_layer.group_send)(
                self.GROUP_NAME,{'type':'online_or_offline','message':{'user_id':self.user.id,"status":'offline'}}
            )
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME,self.channel_name
            )
            
        



class ChatConsumer (WebsocketConsumer) : 
    
    def connect(self) :
        
        self.user = self.scope['user']
        
        if self.user.is_anonymous:
            self.close()
            return
        
        chat_uuid = self.scope['url_route']['kwargs']['chatuuid']
        self.GROUP_NAME = f'room_{chat_uuid}'

        self.chat = Chat.objects.get(uuid=chat_uuid)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )



    
    def receive(self, text_data):
        data = json.loads(text_data)
        
        data['sender'] = self.user.full_name

        m = Message.objects.create(
            chat = self.chat,
            sender = self.user,
            text = data['message']
        )
        
        m.save()

        data['picture'] = self.user.picture.url
        data['id'] = m.id
        data['date'] = f'{m.date}' 

        async_to_sync(self.channel_layer.group_send)(
            self.GROUP_NAME,{
                'type':'send_message',
                'data':data
            }
        )

        

    def disconnect(self, code):
        
        if not self.user.is_anonymous :
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )

    

    def send_message (self, event) :
        self.send(text_data=json.dumps(event['data']))