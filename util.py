def sign(x) -> float:
    if x > 0:
        return 1.0
    if x < 0:
        return -1.0
    return 0.0


def check_out_of_range(min_x, min_y, max_x, max_y, x, y) -> bool:
    return not (min_x <= x and x <= max_x\
           and min_y <= y and y <= max_y)
