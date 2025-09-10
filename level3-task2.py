import pandas as pd


def main():
    # Let's ask the user for a CSV file to load
    path = input("Enter path to your CSV file: ").strip()
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print("Couldn't load the file:", e)
        return

    print("Columns in your data:", list(df.columns))
    print("What kind of plot would you like?")
    print("1. Scatter\n2. Bar\n3. Histogram\n4. Box\n5. Quit")
    import plotly.express as px

    while True:
        choice = input("Pick a number (1-5): ").strip()
        if choice == "1":
            x = input("x-axis column: ").strip()
            y = input("y-axis column: ").strip()
            if x not in df.columns or y not in df.columns:
                print("Invalid column name(s). Available columns:", list(df.columns))
                continue
            try:
                px.scatter(df, x=x, y=y, title=f"{y} vs {x}").show()
            except Exception as e:
                print("Couldn't create scatter plot:", e)
        elif choice == "2":
            x = input("x-axis (category): ").strip()
            y = input("y-axis (value): ").strip()
            if x not in df.columns or y not in df.columns:
                print("Invalid column name(s). Available columns:", list(df.columns))
                continue
            try:
                px.bar(df, x=x, y=y, title=f"{y} by {x}").show()
            except Exception as e:
                print("Couldn't create bar chart:", e)
        elif choice == "3":
            x = input("Column for histogram: ").strip()
            if x not in df.columns:
                print("Invalid column name. Available columns:", list(df.columns))
                continue
            try:
                px.histogram(df, x=x, title=f"Histogram of {x}").show()
            except Exception as e:
                print("Couldn't create histogram:", e)
        elif choice == "4":
            y = input("Column for box plot: ").strip()
            if y not in df.columns:
                print("Invalid column name. Available columns:", list(df.columns))
                continue
            try:
                px.box(df, y=y, title=f"Box plot of {y}").show()
            except Exception as e:
                print("Couldn't create box plot:", e)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()



