data_points = [
    (-2, -3),
    (-1, -1),
    (1, 2),
    (4, 3),
]


def get_y_hat(x):
    return (41 / 42 * x) - (5 / 21)


def get_y_mean(data_points):
    l = len(data_points)
    total = 0
    for point in data_points:
        total += point[1]
    return total / l


def squared_error(y, y_hat):
    return (y - y_hat)**2


def squared_from_y_mean(y, y_mean):
    return (y - y_mean)**2


def get_r_squared(sq_e, sq_m):
    # First find the total percentage of the variation not described by the
    # y_hat slope
    perc_total_var_not = sq_e / sq_m
    # Return 1 minus that
    return 1 - perc_total_var_not


print("")
y_mean = get_y_mean(data_points)
total_sq_e = 0
total_sq_m = 0
for x, y in data_points:
    y_hat = get_y_hat(x)
    sq_e = squared_error(y, y_hat)
    sq_m = squared_from_y_mean(y, y_mean)
    total_sq_e += sq_e
    total_sq_m += sq_m
    print("(", x, y, sq_e, sq_m, ")")

print("\ntotal squared error", total_sq_e)
print("y mean", y_mean)
print("total squared variation", total_sq_m)
print("r^2 is", get_r_squared(total_sq_e, total_sq_m))
print("")
