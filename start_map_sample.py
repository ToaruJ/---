#初始地图测试样例
'''
拓展为1，因为初始地图要传输草丛类
坦克数为5
障碍物数为1189
草丛数为375
其他参数参考传输过程测试样例
'''
server_dict = {'info':[1,0,5,0,1396,0,455],   #扩展、winner、坦克数、子弹数、障碍物数、道具数、草丛数

    'tanks':[[1,100,50,0,18,5.32,4.52],[2,100,50,0,0,90.32,90.52],[3,100,50,0,0,5.32,90.52],[4,10,90,0,0,90.32,4.52],[5,100,50,0,0,50.32,40.52]],

    'bulls':[],

    'obs':[[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,5],[2,42],[3,1],[3,5],[3,13],[3,60],[4,1],[4,2],[4,3],
           [4,4],[4,5],[4,34],[4,35],[4,36],[4,37],[4,38],[4,77],[5,27],[5,28],[5,29],[5,30],[5,31],[5,32],
           [5,34],[5,38],[6,27],[6,32],[6,34],[6,35],[6,36],[6,37],[6,38],[6,43],[7,27],[7,32],[7,45],[7,46],
           [7,47],[7,48],[7,49],[7,50],[7,55],[7,56],[7,57],[7,58],[7,59],[7,60],[7,61],[7,62],[8,18],[8,19],
           [8,20],[8,21],[8,27],[8,28],[8,29],[8,30],[8,31],[8,32],[8,45],[8,50],[8,55],[8,62],[8,85],[9,13],
           [9,18],[9,21],[9,45],[9,50],[9,55],[9,62],[10,18],[10,21],[10,45],[10,46],[10,47],[10,48],[10,49],
           [10,50],[10,55],[10,62],[10,69],[10,70],[10,71],[10,72],[10,73],[10,74],[10,75],[10,76],[10,77],
           [10,78],[10,79],[10,80],[10,81],[10,82],[10,94],[11,18],[11,21],[11,55],[11,56],[11,57],[11,58],
           [11,59],[11,60],[11,61],[11,62],[11,69],[11,75],[11,82],[12,18],[12,19],[12,20],[12,21],[12,25],
           [12,69],[12,82],[13,3],[13,5],[13,6],[13,7],[13,8],[13,9],[13,69],[13,82],[14,5],[14,9],[14,37],
           [14,40],[14,41],[14,42],[14,43],[14,44],[14,69],[14,82],[15,5],[15,9],[15,37],[15,40],[15,44],
           [15,69],[15,82],[16,5],[16,9],[16,40],[16,44],[16,47],[16,69],[16,71],[16,82],[17,5],[17,6],
           [17,7],[17,8],[17,9],[17,31],[17,32],[17,33],[17,34],[17,40],[17,44],[17,49],[17,50],[17,51],
           [17,52],[17,53],[17,54],[17,55],[17,69],[17,82],[18,31],[18,34],[18,40],[18,44],[18,49],[18,53],
           [18,55],[18,57],[18,69],[18,82],[18,88],[19,31],[19,34],[19,40],[19,41],[19,42],[19,43],[19,44],
           [19,49],[19,55],[19,69],[19,82],[19,90],[19,91],[19,92],[19,93],[20,22],[20,23],[20,24],[20,25],
           [20,26],[20,27],[20,28],[20,31],[20,34],[20,49],[20,55],[20,68],[20,69],[20,70],[20,71],[20,72],
           [20,73],[20,74],[20,75],[20,76],[20,77],[20,78],[20,79],[20,80],[20,81],[20,82],[20,90],[20,93],
           [21,22],[21,28],[21,31],[21,34],[21,49],[21,55],[21,68],[21,72],[21,90],[21,91],[21,92],[21,93],
           [22,22],[22,28],[22,31],[22,34],[22,49],[22,55],[22,68],[22,69],[22,70],[22,71],[22,72],[23,7],
           [23,22],[23,26],[23,28],[23,31],[23,32],[23,33],[23,34],[23,37],[23,38],[23,49],[23,50],[23,51],
           [23,52],[23,53],[23,54],[23,55],[23,85],[23,86],[23,90],[24,2],[24,22],[24,28],[24,35],[24,36],
           [24,81],[24,82],[24,83],[24,84],[25,22],[25,23],[25,24],[25,25],[25,26],[25,27],[25,28],[25,33],
           [25,34],[25,78],[25,79],[25,80],[26,31],[26,32],[26,45],[26,46],[26,47],[26,48],[26,61],[26,77],
           [27,5],[27,6],[27,7],[27,8],[27,9],[27,29],[27,30],[27,36],[27,37],[27,38],[27,39],[27,40],[27,41],
           [27,45],[27,48],[27,67],[27,68],[27,69],[27,70],[28,5],[28,9],[28,36],[28,41],[28,45],[28,48],
           [28,67],[28,70],[28,84],[29,5],[29,9],[29,10],[29,24],[29,36],[29,41],[29,45],[29,48],[29,67],
           [29,70],[30,5],[30,9],[30,15],[30,16],[30,17],[30,18],[30,36],[30,41],[30,45],[30,47],[30,48],
           [30,49],[30,67],[30,68],[30,69],[30,70],[30,80],[31,5],[31,6],[31,7],[31,8],[31,9],[31,12],
           [31,15],[31,18],[31,21],[31,36],[31,37],[31,38],[31,39],[31,40],[31,41],[31,42],[31,43],
           [31,45],[31,48],[31,52],[31,53],[31,54],[31,55],[31,56],[31,57],[31,58],[31,59],[31,61],
           [31,76],[31,77],[31,78],[31,79],[31,80],[31,81],[31,82],[32,15],[32,18],[32,28],[32,29],
           [32,30],[32,31],[32,32],[32,40],[32,44],[32,45],[32,46],[32,47],[32,48],[32,52],[32,59],
           [32,71],[32,72],[32,76],[32,82],[33,15],[33,18],[33,28],[33,32],[33,39],[33,45],[33,52],
           [33,59],[33,69],[33,70],[33,76],[33,82],[34,15],[34,18],[34,24],[34,28],[34,31],[34,32],
           [34,39],[34,45],[34,52],[34,59],[34,66],[34,67],[34,68],[34,76],[34,82],[35,15],[35,16],
           [35,17],[35,18],[35,22],[35,23],[35,28],[35,32],[35,39],[35,42],[35,45],[35,52],[35,59],
           [35,64],[35,65],[35,76],[35,82],[36,8],[36,9],[36,10],[36,11],[36,20],[36,21],[36,28],[36,32],
           [36,40],[36,44],[36,52],[36,53],[36,54],[36,55],[36,56],[36,57],[36,58],[36,59],[36,63],[36,76],
           [36,77],[36,78],[36,79],[36,80],[36,81],[36,82],[37,8],[37,11],[37,18],[37,19],[37,28],[37,29],
           [37,30],[37,31],[37,32],[37,35],[37,36],[37,37],[37,38],[37,39],[37,40],[37,41],[37,42],[37,43],
           [38,8],[38,11],[38,16],[38,17],[38,65],[38,66],[38,67],[38,68],[38,69],[38,70],[38,71],[39,8],
           [39,9],[39,10],[39,11],[39,19],[39,20],[39,21],[39,22],[39,23],[39,24],[39,25],[39,26],[39,32],
           [39,65],[39,71],[40,19],[40,26],[40,33],[40,65],[40,71],[40,77],[40,78],[40,79],[40,80],[40,81],
           [40,82],[40,83],[40,84],[40,85],[40,90],[41,18],[41,19],[41,26],[41,32],[41,60],[41,65],[41,71],
           [41,77],[41,85],[42,2],[42,19],[42,26],[42,30],[42,31],[42,37],[42,56],[42,57],[42,58],[42,59],
           [42,60],[42,61],[42,62],[42,63],[42,64],[42,65],[42,66],[42,67],[42,68],[42,69],[42,70],[42,71],
           [42,72],[42,73],[42,74],[42,77],[42,85],[43,19],[43,20],[43,21],[43,22],[43,23],[43,24],[43,25],
           [43,26],[43,29],[43,43],[43,44],[43,45],[43,46],[43,47],[43,48],[43,49],[43,50],[43,51],[43,56],
           [43,66],[43,71],[43,75],[43,76],[43,77],[43,85],[44,5],[44,6],[44,7],[44,8],[44,9],[44,10],[44,11],
           [44,12],[44,43],[44,51],[44,56],[44,64],[44,66],[44,70],[44,76],[44,77],[44,85],[45,5],[45,12],
           [45,43],[45,51],[45,56],[45,66],[45,70],[45,76],[45,77],[45,85],[46,5],[46,12],[46,43],[46,44],
           [46,45],[46,46],[46,47],[46,48],[46,49],[46,50],[46,51],[46,56],[46,66],[46,70],[46,76],[46,77],
           [46,78],[46,79],[46,80],[46,81],[46,82],[46,83],[46,84],[46,85],[47,5],[47,12],[47,23],[47,24],
           [47,25],[47,26],[47,27],[47,28],[47,29],[47,30],[47,31],[47,32],[47,33],[47,56],[47,66],[47,71],
           [47,75],[48,5],[48,6],[48,7],[48,8],[48,9],[48,10],[48,11],[48,12],[48,17],[48,23],[48,33],[48,56],
           [48,66],[48,72],[48,73],[48,74],[49,16],[49,23],[49,33],[49,56],[49,57],[49,58],[49,59],[49,60],
           [49,61],[49,62],[49,63],[49,64],[49,65],[49,66],[49,68],[49,91],[50,14],[50,15],[50,23],[50,66],
           [50,84],[50,85],[50,86],[50,87],[50,88],[51,13],[51,23],[51,33],[51,84],[51,88],[52,23],[52,33],
           [52,43],[52,44],[52,45],[52,46],[52,47],[52,48],[52,49],[52,57],[52,58],[52,59],[52,60],[52,61],
           [52,62],[52,63],[52,64],[52,84],[52,88],[52,90],[52,91],[52,92],[53,3],[53,4],[53,5],[53,6],
           [53,23],[53,24],[53,25],[53,26],[53,27],[53,28],[53,29],[53,30],[53,31],[53,33],[53,43],[53,49],
           [53,57],[53,61],[53,64],[53,74],[53,75],[53,76],[53,77],[53,78],[53,79],[53,80],[53,81],[53,82],
           [53,84],[53,88],[53,90],[53,92],[54,3],[54,6],[54,15],[54,16],[54,17],[54,18],[54,19],[54,20],
           [54,21],[54,22],[54,43],[54,49],[54,52],[54,57],[54,64],[54,74],[54,82],[54,84],[54,88],[54,90],
           [54,92],[55,3],[55,6],[55,15],[55,22],[55,43],[55,49],[55,57],[55,64],[55,82],[55,84],[55,85],
           [55,88],[55,90],[55,92],[56,3],[56,6],[56,15],[56,22],[56,24],[56,43],[56,49],[56,57],[56,64],
           [56,82],[56,84],[56,85],[56,86],[56,87],[56,88],[56,90],[56,91],[56,92],[57,3],[57,6],[57,15],
           [57,16],[57,22],[57,38],[57,39],[57,40],[57,41],[57,43],[57,47],[57,48],[57,49],[57,57],[57,64],
           [57,82],[58,3],[58,4],[58,5],[58,6],[58,15],[58,22],[58,27],[58,38],[58,41],[58,57],[58,58],
           [58,59],[58,60],[58,61],[58,62],[58,63],[58,64],[58,75],[58,76],[58,77],[58,78],[58,79],[58,80],
           [58,81],[58,82],[58,84],[59,11],[59,15],[59,22],[59,38],[59,41],[59,43],[59,67],[60,11],[60,15],
           [60,16],[60,17],[60,18],[60,19],[60,20],[60,21],[60,22],[60,38],[60,60],[61,38],[61,63],[62,38],
           [62,48],[62,50],[62,51],[62,52],[62,53],[62,54],[62,55],[63,8],[63,38],[63,39],[63,40],[63,41],
           [63,50],[63,55],[63,92],[64,7],[64,50],[64,55],[64,76],[64,77],[64,78],[64,79],[64,80],[64,81],
           [64,82],[64,83],[64,84],[65,5],[65,6],[65,12],[65,13],[65,14],[65,15],[65,50],[65,55],[65,76],
           [65,84],[66,4],[66,12],[66,15],[66,24],[66,25],[66,26],[66,27],[66,28],[66,29],[66,50],[66,55],
           [66,62],[66,64],[66,65],[66,66],[66,67],[66,68],[66,69],[66,70],[66,76],[66,84],[67,12],[67,15],
           [67,24],[67,29],[67,42],[67,50],[67,55],[67,64],[67,70],[67,72],[67,73],[67,74],[67,76],[67,84],
           [68,12],[68,15],[68,24],[68,29],[68,43],[68,50],[68,51],[68,52],[68,53],[68,54],[68,55],[68,64],
           [68,70],[68,71],[68,75],[68,76],[68,84],[68,86],[69,12],[69,15],[69,24],[69,29],[69,64],[69,70],
           [69,76],[69,84],[70,12],[70,15],[70,21],[70,24],[70,29],[70,43],[70,44],[70,45],[70,46],[70,47],
           [70,48],[70,49],[70,64],[70,65],[70,66],[70,67],[70,68],[70,69],[70,70],[70,72],[70,76],[70,77],
           [70,78],[70,79],[70,80],[70,81],[70,82],[70,83],[70,84],[71,12],[71,15],[71,24],[71,29],[71,43],
           [71,49],[71,70],[71,76],[71,89],[71,90],[72,12],[72,14],[72,15],[72,24],[72,29],[72,43],[72,49],
           [72,71],[72,75],[72,85],[72,86],[72,87],[72,88],[73,12],[73,15],[73,24],[73,29],[73,35],[73,43],
           [73,48],[73,49],[73,72],[73,73],[73,74],[73,82],[73,83],[73,84],[74,12],[74,15],[74,24],[74,25],
           [74,26],[74,27],[74,28],[74,29],[74,43],[74,44],[74,45],[74,46],[74,47],[74,48],[74,49],[74,81],
           [75,4],[75,12],[75,13],[75,14],[75,15],[75,56],[75,85],[76,64],[76,65],[76,66],[76,67],[76,68],
           [76,69],[76,70],[76,71],[76,72],[76,73],[76,94],[77,30],[77,31],[77,32],[77,33],[77,34],[77,35],
           [77,36],[77,37],[77,44],[77,45],[77,64],[77,73],[77,94],[78,30],[78,37],[78,44],[78,45],[78,64],
           [78,73],[78,79],[78,80],[78,81],[78,82],[78,83],[78,84],[78,85],[78,91],[78,94],[79,27],[79,30],
           [79,37],[79,44],[79,45],[79,54],[79,60],[79,64],[79,73],[79,79],[79,85],[79,94],[80,30],[80,37],
           [80,44],[80,45],[80,53],[80,64],[80,73],[80,79],[80,85],[80,94],[81,30],[81,37],[81,44],[81,45],
           [81,51],[81,52],[81,55],[81,56],[81,57],[81,58],[81,59],[81,60],[81,64],[81,65],[81,66],[81,67],
           [81,68],[81,69],[81,70],[81,71],[81,72],[81,73],[81,79],[81,80],[81,85],[81,94],[82,30],[82,37],
           [82,44],[82,45],[82,50],[82,55],[82,60],[82,79],[82,85],[82,94],[83,2],[83,3],[83,4],[83,5],
           [83,6],[83,7],[83,15],[83,16],[83,17],[83,18],[83,19],[83,20],[83,21],[83,22],[83,23],[83,30],
           [83,37],[83,43],[83,44],[83,45],[83,55],[83,60],[83,73],[83,79],[83,80],[83,81],[83,82],[83,83],
           [83,84],[83,85],[83,91],[83,94],[84,2],[84,7],[84,15],[84,23],[84,30],[84,37],[84,55],[84,60],
           [84,94],[85,2],[85,7],[85,15],[85,23],[85,30],[85,31],[85,32],[85,33],[85,34],[85,35],[85,36],
           [85,37],[85,55],[85,60],[85,63],[85,64],[85,65],[85,66],[86,2],[86,7],[86,15],[86,23],[86,55],
           [86,56],[86,57],[86,58],[86,59],[86,60],[86,61],[86,63],[86,66],[86,75],[86,76],[86,77],[86,78],
           [86,79],[87,2],[87,3],[87,4],[87,5],[87,6],[87,7],[87,15],[87,23],[87,40],[87,47],[87,48],[87,49],
           [87,50],[87,51],[87,63],[87,66],[87,75],[87,79],[88,7],[88,15],[88,23],[88,43],[88,44],[88,45],
           [88,46],[88,63],[88,66],[88,75],[88,79],[89,15],[89,16],[89,17],[89,18],[89,19],[89,20],[89,21],
           [89,22],[89,23],[89,27],[89,63],[89,64],[89,65],[89,66],[89,75],[89,76],[89,77],[89,78],[89,79],
           [90,25],[90,37],[91,29],[91,30],[91,31],[91,32],[91,33],[91,34],[91,35],[91,36],[91,37],[91,38],
           [91,39],[91,42],[91,48],[91,50],[91,51],[91,53],[91,55],[91,73],[91,81],[92,29],[92,32],[92,39],
           [92,48],[92,49],[92,50],[92,52],[92,53],[92,54],[92,72],[92,73],[92,74],[92,75],[92,76],[92,77],
           [92,78],[92,79],[92,80],[92,81],[93,29],[93,39],[93,50],[93,52],[93,54],[93,55],[93,61],[93,72],
           [93,81],[94,29],[94,39],[94,43],[94,48],[94,51],[94,55],[94,72],[94,81],[94,89],[94,90],[95,12],
           [95,22],[95,29],[95,39],[95,48],[95,49],[95,53],[95,55],[95,72],[95,73],[95,74],[95,75],[95,76],
           [95,77],[95,78],[95,79],[95,80],[95,81],[96,29],[96,39],[96,48],[96,50],[96,51],[96,53],[96,54],
           [96,55],[96,70],[96,74],[97,29],[97,30],[97,31],[97,32],[97,33],[97,34],[97,35],[97,36],[97,37],
           [97,38],[97,39],[97,49],[97,50],[97,51],[97,53],[98,77]],



    'props':[],

    'safe':[1,1,99,99,1,1,99,99],

    'grass': [[3, 66], [3, 67], [3, 68], [3, 69], [3, 70], [3, 71], [4, 66], [4, 67], [4, 68], [4, 69],
               [4, 70], [4, 71], [5, 66], [5, 67], [5, 68], [5, 69], [5, 70], [5, 71], [6, 66], [6, 67],
               [6, 68], [6, 69], [6, 70], [6, 71], [11, 26], [11, 27], [11, 28], [11, 29], [11, 33], [11, 34],
               [11, 35], [11, 36], [12, 11], [12, 12], [12, 13], [12, 14], [12, 15], [12, 26], [12, 27],
               [12, 28], [12, 29], [12, 33], [12, 34], [12, 35], [12, 36], [13, 11], [13, 12], [13, 13],
               [13, 14], [13, 15], [13, 26], [13, 27], [13, 28], [13, 29], [13, 33], [13, 34], [13, 35],
               [13, 36], [14, 11], [14, 12], [14, 13], [14, 14], [14, 15], [14, 26], [14, 27], [14, 28],
               [14, 29], [14, 72], [14, 73], [14, 74], [14, 75], [14, 76], [14, 77], [15, 26], [15, 27],
               [15, 28], [15, 29], [15, 72], [15, 73], [15, 74], [15, 75], [15, 76], [15, 77], [16, 72],
               [16, 73], [16, 74], [16, 75], [16, 76], [16, 77], [17, 58], [17, 59], [17, 60], [17, 61],
               [17, 72], [17, 73], [17, 74], [17, 75], [17, 76], [17, 77], [18, 58], [18, 59], [18, 60],
               [18, 61], [19, 58], [19, 59], [19, 60], [19, 61], [20, 15], [20, 16], [20, 17], [20, 18],
               [20, 19], [20, 58], [20, 59], [20, 60], [20, 61], [21, 15], [21, 16], [21, 17], [21, 18],
               [21, 19], [21, 58], [21, 59], [21, 60], [21, 61], [22, 15], [22, 16], [22, 17], [22, 18],
               [22, 19], [22, 58], [22, 59], [22, 60], [22, 61], [23, 15], [23, 16], [23, 17], [23, 18],
               [23, 19], [23, 58], [23, 59], [23, 60], [23, 61], [24, 15], [24, 16], [24, 17], [24, 18],
               [24, 19], [24, 58], [24, 59], [24, 60], [24, 61], [37, 44], [37, 45], [37, 46], [37, 47],
               [37, 48], [37, 49], [37, 50], [38, 44], [38, 45], [38, 46], [38, 47], [38, 48], [38, 49],
               [38, 50], [39, 44], [39, 45], [39, 46], [39, 47], [39, 48], [39, 49], [39, 50], [40, 44],
               [40, 45], [40, 46], [40, 47], [40, 48], [40, 49], [40, 50], [43, 34], [43, 35], [43, 36],
               [43, 37], [43, 38], [43, 39], [44, 34], [44, 35], [44, 36], [44, 37], [44, 38], [44, 39],
               [45, 34], [45, 35], [45, 36], [45, 37], [45, 38], [45, 39], [46, 34], [46, 35], [46, 36],
               [46, 37], [46, 38], [46, 39], [47, 34], [47, 35], [47, 36], [47, 37], [47, 38], [47, 39],
               [47, 69], [47, 70], [47, 72], [47, 73], [48, 69], [48, 70], [48, 71], [49, 34], [49, 35],
               [49, 36], [49, 69], [49, 70], [49, 71], [49, 72], [49, 73], [50, 33], [50, 37], [50, 69],
               [50, 70], [50, 71], [50, 72], [50, 73], [51, 32], [51, 38], [51, 69], [51, 70], [51, 71],
               [51, 72], [51, 73], [52, 32], [52, 38], [53, 32], [53, 38], [54, 33], [54, 37], [55, 34],
               [55, 35], [55, 36], [55, 69], [55, 70], [55, 71], [55, 72], [55, 73], [55, 74], [56, 69],
               [56, 70], [56, 71], [56, 72], [56, 73], [56, 74], [57, 44], [57, 45], [57, 46], [57, 69],
               [57, 70], [57, 71], [57, 72], [57, 73], [57, 74], [58, 26], [58, 28], [58, 29], [58, 30],
               [58, 31], [58, 42], [58, 43], [58, 47], [58, 48], [58, 69], [58, 70], [58, 71], [58, 72],
               [58, 73], [58, 74], [59, 26], [59, 27], [59, 28], [59, 29], [59, 30], [59, 31], [59, 42],
               [59, 48], [59, 69], [59, 70], [59, 71], [59, 72], [59, 73], [59, 74], [60, 26], [60, 27],
               [60, 28], [60, 29], [60, 30], [60, 31], [60, 41], [60, 49], [61, 26], [61, 27], [61, 28],
               [61, 29], [61, 30], [61, 31], [61, 41], [61, 49], [61, 58], [61, 59], [61, 60], [61, 61],
               [62, 17], [62, 18], [62, 19], [62, 20], [62, 26], [62, 27], [62, 28], [62, 29], [62, 30],
               [62, 31], [62, 41], [62, 49], [62, 58], [62, 59], [62, 60], [62, 61], [63, 17], [63, 18],
               [63, 19], [63, 20], [63, 26], [63, 27], [63, 28], [63, 29], [63, 30], [63, 31], [63, 42],
               [63, 48], [63, 58], [63, 59], [63, 60], [63, 61], [64, 17], [64, 18], [64, 19], [64, 20],
               [64, 42], [64, 43], [64, 47], [64, 48], [64, 58], [64, 59], [64, 60], [64, 61], [65, 17],
               [65, 18], [65, 19], [65, 20], [65, 44], [65, 45], [65, 46], [65, 58], [65, 59], [65, 60],
               [65, 61], [66, 17], [66, 18], [66, 19], [66, 20], [66, 58], [66, 59], [66, 60], [66, 61],
               [68, 35], [68, 36], [68, 37], [69, 35], [69, 36], [69, 37], [70, 35], [70, 36], [70, 37],
               [71, 35], [71, 36], [71, 37], [71, 54], [71, 55], [71, 56], [71, 57], [71, 58], [71, 59],
               [72, 35], [72, 36], [72, 37], [72, 54], [72, 55], [72, 56], [72, 57], [72, 58], [72, 59],
               [73, 54], [73, 55], [73, 56], [73, 57], [73, 58], [73, 59], [74, 54], [74, 55], [74, 56],
               [74, 57], [74, 58], [74, 59], [75, 18], [75, 19], [75, 20], [75, 21], [75, 22], [75, 54],
               [75, 55], [75, 57], [75, 58], [75, 59], [76, 18], [76, 19], [76, 20], [76, 21], [76, 22],
               [77, 18], [77, 19], [77, 20], [77, 21], [77, 22], [78, 18], [78, 19], [78, 20], [78, 21],
               [78, 22], [79, 18], [79, 19], [79, 20], [79, 21], [79, 22], [80, 18], [80, 19], [80, 20],
               [80, 21], [80, 22]]

               }

