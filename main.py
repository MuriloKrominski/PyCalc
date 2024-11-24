import os
from calculator import run_calculator

if __name__ == "__main__":
    run_calculator()

    # Custom pause message to prevent terminal closure
    if os.name == "nt":  # If the operating system is Windows
        input("Calculation complete! Press Enter to exit... Created by Murilo Krominski")
    else:
        input("Calculation complete! Press Enter to exit... Created by Murilo Krominski")

# Author: Murilo Krominski
