## Top N Plants

I've built api using Flask framework in Python and the Google Maps is integrated with React.

APP URL: http://65.1.134.254/

Feature:
- The app can list top **N** number of plants.
- By default top 10 plants data will be marked.
- Filter option on the basis of state.
- Plant info can be seen by clicking the marker in Map.

Configuration:
- **Postgres** Database deployed in **AWS RDS**
- docker is used to containerize both application together.
- Deployed image to an **EC2** instance.

### Installation

``docker-compose -f conf/docker-dev.yml up``

- UI info can be found in `top-plants/client`
- Backend project can be found in `top-plants/server`

### Run app locally

**Flask**
- ``cd top-plants``
- activate the virtual env
- ``pip install -r requirements.txt``
- ```python create_app.py``` // to Run Flask app

**React**
- ``npm install``
- ```npm start```