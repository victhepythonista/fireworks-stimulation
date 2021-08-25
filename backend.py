
import pygame,sys,random


colors = [
"red","green", "yellow", "orange","turquoise"]
fireworks = {
    "red":"red.png",
    "turquoise":"blue.png",
    "orange":"orange.png",
    "green":"green.png",
    "yellow":"yellow.png",
}
class Firework:
    def __init__(self,y = 590):
        self.x = random.randint(20,880)
        self.y = y
        self.explode_height = random.randint(20,200)
        self.speed = random.randint(3,9)
        self.color = random.choice(colors)
        self.loaded_color = pygame.Color(self.color)
        self.image = pygame.image.load(fireworks[self.color])
        self.exploding = False
        self.dead = False
        self.particles = []
        self.show_count = 0

    def explode(self):
        for i in range(30):
            x_pos = self.x + random.randint(-50,50)
            y_pos = self.y + random.randint(-50,50)
            rect = pygame.Rect(x_pos, y_pos, 2,2) 
            self.particles.append(rect)
    def show(self, window):
        if self.exploding:
            for particle in self.particles:
                particle.y += 2

                pygame.draw.rect(window, self.loaded_color, particle, 0)
                self.show_count += 1
            if self.show_count > 700:
                self.dead = True

        elif self.y > self.explode_height:
            self.y -= self.speed
            window.blit(self.image,(self.x,self.y))
        else:
            self.explode()
            self.exploding = True

class FireworksManager:
    def __init__(self, limit = 10):
        self.fireworks = [] # takes a Firework class
        self.limit = limit

    def show(self,window):
        if len(self.fireworks) < self.limit:
            self.fireworks.append(Firework())

        for fw in self.fireworks:
            if fw.dead:
                self.fireworks.pop(self.fireworks.index(fw))
            else:
                fw.show(window)








class Screen:
    def __init__(self, size, fps = 50):
        self.running = True
        self.name = ""
        self.size = size
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.events = pygame.event.get()
         

        self.window = pygame.display.set_mode(self.size)
        
        


    def screen_backend(self):
        self.clock.tick(self.fps)
        pygame.display.set_caption(self.name)

    
 
    def exit(self):
        # exit the screen
        self.running = False

    def quit_event(self  ):
            # anticipate a quit event

        for ev in self.events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit()
    def dipslay_widgets(self):
        pass
    def show(self):
        while self.running:
            self.display_widgets()
            self.events = pygame.event.get()
            self.screen_backend()
             
            self.quit_event()
            pygame.display.update()
            continue
            
