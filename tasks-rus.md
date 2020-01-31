1. Напишите функцию, которая будет валидировать строку на правильную расстановку разных скобок
	Например:
	aa[bb{cc}bb]aa - правильно
	aa[bb{cc]bb}aa - неправильно
	[aa{bb(cc)bb}aa] - правильно
	aabb[cc{bb}aa - неправильно

	Решение:
	Нужно использовать стек. Если находишь открывающую скобку - кладешь ее в стек. Если закрывающую - сравниваешь ее с последним элементом стека, если это соответствующая открывающая скобка, то удаляешь ее из стека.

2. Напишите имплементацию алгоритма binary search

3. Eсть массив генераторов, данные в которых отсортированы по какому-то одному признаку. количество объектов в генераторах разное и рандомное, количество генераторов рандомное. Нужно создать новый генератор, в котором будут все объекты из тех генераторов в отсортированом по тому же признаку порядке. При этом нельзя просто выгрузить объекты в память, а нужно использовать именно преимущества генераторов.

	gen = [g1, g2, g3, ...]


4. Нужно в массиве с положительными и отрицательными чистами найти подмассив с наибольшей суммой чисел. Таким подмассивом может быть и [].
	Например:
	Если l = [−2, 1, −3, 4, −1, 2, 1, −5, 4] то нужно вернуть [4, −1, 2, 1] => 6

	Решение:
	https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

5. Напишите метод, который будет возвращать все ноды на заданной глубине дерева  
		1		| 0  
	   / \  
	  2   3			| 1  
	 / \    \	  
	4   6    8		| 2  
   /   /\   / \  
  5   7  9 10  11		| 3  
  Если глубина 3, то функция должна вернуть [5, 7, 9, 10, 11]  
  На глубине 1 должна вернуть [2, 3]  
	Решение:
	Нужно использовать рекурсию

6. A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b. Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible. Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

	For example, given N = 5, and the following edges:
	edges = [
	    (0, 1, 5),
	    (0, 2, 3),
	    (0, 5, 4),
	    (1, 3, 8),
	    (2, 3, 1),
	    (3, 5, 10),
	    (3, 4, 5)
	]
	You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time

	NOTICE: Есть подозрение, что приведенный пример неправильный

	Решение:
		https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

	Решение, предложенное одним умным человеком:
		nodes = set([edge[0] for edge in edges] + [edge[1] for edge in edges])
		distances={0:0}
		while len(distances) != len(nodes):
		    visited = set(distances.keys())
		    calc_distance = lambda edge: distances[edge[0]] + edge[2]
		    best = min((edge for edge in edges if edge[0] in visited and edge[1] not in visited), key = calc_distance)
		    distances[best[1]] = calc_distance(best)
		print(max(distances.values()))
