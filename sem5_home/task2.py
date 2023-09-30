names: list[str] = ['Vas', 'Das']
salary: list[int] = [100, 100]
bonus: list[str] = ['10.25%', '5.0%']

a: dict[str, float] = {z[0]: z[1] * float(z[2].strip('%')) / 100 for z in zip(names, salary, bonus)}