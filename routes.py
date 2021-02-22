class route():
  def __init__(self, height, top_route, x_top_route):
    self.height = height
    self.top_route = top_route
    self.x_top_route = x_top_route

class slant(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -75, -50, -100 if breaks_left else 100)

class flat(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -75, 0, -100 if breaks_left else 100)

class curl(route):
  def __init__(self):
    route.__init__(self, -100, 20, 15)

class comeback(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -150, 45, -30 if breaks_left else 30)
  
class quick_out(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -60, 0, -100 if breaks_left else 100)

class medium_out(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -120, 0, -100 if breaks_left else 100)

class deep_out(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -200, 0, -100 if breaks_left else 100)

class corner(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -200, -100, -100 if breaks_left else 100)

class post(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -150, -150, -60 if breaks_left else 60)

class skinny_post(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -150, -150, -30 if breaks_left else 30)

class go(route):
  def __init__(self):
    route.__init__(self, -150, -150, 0)

class fade(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -10, -50, -40 if breaks_left else 40)

class shoot(route):
  def __init__(self, breaks_left = True):
    route.__init__(self, -2, -50, -150 if breaks_left else 150 )

""" TODO Multiple cut routes
class crosser(route):
  pass

class over(route):
  pass

class drag(route):
  pass

class sit(route):
  pass

"""

# TODO Play protection for routes. Like: Post and corner, basically the same. But make sure
# Corner is always going away from the quarterback, same for the out