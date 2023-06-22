# Django Portfolio App

This Django Portfolio App allows users to create and manage their portfolio profiles. It includes features such as user authentication, user profile management, and displaying user locations on a map.


## Features

- User Registration: Users can sign up for an account to create their portfolio profiles.
- User Authentication: Registered users can log in to access their profiles.
- User Profile Management: Users can view and edit their profile information, including home address, phone number, and location.
- Interactive Map: The app displays a full-screen map with markers indicating the registered users' locations. Clicking on a marker shows the user's profile information.
- Superuser Access: Superusers have access to the Django admin page for all models.
- User Activity Logging: Login and logout activities are logged and displayed on the admin page.

## Installation

1. Clone the repository:

git clone <repository_url>

2. Create and activate a virtual environment:

python -m venv env
source env/bin/activate

3. Install the dependencies:

pip install -r requirements.txt


4. Apply the database migrations:

python manage.py migrate

5. Start the development server:
python manage.py runserver


6. Access the application in your browser at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. Make sure to follow the project's code style and guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or feedback, please contact (mailto:costa.pimentel@ubi.pt)

