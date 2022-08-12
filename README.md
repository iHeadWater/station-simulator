# station-simulator

一种从模拟站点和河网图层文件（SHP）中判断站点上下游关系的简单办法。

如果是第一次生成，需要将outdated项改为True，然后将INPUT_NETWORK_FILE_SHP所对应路径改为所需河网线图层所在路径，INPUT_NODE_FILE_SHP所对应路径改为所需站点图层所在路径，注意是相对路径。（如果感觉难以理解，只需要将两个图层文件拖到dfs_path_test.py所在文件夹下，然后将路径改为相应文件名即可）

之后就可以直接运行，等待进程完成，main方法里可以指定相关测试，分别为show_upstream_stations_graph、show_downstream_stations、upstream_node_on_mainstream方法，详情见dfs_path_test.py里的文档注释。

运行完毕后至少会生成5个缓存文件，功效分别为：

up_down_paths.txt：存储所有上下游关系
source_project_points.csv：源站点与河网线上投影点之间关系，加快计算速度，一般不必关注
nearest_line_project_points.csv：河网线上投影点与河网线之间关系，加快计算速度，一般不必关注
network_graph.edgelist：河网线和站点投影点构成的图边表文件，加快计算速度，一般不必关注
origin_graph.edgelist：河网线自己构成的图边表文件，加快计算速度，一般不必关注

如果要换用其他图层文件重新生成上下游关系，应删除所有.csv、.edgelist、.txt缓存文件再将outdated项改为True运行；如果一段时间内只在这些缓存文件上寻找上下游关系，将outdated指定为False并运行相关测试即可。
