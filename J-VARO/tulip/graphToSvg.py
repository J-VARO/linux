import sys

sys.path+=['./tulip/lib/python','./tulip/pySVG/src/pysvg',r'.\tulip\bin\python',]

from tulip import *
from bioinfoLayout import *
#on importe les fichier de pySVG
for subpackage in ['core', 'filter', 'gradient', 'linking', 'script','shape','structure','style','text','builders','animate']:
	exec 'from '+ subpackage + ' import *'




def toSVG(graph,outName):
	maxX=0
	maxY=0
	minX=0
	minY=0	
	for node in graph.getNodes():
		
		if float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[0]) < minX:
			minX=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[0])
		if float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[0]) > maxX:
			maxX=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[0])
		if float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[1]) < minY:
			minY=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[1])
		if float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[1]) > maxY:
			maxY=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[1])
	
	minX-=50
	minY-=50
	maxY-=(minY-50)
	maxX-=(minX-50)
	
	oh = ShapeBuilder()
	s=svg()
	
	#on ajoute un 'glasspane'
	style_dict = {'fill':"none;pointer-events:fill", 'stroke-width':0}
	myStyle = StyleBuilder(style_dict)
	r = rect(0, 0, maxX+1000, maxY+1000, None, None)
	r.set_style(myStyle.getStyle())
	r.setAttribute("id","glasspane")
	
	
	s.addElement(r)
	#placement des aretes
	for edge in graph.getEdges():
		
		xSource=float(graph.getProperty('viewLayout').getNodeStringValue(graph.source(edge)).replace('(',''.replace(')','')).split(',')[0])
		ySource=float(graph.getProperty('viewLayout').getNodeStringValue(graph.source(edge)).replace('(',''.replace(')','')).split(',')[1])
		xTarget=float(graph.getProperty('viewLayout').getNodeStringValue(graph.target(edge)).replace('(',''.replace(')','')).split(',')[0])
		yTarget=float(graph.getProperty('viewLayout').getNodeStringValue(graph.target(edge)).replace('(',''.replace(')','')).split(',')[1])
		
		color = graph.getColorProperty("viewColor")[edge]
		svgColor="rgb("+str(color[0])+","+str(color[1])+","+str(color[2])+")"
		##
		l = line(xSource-minX, ySource-minY, xTarget-minX, yTarget-minY)
		l.setAttribute("style","stroke:"+svgColor+"; stroke-width:0.5; ")
		l.setAttribute("source",graph.getStringProperty("viewLabel")[graph.source(edge)])
		l.setAttribute("target",graph.getStringProperty("viewLabel")[graph.target(edge)])
		
		
		s.addElement(l)
		
		#~ s.addElement(oh.createLine(xSource-minX, ySource-minY, xTarget-minX, yTarget-minY, strokewidth=0.5, stroke=svgColor))
	
	
	for node in graph.getNodes():
		
		x=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[0])
		y=float(graph.getProperty('viewLayout').getNodeStringValue(node).replace('(',''.replace(')','')).split(',')[1])
		
		size=graph.getSizeProperty("viewSize")[node][0]
		
		shape=graph.getIntegerProperty("viewShape")[node]
		
		color = graph.getColorProperty("viewColor")[node]
		svgColor="rgb("+str(color[0])+","+str(color[1])+","+str(color[2])+")"
		borderColor=graph.getColorProperty("viewBorderColor")[node]
		svgBorderColor="rgb("+str(borderColor[0])+","+str(borderColor[1])+","+str(borderColor[2])+")"
		borderWidth=float(graph.getDoubleProperty("viewBorderWidth")[node])
		#4 => carre
		#2 => cercle
		
		
		if shape==4:
			style_dict = {'fill':svgColor, 'stroke-width':borderWidth, 'stroke':svgBorderColor}
			myStyle = StyleBuilder(style_dict)
			r = rect((x-size/2)-minX, (y-size/2)-minY, size, size, None, None)
			r.set_style(myStyle.getStyle())
			r.setAttribute("id",graph.getStringProperty("viewLabel")[node])
			
			
			s.addElement(r)
			
		if shape==2:
			style_dict = {'fill':svgColor, 'stroke-width':borderWidth, 'stroke':svgBorderColor}
			myStyle = StyleBuilder(style_dict)
			c = circle(x-minX, y-minY,  size/2)
			c.set_style(myStyle.getStyle())
			c.setAttribute("id",graph.getStringProperty("viewLabel")[node])
			
			
			s.addElement(c)
		
			
		fontSize=graph.getIntegerProperty("viewFontSize")[node]
		fontColor=graph.getColorProperty("viewLabelColor")[node]
		svgFontColor="rgb("+str(fontColor[0])+","+str(fontColor[1])+","+str(fontColor[2])+")"
		
		style_dict = {'fill':svgFontColor}
		myStyle = StyleBuilder(style_dict)
		myStyle.setFontSize(5)
		myStyle.setTextAnchor("middle")
		t = text(graph.getStringProperty("viewLabel")[node], x-minX, y-minY)
		t.set_style(myStyle.getStyle())
		t.setAttribute("id",graph.getStringProperty("viewLabel")[node])
		
		s.addElement(t)
	
	s.setAttribute("height",maxY+1000)
	s.setAttribute("width",maxX+1000)
	s.save(outName)
	pass
		
