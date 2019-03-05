from graphviz import Digraph, Source

chart=Digraph(format='png')
chart.node('A','init')
chart.node('B','gamefield')
chart.node('C','win')
chart.node('D','gameover')
chart.node('E','exit')
chart.edge('A','B','init')
chart.edge('B','A','restart')
chart.edge('C','A','restart')
chart.edge('D','A','restart')
chart.edge('B','C','win')
chart.edge('B','D','gameover')
chart.edge('B','E','exit')
chart.edge('C','E','exit')
chart.edge('D','E','exit')

chart.save('2048.gv')
chart.render('2048.gv')
p=Source.from_file('2048.gv')

print(p.Source)