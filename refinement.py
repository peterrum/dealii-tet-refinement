def print_face_lines_tet(subcell_definititions_vertices, subface_definitions_vertics):
    
    print("new_quad_lines_tet")
    
    table_face_lines_to_vertices=[[0,1],[1,2],[2,0]]
    
    subface_definitions_vertics_temp = subface_definitions_vertics
    
    for i in subface_definitions_vertics_temp:
        i.sort()
    
    for i in subcell_definititions_vertices:
        temp = []
        for j in table_face_lines_to_vertices:
            a = [i[ii] for ii in j  ]
            a.sort()
            temp = temp + [subface_definitions_vertics_temp.index(a)]
        print(temp)
    print("")

def print_face_line_vertices_tet(subface_definititions_vertices):
    
    print("new_quad_line_vertices_tet")
    
    table_face_lines_to_vertices=[[0,1],[1,2],[2,0]]
    
    for i in subface_definititions_vertices:
        for j in table_face_lines_to_vertices:
            print ([i[ii] for ii in j  ], end = ' ')
        print ("")
    print("")


def print_cell_quads_tet(subcell_definititions_vertices, subface_definitions_vertics):
    
    print("cell_quads_tet")
    
    table_cell_faces_to_vertices=[[0,1,2],[1,0,3],[0,2,3],[2,1,3]]
    
    subface_definitions_vertics_temp = subface_definitions_vertics
    
    for i in subface_definitions_vertics_temp:
        i.sort()
    
    for i in subcell_definititions_vertices:
        temp = []
        for j in table_cell_faces_to_vertices:
            a = [i[ii] for ii in j  ]
            a.sort()
            temp = temp + [subface_definitions_vertics_temp.index(a)]
        print(temp)
    print("")


def print_cell_face_vertices_tet(subcell_definititions_vertices):
    
    print("cell_face_vertices_tet")
    
    table_cell_faces_to_vertices=[[0,1,2],[1,0,3],[0,2,3],[2,1,3]]
    
    for i in subcell_definititions_vertices:
        for j in table_cell_faces_to_vertices:
            print ([i[ii] for ii in j  ], end = ' ')
        print ("")
    print("")
    

def main():
    subline_definitions_vertics = [[0,4],[4,1],[1,5],[5,2],[0,6],[6,2],
                                   [0,7],[7,3],[1,8],[8,3],[2,9],[9,3],
                                   [4,5],[5,6],[6,4],
                                   [4,7],[7,8],[8,4],
                                   [6,9],[9,7],[7,6],
                                   [5,8],[8,9],[9,5],
                                   [6,8]] 
    
    subface_definitions_vertics = [[6,4,7],[4,5,8],[5,6,9],[7,8,9], 
                                   [4,6,8],[6,5,8],[8,7,6],[9,6,8],
                                   [0,4,6],[4,1,5],[5,2,6],[4,5,6],
                                   [1,4,8],[4,0,7],[8,7,3],[4,7,8],
                                   [0,6,7],[6,2,9],[7,9,3],[6,9,7],
                                   [2,5,9],[5,1,8],[9,8,3],[5,8,9]]
    
    subcell_definititions_vertices = [[0,4,6,7], [4,1,5,8], [6,5,2,9], [7,8,9,3],
                                      [4,5,6,8], [4,7,8,6], [6,9,7,8], [5,8,9,6]]
                                      
                                      
    print_face_lines_tet(subface_definitions_vertics,subline_definitions_vertics)
    print_face_line_vertices_tet(subface_definitions_vertics)
                                      
    print_cell_quads_tet(subcell_definititions_vertices,subface_definitions_vertics)
    print_cell_face_vertices_tet(subcell_definititions_vertices)

if __name__ == "__main__":
    main()