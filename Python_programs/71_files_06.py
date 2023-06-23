for i in range (1,21):
    with open(f'tables/multiplication_table_of_{i}''w',)as f:
        for j in range(1,11):
            f.write(f'{i}x{j}={i}*{j}\n')
        if j!=10:
            f.write('\n')