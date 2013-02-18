import sys
import struct

if64=""
#si c'est une architecture 64 bits (important pour les librairies tulip ...)
if (struct.calcsize("P") * 8)==64:
	
	if64="64"


sys.path+=['./tulip/lib'+if64+'/python']

from tulip import *
from bioinfoLayout import *
from graphToSvg import *

graph=tlp.newGraph()
tlp.initTulipLib("./tulip/lib"+if64+"/tulip")
tlp.loadPlugins()

fileName=sys.argv[1]
layoutAlgo=sys.argv[2]
outName=sys.argv[3]

tulipAlgo=["Random layout","Circular","Balloon (OGDF)","GEM Frick (OGDF)"]

graph=tlp.loadGraph("./tulip/tlp/"+fileName)


#si c'est un algo de tulip
if (tulipAlgo.count(layoutAlgo)):
	graph.computeLayoutProperty(layoutAlgo,graph.getLayoutProperty("viewLayout"))


else:
	if layoutAlgo=="Linear layout":
		linearLayout(graph)
	if layoutAlgo=="Square layout":
		squareLayout(graph)
	

toSVG(graph,"./tulip/svg/"+outName)

