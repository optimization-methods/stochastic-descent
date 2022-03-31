# import random
#
# import minibatch as minibatch
# import numpy as np
#
# dataset = [[1, 1], [2, 3], [3, 2], [4, 3], [5, 5]]
#
# def ssr_gradient(x, y, b):
#     res = b[0] + b[1] * x - y
#     return res.mean(), (res * x).mean()  # .mean() is a method of np.ndarray
#
#
# def sgd(
#         gradient, x, y, start, learn_rate=0.1, batch_size=1, n_iter=50,
#         tolerance=1e-06, dtype="float64", random_state=None
# ):
#     # Setting up the data type for NumPy arrays
#     dtype_ = np.dtype(dtype)
#
#     # Converting x and y to NumPy arrays
#     x, y = np.array(x, dtype=dtype_), np.array(y, dtype=dtype_)
#     n_obs = x.shape[0]
#     if n_obs != y.shape[0]:
#         raise ValueError("'x' and 'y' lengths do not match")
#     xy = np.c_[x.reshape(n_obs, -1), y.reshape(n_obs, 1)]
#
#     # Initializing the random number generator
#     seed = None if random_state is None else int(random_state)
#     rng = np.random.default_rng(seed=seed)
#
#     # Initializing the values of the variables
#     vector = np.array(start, dtype=dtype_)
#
#     # Setting up and checking the learning rate
#     learn_rate = np.array(learn_rate, dtype=dtype_)
#     if np.any(learn_rate <= 0):
#         raise ValueError("'learn_rate' must be greater than zero")
#
#     # Setting up and checking the size of minibatches
#     batch_size = int(batch_size)
#
#     if not 0 < batch_size <= n_obs:
#         raise ValueError("'batch_size' must be greater than zero and less than or equal to the number of observations")
#
#     # Setting up and checking the maximal number of iterations
#     n_iter = int(n_iter)
#     if n_iter <= 0:
#         raise ValueError("'n_iter' must be greater than zero")
#
#     # Setting up and checking the tolerance
#     tolerance = np.array(tolerance, dtype=dtype_)
#
#     if np.any(tolerance <= 0):
#         raise ValueError("'tolerance' must be greater than zero")
#
#     # Performing the gradient descent loop
#     for _ in range(n_iter):
#         # Shuffle x and y
#         rng.shuffle(xy)
#
#         # Performing minibatch moves
#         for start in range(0, n_obs, batch_size):
#
#             stop = start + batch_size
#             x_batch, y_batch = xy[start:stop, :-1], xy[start:stop, -1:]
#
#             # Recalculating the difference
#             grad = np.array(gradient(x_batch, y_batch, vector), dtype_)
#
#             diff = -learn_rate * grad
#
# def predict(point, coefficients):
#     prediction = coefficients[0]
#     for i in range(len(point) - 1):
#         prediction += coefficients[i + 1] * point[i]
#     return prediction
#
#
# def coefficients_sgd(start, learn_rate, epoch, batch):
#     coefficients = start  # maybe '[start]'?
#     for i in range(1, epoch):
#         w_grad, h_grad = 0, 0
#
#         point_set = random.sample(dataset, batch)
#         for point in point_set:
#             w_grad += (-2) * point[0] * (point[1] - predict(point, coefficients))
#             h_grad += (-2) * (point[1] - predict(point, coefficients))
#         coefficients[0] -= learn_rate * w_grad
#         coefficients[1] -= learn_rate * h_grad
#
#     return coefficients
#
#
# def main(name):
#     coefficients_sgd([0, 1], 0.01, 20, 2)
#
#
# if __name__ == '__main__':
#     main("main.py")
