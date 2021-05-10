import networkx as nx
import matplotlib.pyplot as plt

# def draw_shell_graph_from_to_file():
#     read = read_adjlist('2.txt')
#     nx.draw_shell(read, with_labels=True, font_color='white', node_color='black')
#     save_graph('2_automatically.png')

# def draw_graph_in_file(graph):
#     plt.axes().set_aspect('equal', adjustable='datalim')
#     nx.draw(graph, pos=pos, with_labels=True, font_color='white', node_color='black')
#     save_graph('2_manually.png')

# def write_adjlist(g, path):
#     """
#     для створення текстового файлу зі спискy суміжності
#     """
#     nx.write_adjlist(g, path)

# def make_graph():
#     g = nx.empty_graph(13)
#     g.add_edges_from((i, i+6) for i in range(6))
#     g.add_edges_from((i, i+1) for i in (0, 2, 6, 8, 11))
#     g.add_edges_from((i, i+7) for i in (0, 2, 5))
#     g.add_edges_from((i, i+5) for i in (1, 3))
#     return g


pos = {i: (i, 2) for i in range(6)}
pos.update({i: (i-6, 0) for i in range(6, 13)})


def read_adjlist(path):
    H = nx.read_adjlist(path, create_using=nx.Graph, nodetype=int)
    return H


def draw_graph(graph, pos):
    plt.axes().set_aspect('equal', adjustable='datalim')
    nx.draw(graph, pos=pos, with_labels=True, font_color='white', node_color='black')


def draw_diameter(graph, pos,  edges_colors, nodes_colors):
    nx.draw(graph, pos=pos, with_labels=True, font_color='white', node_color=nodes_colors, edge_color=edges_colors)


def automatic_graph(g,  path_to):
    nx.draw_shell(g, with_labels=True, font_color='white', node_color='black')
    save_graph(path_to)
    return g


def save_graph(path):
    plt.savefig(path, format='jpg')


def manual_graph(g, pos, path_to):
    draw_graph(g, pos)
    save_graph(path_to)
    return g


def general_information(g):
    h = 0
    components = ['First', 'Second', 'Third', 'Fourth']
    for i in nx.connected_components(g):
        print(f"{components[h]} component: ", end='\n')
        name = g.subgraph(i)
        h += 1
        print('\tnumber of nodes: ', end='')
        print(len(nx.nodes(name)))
        print('\tnumber of edges: ', end='')
        print(len(nx.edges(name)))
        print('\tdegree and eccentricity of nodes: \n', end='')
        for j in i:
            print('\t', j, ': ', name.degree(j), '; ', nx.eccentricity(name, j), sep='')
        print('\tradius: ', nx.radius(name), sep='')
        print('\tdiameter: ', nx.diameter(name), sep='', end='\n\n')


def diameter_bfs(g, color, path):
    for i in nx.connected_components(g):
        g1 = g.subgraph(i)
        diam = nx.diameter(g1)
        lst = []
        for v, w in nx.bfs_edges(g1, list(i)[0]):
            lst.append([v, w])
        lst = lst[:diam]
        v = lst[0][0]
        w = lst[0][1]
        g1[v][w]['color'] = color
        edges_colors = [color for a, b, color in g1.edges.data(data='color', default='black')]
        nodes_colors = [color for v, color in g1.nodes.data(data='color', default='black')]
        for j in (v, w):
            if j in g1.nodes:
                ind = list(g1.nodes).index(j)
                nodes_colors[ind] = color
        draw_diameter(g1, pos, edges_colors, nodes_colors)
    save_graph(path)


def forest_graph(g, color):
    g1 = g.copy()
    for v, w in nx.dfs_edges(g1):
        g1[v][w]['color'] = color
    edges_colors = [color for a, b, color in g1.edges.data(data='color', default='black')]
    draw_diameter(g1, pos, edges_colors, 'black')
    save_graph('forest.jpg')


g = read_adjlist('graph_adjlist.txt')
automatic_graph(g, 'g_automatically.jpg')
manual_graph(g, pos, 'g_manually.jpg')
general_information(g)
diameter_bfs(g, 'pink', 'diameter_bfs.jpg')
forest_graph(g, 'red')


