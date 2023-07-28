import pygame

class EventHandler:
    events = []
    @staticmethod
    def init():
        EventHandler.poll_events()
    @staticmethod
    def poll_events():
        EventHandler.events = pygame.event.get()