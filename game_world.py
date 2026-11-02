# 게임월드 리스트 초기화
world = [[], []] # layers for game objects

def add_object(o, depth = 0):
    world[depth].append(o)
    pass

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return #객체 제커 후 함수 종료
        
# 게임 로직
def update():
    for layer in world:
        for o in layer[:]:
            o.update()

#게임 월드 렌더링
def  render():
    for layer in world:
        for o in layer:
            o.draw()
