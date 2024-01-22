def avg_loss(spendings, sales, w, b):
  N = len(spendings)
  total_error = 0.0

  for i in range(N):
    totatl_error += (sales[i] - (w * spendings[i] + b))**2

  return total_error / float(N)
