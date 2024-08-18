# ****************************************************************************************************
#
# File name: uspoplation.py
# Description:
#       This program shows the midyear population of U.S.A. during the years of 1950 and 1990
#
#
# ****************************************************************************************************

import matplotlib.pyplot as plt


# ****************************************************************************************************

def print_list(nums):
    for i in range(0, len(nums), 10):
        print(nums[i:i + 10])


# ****************************************************************************************************

def calcDifference(population_list):
    change_list = [population_list[i + 1] - population_list[i]
                   for i in range(len(population_list) - 1)]
    return change_list


# ****************************************************************************************************

def getAverage(population_list):
    return sum(population_list) / len(population_list)


# ****************************************************************************************************

def getGreatestIncrease(change_list):
    return max(change_list)


# ****************************************************************************************************

def getSmallestIncrease(change_list):
    return min(change_list)


# ****************************************************************************************************

def plotBar(population_list):
    years = list(range(1950, 1991))
    plt.bar(years, population_list)
    plt.xlabel('Year')
    plt.ylabel('Population (in thousands)')
    plt.title('Population of the United States (1950-1990)')
    plt.show()


# ****************************************************************************************************

def sortAscending(change_list):
    sorted_changes = sorted(change_list)
    print_list(sorted_changes)


# ****************************************************************************************************

def sortDescending(change_list):
    sorted_changes = sorted(change_list, reverse=True)
    print_list(sorted_changes)


# ****************************************************************************************************

def searchPopulation(population_list, population):
    if population in population_list:
        print(f'Population {population} found.')
    else:
        print(f'Population {population} not found.')


# ****************************************************************************************************

def main():
    try:
        with open('USPopulation.txt', 'r') as file:
            population_data = [int(line.strip()) for line in file]
            print('the original list is: ')
            print_list(population_data)

            print('the population changes are:')
            print(calcDifference(population_data))

            average_population = getAverage(population_data)
            print(f'Average population: {average_population:.2f}')

            population_changes = calcDifference(population_data)
            greatest_increase = getGreatestIncrease(population_changes)
            smallest_increase = getSmallestIncrease(population_changes)
            print(f'Year with greatest increase: {population_data[population_changes.index(greatest_increase) + 1]}')
            print(f'Year with smallest increase: {population_data[population_changes.index(smallest_increase) + 1]}')

            plotBar(population_data)

            print('Population sorted in ascending order:')
            sortAscending(population_changes)

            print('Population sorted in descending order:')
            sortDescending(population_changes)

            search_population = int(input('enter a population: '))
            searchPopulation(population_data, search_population)

    except FileNotFoundError:
        print('The file could not be found.')
    except Exception as e:
        print('An error occurred.')
    finally:
        file.close()


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
