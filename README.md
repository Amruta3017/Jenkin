# Automation Framework
This is a framework for automating test cases for MNF products

<b>Author</b>: <span style="color: red">Prikshit Pundir</span>
<br>
<b>URL</b>: https://github.com/Salts-Spray/MNF_Automation.git

## Code
The repository contains code for automating test cases. The framework includes the following folders:

## Project Description
The project is a sophisticated testing framework developed in the PyCharm IDE, combining both Behavior-Driven Development (BDD) and Test-Driven Development (TDD) methodologies. This Hybrid framework is designed to facilitate efficient and comprehensive testing of applications. The framework comprises seven essential directories, each serving a distinct purpose:
<br>
1. Configurations
<ul>
This directory hosts a 'config.ini' file. The file centralizes essential configuration parameters such as the base URL, email, and password. This streamlines the management of these parameters across various tests.
</ul>

2. Logs
<ul>
The 'Logs' directory is home to the 'automation.log' file. This file serves as a repository for all logs generated during the testing process. It ensures that logs are well-organized and accessible for debugging and auditing purposes.
</ul>

3. PageObjects:
<ul>
This package is a vital component of the framework. It contains multiple '.py' files, each dedicated to a specific page or component of the application under test. Within each file, you'll find imports, classes, locators for relevant elements, and functions to perform actions on these elements. This modular approach promotes maintainability and reusability.
</ul>

4. Reports:
<ul>
The 'Reports' directory stores the outcome of test executions. After each test run, an HTML report is generated and saved in this directory. These reports provide a clear and detailed overview of test results, making it easier to identify issues and track progress.
</ul>

5. Screenshots:
<ul>
All screenshots captured during the testing process are saved in the 'Screenshots' directory. These screenshots are invaluable for visually documenting issues and sharing them with stakeholders for clarity.
</ul>

6. TestCases:
<ul>
This directory hosts Python test scripts organized into separate '.py' files. Each file contains test cases that utilize functions and classes defined in the 'PageObjects' directory. The project leverages the pytest framework for test execution. Additionally, the 'conftest.py' file within this directory centralizes configurations for pytest, enhancing test efficiency and consistency.
</ul>

7. TestData:
<ul>
The 'TestData' directory is reserved for data used in Data-Driven Testing (DDT). Here, an Excel file ('.xlsx') stores datasets that are employed to execute test cases with varying data inputs. This approach enables comprehensive testing and validation of diverse scenarios.
</ul>

8. Utilities:
<ul>
The 'Utilities' package consists of Python files containing common methods and utilities that aid in test automation. This includes loggers for efficient logging, Excel file readers for processing test data, and configuration file readers for managing essential parameters.
</ul>

In summary, this project encapsulates a powerful testing framework that seamlessly integrates BDD and TDD approaches, streamlining test automation. The modular structure of the framework enhances maintainability, readability, and extensibility, making it a robust solution for conducting comprehensive testing on a variety of applications.

## Getting Started
If you'd like to get started with the project, you can follow these steps:

1. Clone the repository:
git clone https://github.com/Salts-Spray/MNF_Automation.git

2. Install the necessary dependencies: pip install -r requirements.txt

3. Execute the test cases: pytest -s -v --html=<path_to_html_file> <path_to_py_file> --browser <browser_name>

## License
This project is licensed under the XYZ License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
You can use this section to acknowledge any third-party libraries or tools you've used in your project.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Issues
If you find any issues or have suggestions, please open a new issue on the repository.

## Support
For any questions or support, please contact [pprikshit24@gmail.com](mailto:pprikshit24@gmail.com).

#   A u t o m a t i o n _ a m r u t a  
 