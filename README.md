# Efficiency Comparison: Greedy Algorithm vs Dynamic Programming

## 🎯 Objective

Compare two strategies for solving the **coin change problem**:

- **Greedy Algorithm**
- **Dynamic Programming (DP)**

The evaluation is based on execution time for large amounts.

---

## ⚙️ Experiment Setup

Each function was tested **10 times**, and the **average execution time** was measured using Python's `timeit` module.

### Test amounts:

- `amount = 123123`
- `amount = 1231231`

---

## ⏱️ Timing Results

| Amount   | Greedy Time (avg) | DP Time (avg) |
| -------- | ----------------- | ------------- |
| 123      | 0.000002 sec      | 0.000121 sec  |
| 123123   | 0.000004 sec      | 0.157392 sec  |
| 1231231  | 0.000004 sec      | 1.580794 sec  |
| 12312312 | 0.000009 sec      | 15.889064 sec |

---

## 📊 Performance Analysis

### Greedy Algorithm

**Pros:**

- Nearly instant execution, regardless of the amount.
- Simple to implement.
- Highly efficient for coin systems where greedy strategy yields optimal results (e.g., US coins: 1, 5, 10, 25, 50).

**Cons:**

- Does **not always guarantee the optimal coin combination** for arbitrary denominations.

---

### Dynamic Programming

**Pros:**

- Guarantees an **optimal solution** for any coin set.
- Flexible and works well with **non-standard currency systems**.

**Cons:**

- Performance drops significantly as the amount increases.
- Execution time grows **linearly with the amount**, especially noticeable for large values.

---

## 📌 Conclusion

The **Greedy Algorithm** is a great choice for quick computations **if** you are certain that the coin set allows for an optimal result.

**Dynamic Programming** is essential for **non-standard currency systems** or when minimizing the number of coins is critical.

In real-world scenarios, the **greedy approach is often preferred** for its speed, particularly when using standard coin sets (like those in the US or EU). However, if **precision and optimality** are required — such as in financial or logistics applications — it's worth using algorithms that ensure the best possible result, even with higher computational costs.
