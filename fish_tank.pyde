def setup():
    size(700,700)
    background(0,80,200)
    #body_color = color(random(255),random(255),random(255))
    #eye_color = color(255,255,255)
    #pupil_color = color(0,0,0)
    
    fish_x = 100
    fish_y = 100
    fish_tank(fish_x,fish_y)
              #body_color,eye_color,pupil_color)


    i=1
    while i < 40 :
        print(i)
        fish_tank(random(700),random(700))
        i=i+1
    print(fish_x)
    
def fish_tank(fish_x,fish_y):
    body_color = color(random(255),random(255),random(255))
    fill(body_color)
    ellipse(fish_x-25,fish_y-70,50,20)
    triangle(40, 50, 50, 30, 10, 10)
    
    
    #triangle (
    #triangle(fishX+25,fishY,fishX+25+10,fishY-20,fishX+30+10,fishY+20)

    
