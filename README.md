# Mwanga Backend
Mwanga aims to address delayed milestones in children under 5 years old by providing a comprehensive solution through a mobile app and a dashboard. 
The mobile app enables Community Health Volunteers (CHVs) to register and track cases of delayed development in children,
while the dashboard offers Non-Governmental Organizations (NGOs) a visual tool to analyze this data and allocate resources effectively.
Ultimately, Mwanga aims to enhance the early detection and support of children at risk of delayed milestones, improving their overall development and well-being.
## Technologies Used
- Backend Language: Python v3.9
Visit https://www.python.org/downloads/ to download the latest version of Python 3.
- Web Framework: Django v4.2
- Database: PostgreSQL v14.9
 Visit https://www.postgresql.org/download/ to download PostgreSQL

## Key Features

## CHV Registration
The backend enables the registration of Community Health Volunteers.

## Developmental Milestone tracking
The backend includes criteria for enabling milestone registration and tracking.

## Dashboard Integration
 The backend integrates with the Mwanga Dashboard, providing data and insights that help visualize the areas with high numbers of delayed milestones.


## Getting Started
1.  Navigate to this repository
   - git clone https://github.com/akirachix/Qemer-backend.git
2. Navigate into the directory
`` 
cd Qemer-backend
``
3. Create the virtual environment by running this command
``
python3 -m venv myenv
``
 4. Activate the virtual environment
`` source myenv/bin/activate
``
 5. To install Django dependencies into the virtual environment run
``pip install requirements.txt
``

6.  Make migrations in order to enable new changes to the database
  ``python3 manage.py makemigrations `` to make the migrations
  ``python3 manage.py migrate `` to configure the migrations
7. Start the backend server using
`` 
python3 manage.py runserver
``

## Usage

## CHV Registration
The CHV Registration feature allows you to onboard Community Health Volunteers. To utilize this feature:

- Navigate to the CHV Registration section in the system.
- Click on the "Register New CHV" button.
- Fill in the required information for the new CHV, such as their name, contact details, and training history.
- Save the information to complete the registration process.
- This feature helps you maintain an up-to-date database of CHVs, ensuring a well-organized and efficient workforce.

## Developmental Milestone Tracking
Enables milestone registration and tracking, and monitors assigned CHVs in meeting registration of new cases. To get started with milestone tracking:

- Access the Developmental Milestone Tracking section.
- Select a specific CHV whose milestones cases you want to track.
- Enter the relevant milestone information, such as completion dates and objectives achieved.
- Save the milestone data.

## Dashboard Integration
Our system seamlessly integrates with the Mwanga Dashboard, providing valuable data and insights that help visualize areas with high numbers of delayed milestones. To make the most of this integration:

- Log in to the Mwanga Dashboard.
- Access the "CHV Milestone Insights" or a similar section within the dashboard.
- Explore the visualizations and reports that showcase delayed milestones across different parts of the region.
- Utilize this data to make informed decisions, allocate resources efficiently, and support CHVs in areas with high number of cases.
- The integration with the Mwanga Dashboard empowers you with real-time information to improve CHV management and enhance community healthcare.
