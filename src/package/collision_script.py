import pygame, math

class Collider:
    def __init__(self,point_1,point_2):
        self.line = (point_1,point_2)
        self.slope = self.get_slope()
        self.normal = self.get_normal()
    
    def collide(self,rect: pygame.Rect):
        if rect.clipline(self.line):
            if self.normal < math.pi/2:
                poi = rect.topleft
            elif self.normal < 0:
                poi = rect.topright
            elif self.normal > math.pi/2:
                poi = rect.bottomleft
            else:
                poi = rect.bottomright

            if self.slope[0] == 0: #handling horizontal slopes (0 division error)
                x = poi[0]
                y = self.line[0][1]
            elif self.slope[0] == "v": #handling vertical slopes (0 division error)
                x = self.line[0][0]
                y = poi[1]
            else:
                m1,b1 = self.slope
                m2 = -1/m1
                b2 = poi[1]-m2*poi[0]
                x = (b2-b1)/(m1-m2)
                y = x*m2+b2
            
            x_offset = x-poi[0]
            y_offset = y-poi[1]
            # x_offset = round(-math.cos(self.normal)*rect.width/2,2)
            # y_offset = round(-math.sin(self.normal)*rect.height/2,2)
            # print(x_offset, y_offset)
            return x_offset, y_offset
    
    def get_slope(self):
        x1 = min(self.line[0][0],self.line[1][0])
        x2 = max(self.line[0][0],self.line[1][0])
        y1 = min(self.line[0][1],self.line[1][1])
        y2 = max(self.line[0][1],self.line[1][1])
        if x1 != x2:
            m = (y2-y1)/(x2-x1)
            b = y1-m*x1
            return [m,b]
        else:
            return ["v",x1]

    def get_normal(self):
        x1,y1 = self.line[0]
        x2,y2 = self.line[1]
        angle = math.atan2((y2-y1),(x2-x1))+math.pi/2
        # print(angle)
        return angle

    def reverse_normals(self):
        self.line = (self.line[1],self.line[0])
        self.normal = self.get_normal()

    def draw(self,screen):
        point_1 = (self.line[0][0],self.line[0][1])
        point_2 = (self.line[1][0],self.line[1][1])
        pygame.draw.line(screen,(0,0,0),point_1,point_2)
        pygame.draw.circle(screen,(0,0,0),point_1,5,2)
        pygame.draw.circle(screen,(0,0,0),point_2,5,2)


class ColliderPolygon:
    def __init__(self,points=[]):
        self.points = points
        self.lines = []
        self.calculate_lines()
    
    def calculate_lines(self):
        self.lines.clear()
        for i in range(len(self.points)):
            self.lines.append(Collider(self.points[i-1],self.points[i]))
    
    def reverse_facing(self):
        self.points.reverse()
        self.calculate_lines()
    
    def add_point(self,point,index:int=-1):
        self.points.insert(index,point)
        self.calculate_lines()
    
    def remove_point(self,index:int):
        self.points.pop(index)
        self.calculate_lines()
    
    def collide(self,rect: pygame.Rect):
        for line in self.lines:
            collison = line.collide(rect)
            if collison:
                return collison
    
    def draw(self,screen):
        for line in self.lines:
            line.draw(screen)


# class ColliderGroup: # work in progress...
#     def __init__(self):
#         self.group = []
#         self.disabled = False
    
#     def set_disabled(self,state:bool):
#         self.disabled = state
    
#     def collide(self,rect):
#         if self.disabled == False:
#             for line in self.group:
#                 return line.collide(rect)
            
#     def add(self,new):
#         if type(new) == list:
#             for collider in new:
#                 self.group.append(collider)
#         elif type(new) == Collider:
#             self.group.append(new)