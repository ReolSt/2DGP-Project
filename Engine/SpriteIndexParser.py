class SpriteIndexParser:
    def __init__(self, filePath):
        self.indices = {}

        with open(filePath, "r") as index_file:
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
