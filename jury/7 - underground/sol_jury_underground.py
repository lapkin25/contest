from collections import deque

# Решение заимствовано у участника
def sol_underground(N, conditions):
    """
    Находит участников с фиксированной позицией во всех возможных порядках
    """
    if N == 0:
        return []

    # Строим граф
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for a, b in conditions:
        graph[a].append(b)
        in_degree[b] += 1

    def has_multiple_positions(node):
        """
        Проверяет, может ли вершина node находиться на разных позициях
        в разных топологических сортировках
        """
        # Идея: если существует пара вершин (u, v) такая что:
        # - u и v не связаны с node
        # - u и v можно поменять местами с node без нарушения условий
        # то позиция node не фиксирована

        # Находим множество вершин, которые должны быть строго ДО node
        must_be_before = set()
        stack = [node]
        visited = set()
        while stack:
            curr = stack.pop()
            for a, b in conditions:
                if b == curr and a not in visited:
                    must_be_before.add(a)
                    stack.append(a)
                    visited.add(a)

        # Находим множество вершин, которые должны быть строго ПОСЛЕ node
        must_be_after = set()
        stack = [node]
        visited = set()
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    must_be_after.add(neighbor)
                    stack.append(neighbor)
                    visited.add(neighbor)

        # Вершины, которые могут быть как до, так и после node
        flexible_vertices = set(range(1, N + 1)) - must_be_before - must_be_after - {node}

        # Если есть хотя бы одна гибкая вершина, то позиция node может меняться
        return len(flexible_vertices) > 0

    fixed_positions = []
    for node in range(1, N + 1):
        if not has_multiple_positions(node):
            fixed_positions.append(node)

    #print(fixed_positions)

    return fixed_positions


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    N = 3
    pairs = [(1, 2), (2, 3)]
    ans = sol_underground(N, pairs)
    print(f"answer = {ans}")
