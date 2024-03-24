import sys

def create_vertices(scale = 1.0, x_shift = 0.0, y_shift = 0.0):
    vertices = [[0,0,0], [0,0,1], [1,0,0], [0,1,0],
        [0,0,0.5], [0.5,0.0,0.5], [0.5,0,0], [0,0.5,0], [0.0,0.5,0.5], [0.5,0.5,0.0]]

    for v in range(0, len(vertices)):
        vertices[v] = [vertices[v][0]*scale + x_shift, vertices[v][1]*scale + y_shift, vertices[v][2]*scale]

    return vertices

def create_label_positions():
    return ["below", "below", "below", "above", "above", "below", "above", "right", "left", "above"]

def draw_tet(scale = 1.0, x_shift = 0.0, y_shift = 0.0):
    vertices = create_vertices(scale, x_shift, y_shift)

    def print_vertices(vertices):
        print("\\draw[rounded corners] %s;" % " -- ".join(["(%f, %f, %f)" % (i[0],i[1], i[2]) for i in vertices]))

    print_vertices(vertices[i] for i in [0, 1, 2, 0])
    print_vertices(vertices[i] for i in [0, 1, 3, 0])
    print_vertices(vertices[i] for i in [0, 2, 3, 0])


def draw_line(scale, x_shift, y_shift, indices):
    vertices        = create_vertices(scale, x_shift, y_shift)
    label_positions = create_label_positions()

    def print_vertices(vertices):
        print("\\draw[red, fill=red, line width=3pt] %s;" % " -- ".join(["(%f, %f, %f)" % (i[0],i[1], i[2]) for i in vertices]))

    print_vertices(vertices[i] for i in indices)

    for i in range(0, len(indices)):
        print("\\draw[black,fill=black] (%f,%f,%f)       circle (0.8pt) node [%s] {%d};" % (vertices[indices[i]][0],vertices[indices[i]][1],vertices[indices[i]][2], label_positions[indices[i]], i))

def draw_triangle(scale, x_shift, y_shift, indices):
    vertices        = create_vertices(scale, x_shift, y_shift)
    label_positions = create_label_positions()

    def print_vertices(vertices):
        print("\\draw[rounded corners,red, fill=red, fill opacity=0.1, line width=3pt] %s -- cycle;" % " -- ".join(["(%f, %f, %f)" % (i[0],i[1], i[2]) for i in vertices]))

    print_vertices(vertices[i] for i in indices)

    for i in range(0, len(indices)):
        print("\\draw[black,fill=black] (%f,%f,%f)       circle (0.8pt) node [%s] {%d};" % (vertices[indices[i]][0],vertices[indices[i]][1],vertices[indices[i]][2], label_positions[indices[i]], i))

def draw_cell(scale, x_shift, y_shift, indices):
    vertices        = create_vertices(scale, x_shift, y_shift)
    label_positions = create_label_positions()

    def print_vertices(vertices):
        print("\\draw[rounded corners,red, fill=red, fill opacity=0.1, line width=3pt] %s -- cycle;" % " -- ".join(["(%f, %f, %f)" % (i[0],i[1], i[2]) for i in vertices]))

    print_vertices(vertices[i] for i in [indices[i] for i in [0, 1, 2]])
    print_vertices(vertices[i] for i in [indices[i] for i in [0, 1, 3]])
    print_vertices(vertices[i] for i in [indices[i] for i in [0, 2, 3]])

    for i in range(0, len(indices)):
        print("\\draw[black,fill=black] (%f,%f,%f)       circle (0.8pt) node [%s] {%d};" % (vertices[indices[i]][0],vertices[indices[i]][1],vertices[indices[i]][2], label_positions[indices[i]], i))


def draw_labels():
    vertices        = create_vertices()
    label_positions = create_label_positions()

    for i in range(0, len(vertices)):
        print("\\draw[black,fill=black] (%f,%f,%f)       circle (0.8pt) node [%s] {\\LARGE %d};" % (vertices[i][0],vertices[i][1],vertices[i][2], label_positions[i], i))

def print_header():
    print("\\documentclass{standalone}")
    print("\\usepackage{tikz}")
    print("\\begin{document}")
    print("\\begin{tikzpicture}[scale=3.5]")
            
def print_footer():
    print("\\end{tikzpicture}")
    print("\\end{document}")

