import pygame
import random
pygame.init()

'''
pygame.init() safely initializes all imported pygame modules regardless if the modules 
actually need to be initialized; but since it does for the ones that do, 
it saves the trouble of manually initializing each module individually
'''

#make it class and not globas as cna port shit to other projects 

class DrawStuff:
    #stuff is in r,g,b
    dark = 34, 40, 49
    white = 255,255,255
    green = 0,255,0
    red = 255,0,0
    grey = 128,128,128
    background_color = dark
    
    gradients = [(238, 238, 238), (57, 62, 70), (0, 173, 181)]
    
    #side_pad =100  
    #is 100 px padding if needed
    
    #top padding
    top_pad = 150
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        #setting up window as a atribute
        self.window = pygame.display.set_mode((width,height))
        #setting caption for hte window
        pygame.display.set_caption("sorting visualizer by X30")
        #defininf a new method
        self.set_list(lst)
        
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        #a way to deterrmine the width of the bar
        #if needed side padding --> self.pixle_width = self.width - self.side_pad/ len(lst)
        #gives us our drawable area
        self.pixle_width = round(self.width / len(lst))
        #representation of lines realtive to larest number
        #self.height - self.top_pad --> gives us max drawable area
        #self.max_val - self.min_val --> gives total values in the range
        self.block_height = round((self.height - self.top_pad)/(self.max_val - self.min_val))
        
        #top left x = 0, y=0
        self.start_x = 0


def draw(draw_info):
    draw_info.window.fill(draw_info.background_color)
    draw_list(draw_info)
    pygame.display.update()
    

def draw_list(draw_info):
    #we iterate over our list
    lst = draw_info.lst
    
    for i,val in enumerate(lst):
        #calculating rect drawing positions
        x = draw_info.start_x + 1* draw_info.pixle_width
        
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        
        color = draw_info.gradients[i % 3] #shit returns 0/1/2
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.pixle_width, draw_info.height))
        

#random list generator
def generator(n, min_val, max_val):
    lst = []
    for _ in range(n):
        #gens and assigns random values b/w max and min range including em
        val = random.randint(min_val, max_val)
        lst.append(val)
        #can shuffle the list mroe if we want or use it as it is
    return lst


#driver code
def main():
    #render screen and setup event loop 
    run = True
    #need a loop so it constantley draws instead of closing once done
    tick_rate = pygame.time.Clock()
    
    n=50
    min_val= 0
    max_val = 100
    
    lst = generator(n,min_val,max_val)
    #instanciated the class
    #and cretes a window
    draw_info = DrawStuff(800, 600, lst)
    while run:
        tick_rate.tick(60) #fps
        
        #drawing window
        draw(draw_info)
        #handelig events
        #pygame.event.get --> returns list of events that occured since the last loop/tick, gives it to us in event variable
        for event in pygame.event.get():
            #is equal to hitting x in top right corner and this has to be manually handeled as done below :D
            #the type of event is returned in event so we need to check for its type
            if event.type == pygame.QUIT:
                run = False
                
            if pygame.event != pygame.KEYDOWN:
                continue
            
            if pygame.event.key == pygame.K_r:
                #reset the list
                lst = generator(n,min_val,max_val)
                
                #draw_info is storing the list, so we gotta reset it in draw_info calss
                draw_info.set_list(lst)
                
                
    #once out of while we end the pygame program
    pygame.quit()
        
if __name__ == "__main__":
    #maeks sures that we are running this module directly then only calls main
    #if was imported then nah
    main()     