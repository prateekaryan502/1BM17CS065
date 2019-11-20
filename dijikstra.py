graph = [[float('inf'), 4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf')],
        [4, float('inf'), 8, float('inf'), float('inf'), float('inf'), float('inf'), 11, float('inf')],
        [float('inf'), 8, float('inf'), 7, float('inf'), 4, float('inf'), float('inf'), 2],
        [float('inf'), float('inf'), 7, float('inf'), 9, 14, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), 9, float('inf'), 10, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), 4, 14, 10, float('inf'), 2, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 1, 6],
        [8, 11, float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), 7],
        [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), 6, 7, float('inf')]
        ]

distance=[0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
visited=[False for i in range(len(distance))]
min=0
index=0
print("vertex   Distance from source")
while(all(visited)!=True):
    for i in range(len(distance)):
        if min>distance[i] and visited[i]==False:
            min=distance[i]
            index=i
    print(index,"   ",min)

    visited[index]=True
    for i in range(len(distance)):
        if graph[index][i]!=float('inf') and visited[i]==False and distance[i]>distance:
            if distance[i]!=float('inf'):
                distance[i]=graph[index][i]
            else:
                distance[i]+=graph[index][i]

