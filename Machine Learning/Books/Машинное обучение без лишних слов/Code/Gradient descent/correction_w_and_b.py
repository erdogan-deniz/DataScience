def   update_w_and_b(spendings, sales, w, b, alpha):
  dl_dw = 0.0
  dl_db = 0.0
  N = len(spendings)

  for i in range(N):
    dl_dw += -2 * spendings[i] * (sales[i] - (w * spendings[i] + b))
    dl_db += -2 * (sales[i] - (w * spendings[i] + b))

    # Корректировка w и b
    w -= (1 / float(N)) * dl_dw * alpha
    b -= (1 / float(N)) * dl_db * alpha

    return w, b
