import toytree       # a tree plotting library
import toyplot       # a general plotting library
import toyplot.pdf
import numpy as np
import re
import argparse


parser = argparse.ArgumentParser(description='Plots a tree file with hominid samples in it')
parser.add_argument('--file', metavar='N', type=str, nargs='+',help='A .txt or .tree newick tree file')

args = parser.parse_args()


#### Testing Toytree


FILE="./"+args.file[0]
print(FILE)
tre = toytree.tree(FILE)
print(tre.ntips)
print(tre.get_tip_labels())

rtre = tre.root(wildcard="nomascus_leucogenys").drop_tips(wildcard="microcebus_murinus").drop_tips(wildcard="macaca_mulatta").drop_tips(wildcard="macaca_nemestrina").drop_tips(wildcard="papio_anubis")


# print(rtre.ntips)
# print(rtre.nnodes)
# print(tre.is_rooted())
# print(rtre.get_tip_labels())
# print(rtre.get_edges())
# print(rtre.get_node_values("support", show_root=1, show_tips=0))

#Assing Sample labels into groups
LABLS=rtre.get_tip_labels()

LABLS_T_CLRS={}

for x in LABLS:
    if ( ('NA' in x) | ('HG' in x)):
        LABLS_T_CLRS[x]=1 #Humans
    if (('pan' in x) | ('Pan' in x)):
        LABLS_T_CLRS[x]=2 #Chimps
    if (('Gori' in x) | ('gori' in x)):
        LABLS_T_CLRS[x]=3 #Gorillas
    if (('Pongo' in x) | ('pongo' in x)):
        LABLS_T_CLRS[x]=4 #Urangotangs
    if bool(re.search(r'MASKED', x, re.IGNORECASE)):
        LABLS_T_CLRS[x]=6 #MASKED SAMPLES :O

for x in LABLS:
    if x not in LABLS_T_CLRS.keys():
        LABLS_T_CLRS[x]=10 # Everything Else






#Match Groups to Colours

# MY_PALETTE=toyplot.color.brewer.palette("Set3") #12 colours
COLOURS_FINAL=[]
# for k in range(0,11): #Use a palette
    # LABLS_T_CLRS_2[k]=MY_PALETTE[k]




#Custom assignment of colours
LABLS_T_CLRS_2={
1:'#DD3734',
2:'#7FDF52',
3:'#53CFDA',
4:'#E88A2B',
5:'#F7F241',
6:'#CB6BF7',
7:'#35EAE8',
8:'#FFA7EA',
9:'#535DF9',
10:'#000000'
} # Avaialable colours


for I in rtre.get_tip_labels():
    COLOURS_FINAL.append(LABLS_T_CLRS_2[LABLS_T_CLRS[I]])

#Node colours
NODE_COLOURS=[toytree.colors[0] for x in rtre.get_node_values("support", show_root=1, show_tips=0)]
counter=0
for J in range(0,len(NODE_COLOURS)):
    if rtre.get_node_values("support", show_root=1, show_tips=0)[J]=='':
        NODE_COLOURS[J]=COLOURS_FINAL[counter]
        counter+=1


Prettier_Nodes=[]
for x in rtre.get_node_values("support", 1, 1):
    if x>=10:
        Prettier_Nodes.append(x)
    else:
        Prettier_Nodes.append('')

Node_shapes=["o" for x in range(rtre.nnodes)]
# for x in range(rtre.nnodes):
    # if rtre.get_node_values("support", show_root=1, show_tips=1)[x]>=0:
        # Node_shapes[x]="r2x1.25"
    # else:
        # Node_shapes[x]="o"




Node_sizes=[]
for x in rtre.get_node_values("support", 1, 1):
    if x <=10:
        Node_sizes.append(2)
    else:
        Node_sizes.append(12)








#https://toytree.readthedocs.io/en/latest/8-styling.html
#### Custom style Dictionary:
mystyle = {
    "layout": 'r',
    "edge_type": 'c',
    "edge_align_style":{ #does nothing if tip align is false
        "stroke": "violet",
        "stroke-width": 1.5,
        "stroke-dasharray": "2,5"    # size of dash, spacing of dashes
    },
    "edge_style": {
        "stroke": toytree.colors[0],
        "stroke-width": 2.5,
    },
    "tip_labels":rtre.get_tip_labels(),  #if we wanna change them
    "tip_labels_align": False,
    "tip_labels_colors": COLOURS_FINAL, #incompatible with "fill":toytree.colors[0],
    "tip_labels_style": {
        "font-size": "8px",
    },
    "node_labels": Prettier_Nodes,
    "node_markers":Node_shapes, #https://toyplot.readthedocs.io/en/stable/markers.html
    "node_colors": NODE_COLOURS,
    "node_style":{
    "stroke": "black",
    "stroke-width": 0.75},
    "node_sizes": [x for x in Node_sizes], #provide a list with length equal to rtre.nnodes
    "node_labels_style":{"font-size":"5pt"},
    "scalebar": True ,
}

# Use
canvas, axes, mark = rtre.draw(**mystyle,width=1000, height=3700);






# canvas, axes, mark = rtre.draw(tree_style='o',width=1000, height=2800);
toyplot.pdf.render(canvas, "tree-plot.pdf")