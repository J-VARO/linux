import sys

sys.path+=['./tulip/lib/python']

from tulip import *
import random

#retourne un tableau qui contient les reactions dont les substrats ne sont produits d'aucune autre reaction
def getFirstReac(graph,reactions):
	
	firstReacs=[]
	
	for reac in reactions:
		
		firstReac=True
		
		for sub in graph.getInNodes(reac):
			for r in graph.getInNodes(sub):
				firstReac=False
				break
				
		if firstReac:
			firstReacs.append(reac)	
		
	return firstReacs
			
def getNextReaction(graph,reaction,reactions):
	
	for prod in graph.getOutNodes(reaction):
		for nextReac in graph.getOutNodes(prod):
			if nextReac in reactions:
				reactions.remove(nextReac)
				return nextReac
			
	
	return 0			
	
def placeMeta(graph,meta,x,y):
	free=True
	
	for node in graph.getNodes():
		if (graph.getProperty('viewLayout').getNodeStringValue(node)==("("+str(x)+","+str(y)+",0)")) and (node != meta):
			free=False
			print "OUI",graph.getStringProperty("viewLabel")[meta],"a cause de ",graph.getStringProperty("viewLabel")[node]
			placeMeta(graph,meta,x,y-20)
			
	if free:
		graph.getLayoutProperty("viewLayout").setNodeStringValue(meta,"("+str(x)+","+str(y)+",0)")

def linearLayout(graph):
	
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLabelRotation =  graph.getDoubleProperty("viewLabelRotation")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")
	
	loop=False
	
	reactions=[]
	#on recupere les noeuds correspondant aux reactions
	for node in graph.getNodes():
		if viewShape[node]==4:
			reactions.append(node)
			
	firstReactions= getFirstReac(graph,reactions)
	if firstReactions==[]:
		print "loop"
		loop=True
	
	
	if(not loop):
		
		random.shuffle(firstReactions)
		
		#on considere que le reseau commence par une des "firstreaction"
		#ordreReaction : tableau  qui contient un chemin du reseau
		ordreReactions=[firstReactions[0]]
		reactions.remove(firstReactions[0])
		
		canContinue = True
		while (canContinue):
			lastReaction = ordreReactions[-1]
			nextReaction=getNextReaction(graph,lastReaction,reactions)
			if nextReaction==0:
				canContinue= False
			
			else:
				ordreReactions.append(nextReaction)
	
	
		#a ce stade on a range que une suite de reactions, si le reseau est plus complexe, il reste des noeuds a placer
	
	
		
		placed=[]
	
		y=50
		x=50
		for reac in ordreReactions:
			viewLayout.setNodeStringValue(reac,"("+str(x)+","+str(y)+",0)")
			
			nbSub=0
			for sub in graph.getInNodes(reac):
				nbSub+=1
				
			nbProd=0
			for prod in graph.getOutNodes(reac):
				nbProd+=1
				
				
			ySub=y+(20*(nbSub-1))
			for sub in graph.getInNodes(reac):
				placeMeta(graph,sub,(x-25),ySub)
				placed.append(sub)
				ySub-=20
				
			yProd=y+(20*(nbProd-1))
			for prod in graph.getOutNodes(reac):
				if (not placed.count(prod)):
					placeMeta(graph,prod,(x+25),yProd)
					placed.append(prod)
				yProd+=20
	
			x+=50


def squareLayout(graph):
	
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLabelRotation =  graph.getDoubleProperty("viewLabelRotation")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")
	
	
	x = 20;
	y = 20;
		
	line=0
	for i in graph.getNodes():
		viewLayout[i]=tlp.Coord(x,y,0)
		x+=50
		line+=1
		if line%15==0:
			y-=50
			x=20
	
