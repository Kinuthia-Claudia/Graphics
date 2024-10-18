import cairo

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,1)
ctx.paint ()


#side doors
ctx.rectangle(50, 800,250,200 )
ctx.set_source_rgb(0,0,0)
ctx.rectangle(700, 800,250,200 )
ctx.set_source_rgb(0,0,0)
ctx.fill()

#windows

ctx.rectangle(100, 850,50,50 )
ctx.rectangle(200, 850,50,50 )
ctx.rectangle(750, 850,50,50 )
ctx.rectangle(850, 850,50,50 )
ctx.set_source_rgb(1,1,1)
ctx.fill()

#Trapezium

ctx.move_to(0,790)
ctx.line_to(150,650)
ctx.line_to(300,650)
ctx.line_to(300,790)
ctx.close_path()
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()

ctx.move_to(700,790)
ctx.line_to(700,650)
ctx.line_to(900,650)
ctx.line_to(1000,790)
ctx.close_path()
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(5)
ctx.stroke()

#main building

ctx.move_to(310,1000)
ctx.line_to(690,1000)
ctx.line_to(690,500)
ctx.line_to(650,450)
ctx.line_to(350,450)
ctx.line_to(310,500)
ctx.close_path()
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(5)
ctx.stroke()

# line above main
ctx.move_to(250,520)
ctx.line_to(340,420)
ctx.line_to(650,420)
ctx.line_to(740,520)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(20)
ctx.stroke()

# Circle window
ctx.set_source_rgb(1, 1, 1)  # White outline
ctx.arc(500, 550, 35, 0, 2 * 3.14)
ctx.fill()

#doors
ctx.move_to(350,750)
ctx.line_to(500,650)
ctx.line_to(670,750)
ctx.set_source_rgb(1,1,1)
ctx.set_line_width(15)
ctx.stroke()

# Door (white, arched)
ctx.set_source_rgb(1, 1, 1)  # White color for the door
ctx.move_to(420, 830)
ctx.arc(500, 780, 80, 3.14, 0)  # Arc for the top part of the door
ctx.line_to(580, 950)  # Right side of the door
ctx.line_to(420, 950)   # Left side of the door
ctx.close_path()
ctx.fill()
ctx.set_source_rgb(0, 0, 0)  # Black color for the line
ctx.set_line_width(20)
ctx.move_to(500, 670)  # Starting at the top of the dome
ctx.line_to(500, 950)  # Extending to the bottom of the door
ctx.stroke()


#square
ctx.rectangle(420, 240,160,160 )
ctx.set_source_rgb(0,0,0)
ctx.fill()
ctx.move_to(390,220)
ctx.line_to(605,220)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(20)
ctx.stroke()

# arch window
ctx.set_source_rgb(1, 1, 1)  # White color for the door
ctx.move_to(470, 300)
ctx.arc(500, 300, 30, 3.14, 0)  # Arc for the top part of the door
ctx.line_to(530, 380)  # Right side of the door
ctx.line_to(470, 380)   # Left side of the door
ctx.close_path()
ctx.fill()


#cross
ctx.set_source_rgb(0, 0, 0)
ctx.rectangle(495, 40, 10, 60)
ctx.rectangle(480, 55, 40, 10)
ctx.fill()
ctx.move_to(475,200)
ctx.line_to(530,200)
ctx.line_to(520,130)
ctx.line_to(500,100)
ctx.line_to(484,130)
ctx.close_path()
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

# Save the image
surface.write_to_png(" 2Dhouse.png")
print("2Dhouse.png")