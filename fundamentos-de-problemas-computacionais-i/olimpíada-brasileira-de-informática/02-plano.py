def calcular_quota(q_mensal, q_meses, q_gasta):

    return (q_mensal * q_meses) - q_gasta


if __name__ == '__main__':
    quota_mensal = int(input())
    n_meses = int(input())
    quota_gasta = sum(int(input()) for _ in range(n_meses))
    print(calcular_quota(quota_mensal, n_meses + 1, quota_gasta))
