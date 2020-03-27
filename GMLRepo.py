class GMLRepo(object):
    def __init__(self, filename):
        self._filename = filename

    def readGMLFile(self):
        f = open(self._filename, "r")
        net = {}
        creator_name = f.readline();
        n = 0
        m = 0
        mat = []
        f.readline()  # graph
        f.readline()  # [
        f.readline()  # directed 0
        line = f.readline();
        while line != ']':
            line = line.replace("\n", "")
            line = line.strip()
            if line == 'node':
                # adding node
                f.readline()  # [
                id_line = f.readline()  # id number
                id = int(id_line.split()[1])
                label_line = f.readline()  # label string
                #value_line = f.readline()  # value string
                f.readline()  # ]
                n = n + 1
            elif line == 'edge':
                if m == 0:
                    for i in range(n):
                        mat.append([])
                        for j in range(n):
                            mat[i].append(0)
                # adding edge
                f.readline()  # [
                source_line = f.readline()  # source number
                source = int(source_line.split()[1])
                source = source - 1
                target_line = f.readline()  # target number
                # value_line = f.readline()  # value string
                target = int(target_line.split()[1])
                target = target - 1
                f.readline()  # ]
                mat[source][target] = 1
                mat[target][source] = 1
                m = m + 1
            line = f.readline()
            line = line.strip()
            line = line.replace("\n", "")
        degrees = []
        print(mat)
        for i in range(n):
            d = 0
            for j in range(n):
                if mat[i][j] == 1:
                    d += 1
            degrees.append(d)
        net['noNodes'] = n
        net['noEdges'] = m
        net['degrees'] = degrees
        net['mat'] = mat
        return net
