import pandas as pd
import matplotlib.pyplot as plt

# ─── Load Dataset ───
df = pd.read_csv("students.csv")

print("=== First Few Rows ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Summary Statistics ===")
print(df.describe())

# ─── Create average_marks column ───
df["average_marks"] = df[["math", "science", "programming"]].mean(axis=1)

# ─── Top-performing student ───
top_student = df.loc[df["average_marks"].idxmax()]
print(f"\n=== Top Performing Student ===")
print(top_student[["name", "department", "average_marks"]])

# ─── Group by department ───
dept_avg = df.groupby("department")["average_marks"].mean()
print("\n=== Department-wise Average Marks ===")
print(dept_avg)

# ─── Attendance vs Marks correlation ───
correlation = df["attendance"].corr(df["average_marks"])
print(f"\n=== Correlation between Attendance and Marks: {correlation:.2f} ===")

# ─── Chart 1: Bar chart – Student Average Marks ───
plt.figure(figsize=(10, 5))
plt.bar(df["name"], df["average_marks"], color="steelblue")
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart_student_avg.png")
plt.close()

# ─── Chart 2: Column chart – Department Performance ───
plt.figure(figsize=(6, 4))
dept_avg.plot(kind="bar", color=["coral", "mediumseagreen"])
plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_dept_performance.png")
plt.close()

# ─── Chart 3: Scatter plot – Attendance vs Marks ───
plt.figure(figsize=(6, 4))
plt.scatter(df["attendance"], df["average_marks"], color="purple", s=80)
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("chart_attendance_vs_marks.png")
plt.close()

print("\nAll charts saved successfully.")
