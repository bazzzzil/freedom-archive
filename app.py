from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Number of entries per page
ENTRIES_PER_PAGE = 100

### TO ADD: FIX DUPLICATES, CROSS-REFERENCE NAMES FOR RELEASED, SHORTEN the table and make it hoverable

@app.route('/')
def index():
    # --- Read the Excel file using pandas ---

    # For Publication
    # data = pd.read_csv('/home/arzto/archive/static/test.csv')

    # For Testing
    data = pd.read_csv('static/test.csv')

# Get the search term from the query parameters
    search_term = request.args.get('search', '', type=str).lower()

    # Filter the data based on the search term
    if search_term:
        # Check if any cell in the row contains the search term
        data = data[data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    # Get the total number of entries after filtering
    total_entries = len(data)

    # Get the current page number from the query parameters (default to 1)
    page = request.args.get('page', 1, type=int)

    # Calculate the start and end indices for slicing the data
    start = (page - 1) * ENTRIES_PER_PAGE
    end = start + ENTRIES_PER_PAGE

    # Slice the data for the current page
    paginated_data = data[start:end]

    # Convert the paginated DataFrame to HTML format
    data_html = paginated_data.to_html(classes='data', header="true", index=False)

    # Calculate total pages
    total_pages = (total_entries + ENTRIES_PER_PAGE - 1) // ENTRIES_PER_PAGE  # Ceiling division

    # Render the index.html template, passing the data and pagination info
    return render_template('index.html', data=data_html, page=page, total_pages=total_pages, search=search_term)

@app.route('/released')
def released():
    # --- Read the Excel file using pandas ---

    # For Publication
    # data = pd.read_csv('/home/arzto/archive/static/released.csv')

    # For Testing
    data = pd.read_csv('static/released.csv')

# Get the search term from the query parameters
    search_term = request.args.get('search', '', type=str).lower()

    # Filter the data based on the search term
    if search_term:
        # Check if any cell in the row contains the search term
        data = data[data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    # Get the total number of entries after filtering
    total_entries = len(data)

    # Get the current page number from the query parameters (default to 1)
    page = request.args.get('page', 1, type=int)

    # Calculate the start and end indices for slicing the data
    start = (page - 1) * ENTRIES_PER_PAGE
    end = start + ENTRIES_PER_PAGE

    # Slice the data for the current page
    paginated_data = data[start:end]

    # Convert the paginated DataFrame to HTML format
    data_html = paginated_data.to_html(classes='data', header="true", index=False)

    # Calculate total pages
    total_pages = (total_entries + ENTRIES_PER_PAGE - 1) // ENTRIES_PER_PAGE  # Ceiling division

    # Render the released.html template, passing the data and pagination info
    return render_template('released.html', data=data_html, page=page, total_pages=total_pages, search=search_term)

if __name__ == '__main__':
    app.run(debug=True)

