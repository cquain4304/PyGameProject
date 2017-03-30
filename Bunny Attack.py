from gamelib import*

game = Game(800,600,"Bunny Attack!")
bunny = Image("images\\bunny.jpg",game)
bk = Image("images\\background.jpg",game)
dog = Image("images\\dog.png",game)

bks = Sound("bk.wav",1)

dog.resizeTo(150,150)
dog.moveTo(150,150)

bk.resizeTo(800,600)
bunny.resizeTo(150,150)
bunny.setSpeed(6,60)
dog.setSpeed(4,30)

while not game.over:
    game.processInput()
    bk.draw()
    bks.play()
    bunny.move("True")
    dog.move("True")

if bunny.collidedWith(mouse) and mouse.LeftButton:
    game.score+=1
    x = randint(150,650)
    y = randint(150,450)
    bunny.moveTo(x,y)
    bunny.speed+=2
    bunnt.resizeBy(-2)
  
    if bunny.collidedWith(dog):
        dog.health-=1

    if turkey.collidedWith(mouse) and mouse.LeftButton:
        turkey.health-=1
        gobble.play()
   
    if game.score>=10:
        game.drawText("You win!",300,0)
        game.over=True

   
   
   
    game.drawText("Health =  " + str(dog.health),500,0)
    game.displayScore()
game.wait(K_SPACE)
game.quit()
   


 
   
    


   




    


