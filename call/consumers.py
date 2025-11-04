
import json
from channels.generic.websocket import AsyncWebsocketConsumer

waiting_user = None  # global: holds one waiting user

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        global waiting_user
        await self.accept()

        if waiting_user is None:
            waiting_user = self
            self.partner = None
            await self.send(json.dumps({"info": "Waiting for a partner..."}))
        else:
            self.partner = waiting_user
            waiting_user.partner = self
            waiting_user = None
            # notify both users they are connected
            await self.send(json.dumps({"info": "Partner found!"}))
            await self.partner.send(json.dumps({"info": "Partner found!"}))

    async def disconnect(self, close_code):
        global waiting_user
        if waiting_user == self:
            waiting_user = None
        if hasattr(self, 'partner') and self.partner:
            await self.partner.close()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if hasattr(self, 'partner') and self.partner:
            await self.partner.send(text_data)
