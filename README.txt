Luther catalog - Django starter (MVP) with sample data seeder
-----------------------------------------------------------
Quick start (Windows):

1. Extract the folder 'luther_starter' to a local path (e.g. Desktop).

2. Open PowerShell in that folder.

3. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Make migrations and migrate:
   python manage.py makemigrations
   python manage.py migrate

6. Create a superuser:
   python manage.py createsuperuser

7. Seed sample data (creates sucursales, productos and inventarios):
   python manage.py seed_data

8. Run the development server:
   python manage.py runserver
   Open http://127.0.0.1:8000/ (catalog)
   Open http://127.0.0.1:8000/admin/ (admin)
