# RepoSeeker

RepoSeeker is a Django web application that integrates with the GitHub API to search for repositories and allows users to save their favorite repositories.

## Installation

1. Clone the repository:
    git clone https://github.com/jithumag/PythonAssessmentSubmissionRepo.git

2. Navigate to the project directory:
    cd reposeeker

3. Create a virtual environment (optional but recommended):
    # Using virtualenv
    virtualenv env

    # Using venv (Python 3)
    python -m venv env

4. Activate the virtual environment:
    # On Windows
    .\env\Scripts\activate

    # On Unix or MacOS
    source env/bin/activate

5. Install the required dependencies using pip:
    pip install -r requirements.txt

6. Apply the database migrations:
    python manage.py migrate

7. (Optional) Create a superuser to access the Django admin panel:
    python manage.py createsuperuser

## Usage

1. Start the Django development server:
    python manage.py runserver

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the home page.

3. Enter a repository name in the search box and click "Search" to search for GitHub repositories.

4. Click on the "Save" button next to a repository to save it to the database.

5. To view saved repositories, navigate to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.