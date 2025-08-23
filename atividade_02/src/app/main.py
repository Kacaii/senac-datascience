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

    #   Hypotesis: AI is used more often on fields related to technology. -----
    total_hours_per_field = (
        df.group_by(pl.col("Stream").alias("field"))
        .agg(pl.sum("Daily_Usage_Hours").round(decimals=2).alias("total_hours"))
        .sort("total_hours", descending=True)
    )
    print("   Hypotesis: AI is used more often on fields related to technology")
    print("==> Study fields that use AI tools the most:")
    print(total_hours_per_field.collect().head(5))  #   Confirmed

    #   Hypotesis: AI is used more often at the starting years. ---------------
    yearly_ai_usage = (
        df.group_by(pl.col("Year_of_Study").alias("year"))
        .agg(pl.sum("Daily_Usage_Hours").alias("total_hours_by_year"))
        .sort("year")
    )

    ai_usage_by_period = yearly_ai_usage.with_columns(
        pl.when(pl.col("year") <= 2)
        .then(pl.col("total_hours_by_year").head(2).sum())  # First two years.
        .alias("early_years_total_hours"),
        pl.when(pl.col("year") >= 3)
        .then(pl.col("total_hours_by_year").tail(2).sum())  # Last two years.
        .alias("later_years_total_hours"),
    ).fill_null(strategy="zero")

    print("   Hypotesis: AI is used more often at the early years of college.")
    print("==> Total AI usage per year and period:")
    print(ai_usage_by_period.collect().head(4))


if __name__ == "__main__":
    main()
