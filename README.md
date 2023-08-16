# projectmlh (mobile local helper)


set up :

1. fork the repo

2. clone it

3. create your branch

4. python install

5. pip install `sudo apt install python3-pip`

6. install virtual environment : `sudo apt install python3.8-venv`

7. create virtual environment :`python3 -m venv venv`

8. Activate venv :`source venv/bin/activate` in root directory (mlh)

9. **python3 -m pip install Django** (needed or not ? why ?)

10. Django install : `sudo apt install python3-django`

11. Run application : `python3 manage.py runserver`


For any changes after unmerged PR use git revert :

1. git logs

2. git checkout -b revert

3. git revert <your_commit_id>

4. make those changes

5. git add . 

6. git commit -m "message"

7. git push origin revert
