from pygame import Vector2

def lerp(start, end, value:float):
    return start + (end - start) * value


def tuple_to_vector(tuple:tuple) -> Vector2:
    return Vector2(tuple[0], tuple[1])


def segment_intersects(start_1:Vector2, end_1:Vector2, start_2:Vector2, end_2:Vector2) -> bool:
    segment_1 = end_1 - start_1
    segment_2 = end_2 - start_2

    cache = -segment_2.x * segment_1.y + segment_1.x * segment_2.y 
    if cache == 0:
        return False

    s = (-segment_1.y * (start_1.x - start_2.x) + segment_1.x * (start_1.y - start_2.y) ) / (cache)
    t = (segment_2.x * (start_1.y - start_2.y) - segment_2.y * (start_1.x - start_2.x) ) / (cache)

    intersects = s >= 0 and s <= 1 and t >= 0 and t <= 1

    return intersects


if __name__ == '__main__':
    inter = segment_intersects(
        Vector2(0,0),
        Vector2(2,3),
        Vector2(1,0),
        Vector2(0,1),
    )

