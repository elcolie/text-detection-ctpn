def read_points(filename: str):
    point_list = []
    with open(filename, 'r') as file:
        for line in file:
            tmp = line.split(',')
            point_list.append(
                [
                    (int(tmp[0]), int(tmp[1])),
                    (int(tmp[2]), int(tmp[3])),
                    (int(tmp[4]), int(tmp[5])),
                    (int(tmp[6]), int(tmp[7])),
                ]
            )
    return point_list
