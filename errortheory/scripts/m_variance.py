# 仅考虑总体方差

def m_variance(arr):  # 求方差 variance
    m_var = 0
    m_sum = 0
    m_average = 0
    m_len = len(arr)
    for elem in arr:
        m_sum += elem
    m_average = m_sum/m_len
    for elem in arr:
        m_var += pow(elem-m_average, 2)
    m_var /= m_len
    return m_var


def m_std(arr):  # 求标准差 Standard Deviation
    return pow(m_variance(arr), 0.5)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("方差为")
print(m_variance(arr))

print("标准差为")
print(m_std(arr))
