def simple_interest(p: float, n: float, r: float) -> tuple[float, float]:
    """
    This function calulates simple interest and amount
    """
    i = (p * n * r) / 100
    a = p + i
    return i, a


def main():
    p = float(input("Principal in INR : "))
    n = float(input("Number of Years : "))
    r = float(input("Rate of interest in %p.a. : "))
    i, a = simple_interest(p, n, r)
    print(f"Simple Interest : {i:.2f} INR")
    print(f"Amount : {a:.2f} INR")


if __name__ == "__main__":
    main()

def main():
    print("Hello from adv-python!")


if __name__ == "__main__":
    main()
