## quickstart guide
to run application in fastest and easiest manner:
1. clone repository
2. in main directory (djangoapp) run following code `docker build -t djangoapp:latest .`
3. run `docker run -p 8000:8000 djangoapp:latest`

### further configuration
to add new super user, paste this command into your terminal `docker exec -it <container_id_or_name> bash`
from there process is same as in normal django project