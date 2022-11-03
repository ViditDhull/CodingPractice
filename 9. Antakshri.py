file = open("movie_names.txt", "r")
movies = file.readlines()

result = []
result.append('shershaah\n')

for i in result:
    for j in movies:
        if j in result:
            pass
        else:
            if i[-2] == j[0]:
                result.append(j)
                break

print(len(result))
print(result)