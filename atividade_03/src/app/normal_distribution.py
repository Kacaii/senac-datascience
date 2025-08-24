import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import polars as pl

# ▒▒ Columns:

# Student_Name: Anonymized student name.
# College_Name: College attended.
# Stream: Academic discipline (e.g., Engineering, Arts).
# Year_of_Study: Year of study (1–4).
# AI_Tools_Used: Tools used (e.g., ChatGPT, Gemini).
# Daily_Usage_Hours: Hours spent daily on AI tools.
# Use_Cases: Purposes (e.g., Assignments, Exam Prep).
# Trust_in_AI_Tools: Trust level (1–5).
# Impact_on_Grades: Grade impact (-3 to +3).
# Do_Professors_Allow_Use: Professor approval (Yes/No).
# Preferred_AI_Tool: Preferred tool.
# Awareness_Level: AI awareness (1–10).
# Willing_to_Pay_for_Access: Willingness to pay (Yes/No).
# State: Indian state.
# Device_Used: Device (e.g., Laptop, Mobile).
# Internet_Access: Access quality (Poor/Medium/High)


def main():
    df = pl.scan_csv("src/students.csv")

    # 󰓫  Dataframes ------------------------------------------------------------
    mean_val = df.select(pl.col("Daily_Usage_Hours")).mean().collect().item()
    std_val = df.select(pl.col("Daily_Usage_Hours")).std(ddof=1).collect().item()

    # 󰄨  Values ----------------------------------------------------------------
    linear_spacing = np.linspace(
        mean_val - 4 * std_val,
        mean_val + 4 * std_val,
        1000,
    )
    density = norm.pdf(linear_spacing, mean_val, std_val)

    # 󰹉  Building the plot -----------------------------------------------------
    plt.plot(linear_spacing, density)
    plt.xlabel("Values")
    plt.ylabel("Density")
    plt.title("Normal Distribution: Daily AI Usage in hours")

    # 
    plt.show()


if __name__ == "__main__":
    main()
