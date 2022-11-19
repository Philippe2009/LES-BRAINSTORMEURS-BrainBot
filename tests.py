brain_bot.move(72,'cm',0,50)
left_motor.run_for_degrees(-250, 50)
for i in range(4):
    brain_bot.move(-10,'cm',0,100)
    brain_bot.move(43,'cm',0,100)
left_motor.run_for_degrees(250, 100)
brain_bot.move(-72,'cm',0,100)
