from artist import artist

# Sets up the drawing area

artist.up()
artist.draw(0, 0)
artist.draw(1)
artist.rotate(180, t=4000)
artist.draw(0)
artist.rotate(0)
for forward_pos in (0.2, 0.4, 0.6, 0.8):
    artist.up(t=1000)
    artist.draw(forward_pos, 0)
    artist.rotate(5, t=1000)
artist.up()
artist.out()
