
def prim(graph):
    length = len(graph)
    
    if (length != len(graph[0])):
		return []
	#endif
	paths = []
	vertex = []
	vertex.append(0)
	actualmin = 0
	maxinf = 0;
	#find the maximum just for convenience
	for y in xrange(0, length):
		for x in xrange(0,y+1):
			if(graph[y][x] > maxinf):
				maxinf = graph[y][x]
			#endif
		#endfor
	#endfor
	maxinf = maxinf + 1
	minx = miny = 0;
	isinpaths = 0;
	for k in xrange(0,length)
		actualmin = maxinf
		for y in vertex:
			for x in xrange(0, length):
				isinpaths = 0
				for j in paths:
					if([y, x] == j or [x, y] == j):
						isinpaths = 1
						break
					#endif
				#endfor
				if(graph[y][x] < actualmin and isinpaths == 0 and graph[y][x] != 0):
					actualmin = graph[y][x]
					minx = x
					miny = y
				#endif
			#endfor
		#endfor
		paths.append([miny,minx])
		vertex.append(minx)
	#endfor
		
    return paths
    
    
    
if __name__ == '__main__':
	graph_list = [	[0, 2, 1, 4, 5, 1],
					[1, 0, 4, 2, 3, 4],
					[2, 1, 0, 1, 2, 4],
					[3, 5, 2, 0, 3, 3],
					[2, 4, 3, 4, 0, 1],
					[3, 4, 7, 3, 1, 0]]
					
	path = prim(graph_list)


