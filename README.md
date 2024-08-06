# Url Tool

**Url Tool** is a Django-based web application designed to provide efficient URL shortening capabilities while demonstrating best practices in web development. The project integrates robust backend processing with a responsive frontend design to deliver a functional and user-friendly URL shortening tool.

## Project Overview

**Url Tool** leverages Django's powerful framework and integrates seamlessly with HTML, CSS, JavaScript, and AJAX to deliver the following features:

- **URL Shortening Functionality:** Converts lengthy URLs into shortened links with a single click using Django's models and views.
- **Copy Feature:** Includes a JavaScript-driven copy feature to easily copy shortened URLs to the clipboard for convenient sharing.
- **Shared History Section:** Displays the most recent 99 shortened URLs using Django's database management, providing transparency and collaborative data visibility.
- **URL Check Feature:** Integrates with the VirusTotal API to check whether URLs are harmful, malicious, or involve redirects, enhancing the reliability and trustworthiness of shortened URLs.

## Technical Implementation

- **Backend with Django:** Efficiently manages database entries through Django's ORM (Object-Relational Mapping) to ensure rapid data access and storage management.
- **Frontend Design:** Utilizes HTML5, CSS3, and JavaScript for a responsive and intuitive user interface. JavaScript enhances interactivity, and AJAX enables asynchronous data retrieval and interaction without refreshing the page.

## Project Goals

- **Django Framework:** Demonstrates the use of Django for web application development, showcasing scalable and secure applications while maintaining code efficiency.
- **Frontend Integration:** Emphasizes user-centric design principles and responsive web development practices through integration with HTML, CSS, JavaScript, and AJAX.
- **Security Practices:** Highlights the importance of proactive security measures with the URL Check feature to ensure user safety and data integrity.

## Installation and Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/kushal1o1/url_tool.git
    cd url-tool
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Database Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application at** `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
