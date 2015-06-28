# connect to signals
from telegrambot.signals import message_received
from motioncontrol.signals import picture_alert
from django.dispatch import receiver


@receiver(message_received)
def receive_message(sender, **kwargs):
    from parser import Parser
    p = Parser(sender)
    p.parse(kwargs['message'])
    
    
    
@receiver(picture_alert)
def receive_picture_alert(sender, **kwargs):
    print "Picture Alert"
    