def main():
    original_stdout = sys.stdout

    x_shift_0 = 1.4
    x_shift = 0.9
    y_shift = -0.85

    subline_definitions_vertics = [[0,4],[4,1],[1,5],[5,2],[0,6],[6,2],
                                   [0,7],[7,3],[1,8],[8,3],[2,9],[9,3],
                                   [4,5],[5,6],[6,4],
                                   [4,7],[7,8],[8,4],
                                   [6,9],[9,7],[7,6],
                                   [5,8],[8,9],[9,5]]

    subline_definitions_vertics = subline_definitions_vertics + [[[6,8], [5,7], [4,9]]]

    subface_definitions_vertics = [[6,4,7],[4,5,8],[5,6,9],[7,8,9]]

    subface_definitions_vertics = subface_definitions_vertics + [[[[4,6,8],[6,5,8],[8,7,6],[9,6,8]],
      [[5,4,7],[6,5,7],[8,7,5],[7,9,5]],
      [[5,4,9],[4,6,9],[7,4,9],[4,8,9]]]]

    subface_definitions_vertics = subface_definitions_vertics + [[0,4,6],[4,1,5],[5,2,6],[4,5,6],
                                   [1,4,8],[4,0,7],[8,7,3],[4,7,8],
                                   [0,6,7],[6,2,9],[7,9,3],[6,9,7],
                                   [2,5,9],[5,1,8],[9,8,3],[5,8,9]]

    subcell_definititions_vertices = [[0,4,6,7], [4,1,5,8], [6,5,2,9], [7,8,9,3]]
    
    subcell_definititions_vertices = subcell_definititions_vertices + [[[[4,5,6,8], [4,7,8,6], [6,9,7,8], [5,8,9,6]],
      [[4,5,6,7], [4,7,8,5], [6,9,7,5], [5,8,9,7]],
      [[4,5,6,9], [4,7,8,9], [6,9,7,4], [5,8,9,4]]]]

    with open("plot.tex", 'w') as f:
        sys.stdout = f

        print_header()
            
        draw_tet()
        draw_labels()

        # lines
        for i in range(0, 24):
            scale_ = 0.5
            x_     = x_shift_0 + x_shift * 1
            y_     = (-1.0 + i) * y_shift
            draw_tet(scale_, x_, y_)
            draw_line(scale_, x_, y_, subline_definitions_vertics[i])

        for i in range(0, 3):
            scale_ = 0.5
            x_     = x_shift_0 + x_shift * i
            y_     = (-1.0 + 24) * y_shift
            draw_tet(scale_, x_, y_)
            draw_line(scale_, x_, y_, subline_definitions_vertics[24][i])

        # faces
        for i in range(0, 4):
            scale_ = 0.5
            x_     = x_shift_0 + x_shift * (1 + 3)
            y_     = (-1.0 + i) * y_shift
            draw_tet(scale_, x_, y_)
            draw_triangle(scale_, x_, y_, subface_definitions_vertics[i])

        for j in range(0, 4):
            for i in range(0, 3):
                scale_ = 0.5
                x_     = x_shift_0 + x_shift * (i + 3)
                y_     = (-1.0 + 4 + j) * y_shift
                draw_tet(scale_, x_, y_)
                draw_triangle(scale_, x_, y_, subface_definitions_vertics[4][i][j])
        
        for i in range(8, 24):
            scale_ = 0.5
            x_     = x_shift_0 + x_shift * (1 + 3)
            y_     = (-1.0 + i) * y_shift
            draw_tet(scale_, x_, y_)
            draw_triangle(scale_, x_, y_, subface_definitions_vertics[i - 3])

        # cells
        for i in range(0, 4):
            scale_ = 0.5
            x_     = x_shift_0 + x_shift * (1 + 6)
            y_     = (-1.0 + i) * y_shift
            draw_tet(scale_, x_, y_)
            draw_cell(scale_, x_, y_, subcell_definititions_vertices[i])

        for j in range(0, 4):
            for i in range(0, 3):
                scale_ = 0.5
                x_     = x_shift_0 + x_shift * (i + 6)
                y_     = (-1.0 + 4 + j) * y_shift
                draw_tet(scale_, x_, y_)
                draw_cell(scale_, x_, y_, subcell_definititions_vertices[4][i][j])


        for i in range(0,4):
            print("\\draw[black, line width=1pt] (%f, %f) -- (%f, %f);" % (x_shift_0 + i*3*x_shift - 0.3 , -y_shift + 0.8, x_shift_0 + i*3*x_shift - 0.3, 24*y_shift + 0.55))

        print("\\draw[black,fill=black] (%f, %f) node [below] {\\LARGE %s};" % (x_shift_0/4 , -y_shift + 0.8, "(new) vertices"))
        for i in range(0,3):
            labels  = ["new lines", "new faces", "new cells"]
            print("\\draw[black,fill=black] (%f, %f) node [below] {\\LARGE %s};" % (x_shift_0 + i*3*x_shift - 0.3 + 1.5*x_shift , -y_shift + 0.8, labels[i]))
        
        for i in range(0,26):
            print("\\draw[black, line width=1pt, dashed] (%f, %f) -- (%f, %f);" % (x_shift_0 - 0.3 , -y_shift + 0.55 + y_shift*i, x_shift_0 - 0.3 + 9*x_shift + 0.7 , -y_shift + 0.55 + y_shift*i))
        for i in range(0,25):
            print("\\draw[black,fill=black] (%f, %f) node [below] {\\LARGE %d};" % (x_shift_0 - 0.3 + 9*x_shift + 0.2 , -y_shift*0.5 + 0.65 + y_shift*i, i))

        
        print_footer()

        sys.stdout = original_stdout


if __name__ == "__main__":
    main()