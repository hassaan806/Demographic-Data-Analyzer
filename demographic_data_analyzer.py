import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Advanced education (Bachelors, Masters, Doctorate)
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    
    # 5. Percentage with salary >50K
    higher_education_rich = round((df[higher_education]["salary"] == ">50K").mean() * 100, 1)
    lower_education_rich = round((df[~higher_education]["salary"] == ">50K").mean() * 100, 1)

    # 6. Minimum hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of min-hour workers earning >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    # 8. Country with highest percentage of >50K earners
    country_salary_df = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack()
    highest_earning_country = country_salary_df[">50K"].idxmax()
    highest_earning_country_percentage = round(country_salary_df[">50K"].max() * 100, 1)

    # 9. Most popular occupation in India for >50K earners
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]

    # Print data (for debugging)
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country} ({highest_earning_country_percentage}%)")
        print(f"Top occupations in India: {top_IN_occupation}")

    # Return results in a dictionary
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
