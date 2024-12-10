from rich.table import Table
from rich.console import Console
from io import StringIO
from rich import box


def create_table():
    """
    Create and display a table with user data using the `rich` library.
    Save the table's string representation to a text file.
    """
    # Initialize the console for output
    console = Console()

    # Create a table with a title
    table = Table(title="User Data", box=box.MINIMAL_DOUBLE_HEAD)

    # Add columns to the table with styles and alignment
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Age", justify="right", style="green")

    # Add rows of data to the table
    user_data = [
        ("1", "Alice", "20"),
        ("2", "Bob", "25"),
        ("3", "Charlie", "30"),
    ]

    for user in user_data:
        table.add_row(*user)

    # Print the table to the console
    console.print(table)

    # Save the table's string representation to a file
    file_name = "user_data.txt"
    try:
        # Create a separate buffer and console for saving the table
        with StringIO() as buffer:
            save_console = Console(file=buffer)  # Use a separate Console instance
            save_console.print(table)           # Write the table to the buffer
            with open(file_name, "w") as file:  # Save the buffer content to a file
                file.write(buffer.getvalue())

        console.print(f"Table successfully saved to [green]{file_name}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to save table: {e}[/red]")


if __name__ == "__main__":
    create_table()
