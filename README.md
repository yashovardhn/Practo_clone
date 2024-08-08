<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practo Clone README</title>
</head>
<body>

<h1>Practo Clone</h1>

<p>A Django-based web application that replicates the core functionality of Practo, allowing users to book appointments with doctors, manage patient records, and handle prescription uploads.</p>

<h2>Features</h2>
<ul>
    <li><strong>Doctor & Patient Registration</strong>: Separate registration for doctors and patients with customized fields.</li>
    <li><strong>Doctor Listings</strong>: View and search for doctors by specialization.</li>
    <li><strong>Appointment Management</strong>: Book, view, and manage appointments with doctors.</li>
    <li><strong>Prescription Handling</strong>: Doctors can upload prescriptions; patients can download them.</li>
    <li><strong>User Dashboards</strong>: Personalized dashboards for doctors and patients.</li>
    <li><strong>Rating System</strong>: Patients can rate their appointments.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yashovardhn/Practo_clone.git
cd Practo_clone
</code></pre>
    </li>
    <li>Install dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Apply migrations:
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>Run the development server:
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>Access the application at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</li>
</ol>

<h2>Usage</h2>
<ul>
    <li><strong>Doctor Registration</strong>: Navigate to <code>/register/doctor/</code> to register as a doctor.</li>
    <li><strong>Patient Registration</strong>: Navigate to <code>/register/patient/</code> to register as a patient.</li>
    <li><strong>Login</strong>: Access the login page at <code>/login/</code>.</li>
    <li><strong>Book an Appointment</strong>: Patients can book appointments with doctors from their dashboard.</li>
    <li><strong>Manage Prescriptions</strong>: Doctors can upload prescriptions after appointments, and patients can download them.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
