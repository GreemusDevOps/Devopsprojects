# Function to calculate electric field intensity between two point charges
def electric_field(q1, q2, r):
    k = 8.9875e9  # Coulomb's constant in N m^2 / C^2
    # Calculate the magnitude of electric field
    E = k * abs(q1 * q2) / (r ** 2)
    return E


# Main function
def main():
    # Input charges (in Coulombs)
    q1 = float(input("Enter charge q1 (Coulombs): "))
    q2 = float(input("Enter charge q2 (Coulombs): "))

    # Input distance between charges (in meters)
    r = float(input("Enter distance between charges (meters): "))

    # Calculate electric field intensity
    E = electric_field(q1, q2, r)

    # Print the result
    print("Electric field intensity:", E, "N/C")


if __name__ == "__main__":
    main()
