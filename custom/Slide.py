class Slide(object):
    def __init__(self, slideType, title, body):
        self.type = slideType
        self.title = title
        self.body = body
        self.children = []
    def __str__(self):
        return "type: {}\ntitle: {}\nbody: {}".format(self.type, self.title, self.body)
