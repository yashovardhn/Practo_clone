# DocLink

**DocLink** is a comprehensive healthcare management platform that emulates key features of Practo. Designed to streamline doctor-patient interactions, appointment scheduling, and medical record management, this project leverages Django for robust backend integration and a responsive user interface.

## Features

- **Doctor and Patient Profiles:** Manage detailed profiles for doctors and patients, including medical history and specialization.
- **Appointment Scheduling:** Book, view, and manage appointments between doctors and patients.
- **Medical Records:** Securely store and manage medical records and prescriptions.
- **User Authentication:** Secure login and registration for doctors and patients with role-based access.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS (Bulma)
- **Database:** SQL
- **Tools:** Git, GitHub

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yashovardhn/Practo_clone.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd Practo_clone
    ```

3. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the Application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Dashboard:** Access the admin dashboard at `http://127.0.0.1:8000/admin/` to manage doctors, patients, and appointments.
- **User Interaction:** Sign up as a doctor or patient, and explore the features for scheduling appointments and managing records.

## Contributing

Contributions are welcome! Please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [yashovardhn@gmail.com](mailto:yashovardhn@gmail.com).
