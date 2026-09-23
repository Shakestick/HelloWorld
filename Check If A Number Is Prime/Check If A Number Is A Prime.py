import secrets


def is_prime(number: int, rounds: int = 40) -> bool:
	"""Return whether number is prime. Supports integers up to 30 digits."""
	if number < 2:
		return False

	small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
	for prime in small_primes:
		if number == prime:
			return True
		if number % prime == 0:
			return False

	# Write number - 1 as d * 2**s, where d is odd.
	d = number - 1
	s = 0
	while d % 2 == 0:
		s += 1
		d //= 2

	# Miller-Rabin is practical for very large integers; repeated random
	# witnesses make the probability of a false positive negligible.
	for _ in range(rounds):
		witness = secrets.randbelow(number - 3) + 2
		value = pow(witness, d, number)
		if value in (1, number - 1):
			continue

		for _ in range(s - 1):
			value = pow(value, 2, number)
			if value == number - 1:
				break
		else:
			return False

	return True


def main() -> None:
	text = input("Enter an integer (up to 30 digits): ").strip()

	try:
		if text.startswith(("+", "-")):
			digits = text[1:]
		else:
			digits = text

		if not digits.isdigit() or len(digits) > 30:
			raise ValueError

		number = int(text)
	except ValueError:
		print("Please enter a valid integer with at most 30 digits.")
		return

	print(f"{number} is prime." if is_prime(number) else f"{number} is not prime.")


if __name__ == "__main__":
	main()
