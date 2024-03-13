import random
import math

# Функція для обчислення вартості (кількості конфліктів) розв'язку
def calculate_cost(queens):
    n = len(queens)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j] or abs(i - j) == abs(queens[i] - queens[j]):
                cost += 1
    return cost

# Функція для генерації сусіднього стану (випадкової зміни розв'язку)
def generate_neighbor(queens):
    neighbor = queens[:]
    rand_queen = random.randint(0, len(queens) - 1) # Випадково обираємо королеву
    rand_pos = random.randint(0, len(queens) - 1)   # Випадково обираємо позицію для переміщення королеви
    neighbor[rand_queen] = rand_pos                 # Переміщуємо королеву
    return neighbor

# Функція для виведення розв'язку у вигляді шахової дошки
def print_board(queens):
    n = len(queens)
    for i in range(n):
        for j in range(n):
            if queens[i] == j:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()

# Головна функція алгоритму відпалу
def simulated_annealing(n, initial_temp, cooling_rate, max_iter):
    queens = list(range(n))
    random.shuffle(queens)
    temperature = initial_temp
    current_solution = queens
    current_cost = calculate_cost(current_solution)
    best_cost = current_cost
    best_solution = current_solution[:]
    for _ in range(max_iter):
        neighbor = generate_neighbor(current_solution)
        neighbor_cost = calculate_cost(neighbor)
        cost_diff = neighbor_cost - current_cost
        if cost_diff < 0 or math.exp(-cost_diff / temperature) > random.random():
            current_solution = neighbor
            current_cost = neighbor_cost
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
        temperature *= cooling_rate
    return best_solution

if __name__ == "__main__":
    n = 10  # Розмір дошки
    initial_temp = 1000  # Початкова температура
    cooling_rate = 0.99  # Коефіцієнт охолодження
    max_iter = 10000  # Кількість ітерацій

    solution = simulated_annealing(n, initial_temp, cooling_rate, max_iter)

    print("Solution found with cost", calculate_cost(solution), ":")
    print_board(solution)

