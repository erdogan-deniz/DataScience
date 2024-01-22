def train(spendings, sales, w, b, alpha, epochs):
  for e in range(epochs):
    w, b = update_w_and_b(spendings, sales, w, b, alpha)

    # Вывести информацию о продвижении вперёд
    if e % 400 == 0:
      print("Epoch: ", e, "loss: ", avg_loss(spendings, sales, w, b))

  return w, b
