class SpriteIndexParser:
    def __init__(self, index_file_name):
        self.indices = {}

        with open(index_file_name, "r") as index_file:
            for line in index_file.readlines():
                tokens = line.split()
                if len(tokens) < 4:
                    continue

                name, *positions = tokens
                startX, startY, endX, endY = map(int, positions)

                self.indices[name] = {
                    'startX': startX,
                    'startY': startY,
                    'endX': endX,
                    'endY': endY
                }
