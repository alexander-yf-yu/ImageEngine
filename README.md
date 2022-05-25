# ImageEngine
Image repository project with search functionality and [pytest](https://docs.pytest.org/en/7.1.x/) integrations. Written as a [flask](https://flask.palletsprojects.com/en/2.1.x/) application and containerized with [Docker](https://www.docker.com/get-started/) with lightweight SQLite backend as per [sqlalchemy](https://www.sqlalchemy.org/).

## Features

| Endpoint | Description |
| ----------- | ----------- |
| / | Render all images from the home page along with associated filenames, descriptions, upload dates, or receive subset of images from search call. |
| /upload | Upload a new image with a date, description text. |
| /search | Search the repo according to description text and specify start and end ranges for upload dates. Forward results to be rendered at / |


## User Story

> An initial visit is greeted with empty repo.
<img width="1237" alt="empty" src="https://user-images.githubusercontent.com/33843066/169701795-243b38d2-3042-4a9e-b770-ae30984dee5f.png">

---

> Here a user uploads a ladybug as the first image :)
<img width="1305" alt="ladybird_upload" src="https://user-images.githubusercontent.com/33843066/169701863-b2cdc615-072c-4279-b778-379e994f830a.png">

---

> The repo is subsequently populated by a lone bug
<img width="1238" alt="ladybird_finished" src="https://user-images.githubusercontent.com/33843066/169701899-5f94bc8c-4d82-407a-b7eb-5df86527b884.png">

---

> The user can run a search query that matches the ladybug's description text, but has dates that exclude the publification date
<img width="1287" alt="search" src="https://user-images.githubusercontent.com/33843066/169701932-47f26628-989e-4893-9657-d35724988bd7.png">

---

> A resulting visit to the root route returns an empty return result
<img width="1239" alt="empty_res" src="https://user-images.githubusercontent.com/33843066/169701945-55b02bb8-34de-41dc-9ef5-700ea14c368c.png">

## Requirements
- docker
- git

## Quickstart
Clone this repo
```
git clone https://github.com/alexander-yf-yu/ImageEngine.git
cd ImageEngine
```
Build the image locally and run it with port forwarding (using 8080 as default)
```
docker build -t <image_name> .
docker run -p 8080:8080 image_name
```
You should see gunicorn log output as follows:
```
[2022-05-22 13:46:43 +0000] [8] [INFO] Starting gunicorn 20.1.0
[2022-05-22 13:46:43 +0000] [8] [INFO] Listening at: http://0.0.0.0:8080 (8)
[2022-05-22 13:46:43 +0000] [8] [INFO] Using worker: gthread
[2022-05-22 13:46:43 +0000] [9] [INFO] Booting worker with pid: 9
```
Confirm that it's live with a diagnostic curl request: `curl --head localhost:8080`.
Example response:
```
HTTP/1.1 200 OK
Server: gunicorn
Date: Sun, 22 May 2022 14:18:18 GMT
Connection: keep-alive
Content-Type: text/html; charset=utf-8
Content-Length: 1416
```
## Testing
To test code changes, you can attach to the docker container via shell to execute pytest

First run `docker ps` to get the container_id. For example:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
a588c422c557   image-engine   "/bin/sh -c 'gunicor…"   11 minutes ago   Up 11 minutes   0.0.0.0:8080->8080/tcp   cool_keller
```
Then attach via `docker exec`

```
docker exec -it <container_id> /bin/bash
```
Run the pytest python module with the '-m' option from root directory as `python3 -m pytest`

Example output:
```
root@a588c422c557:/ImageEngine# python3 -m pytest
============================================================ test session starts ============================================================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /ImageEngine
collected 2 items

tests/test_routes.py ..                                                                                                               [100%]

============================================================= 2 passed in 0.19s =============================================================
```

## Sample flask logs
<img width="1427" alt="flask_log" src="https://user-images.githubusercontent.com/33843066/169701838-9c54631a-b44b-42c5-a4a5-fa8fbd29a246.png">

