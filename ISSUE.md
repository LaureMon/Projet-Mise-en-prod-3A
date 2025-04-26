# ISSUE – CODE REVIEW

### Context
The **Fridge Decoder App** is a web application designed to facilitate the search for cooking recipes based on ingredients available at the user's home.  
The application is structured around three main pages:
- A home page with a tutorial and a login area,
- A search page for keywords or ingredients,
- A page dedicated to recipe details.

Several filters enable searches to be refined according to criteria such as preparation time, culinary origin, or vegetarian option.  
The application is built with a front-end interface developed in **Streamlit** and a back-end in **Flask**, and can be run locally via Python scripts or deployed using a publicly available Docker image.  
The data used comes from two Kaggle datasets. A demo account is also available to explore all functionalities without prior registration.

---

### Reproducibility
The **README** provides detailed instructions for using or deploying the application.  
The necessary links are clearly indicated and easy to use through copy-paste.  
I was able to successfully launch the application locally with Python by following the instructions and was able to navigate through the various pages without any issues.

---

### Best practices implemented

- [x] **Version control (Git)** is properly used with an adapted `.gitignore` file and a collaborative project history.
- [x] **Comprehensive README** explaining the project context, functionalities, installation steps, and usage.
- [x] **Package versioning** through a `requirements.lock.txt` file to ensure environment consistency.
- [x] **Modular architecture** with a main script (`run.sh` or `run.bat`) launching the different application modules.
- [x] **Presence of a LICENSE file** to define the project’s usage rights.
- [x] **Quality control** with a `pyproject.toml` file indicating the use of `pylint` for linting and code standardization.

---

### Project and Code Structure

The project is well structured:
- Each folder follows an explicit and meaningful naming convention.
- Each file is appropriately named and serves a specific purpose.
- The code adheres to community standards, with a modular structure where a main script coordinates the different components.

Although `/src` and `/tests` folders are present, it does not seem that **Cookiecutter** was used (no separate configuration file, no `setup.py`).

---

### Areas for Improvement

To further enhance project organization and maintainability:
- Create a `/Scripts` folder to group together files such as `run.sh` and `run.bat`, clearly separating execution scripts from source code.
- Add a quick guide explaining how to run the tests, not just how to launch the application.
- Consider using a project generator like **Cookiecutter** to further clarify the separation between code, scripts, and tests, and to standardize the structure.
- In the README, add a section specifying system prerequisites, such as:
  - Minimum required Python version (e.g., Python ≥ 3.9),
  - Whether Docker is necessary or optional for deployment.

---

