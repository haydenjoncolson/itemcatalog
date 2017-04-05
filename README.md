# Item Catalog by Hayden Colson

## Overview
This web application provides a list of categories and within each category is a list of items.
Users can login or signup through their Google or Facebook account. Logged in users are allowed access to local permissions like creating, editing, and deleting of their own categories and category items.

## How to Run
Prerequisites: Python, Virtual Box, and Vagrant

1. Locate your vagrant directory
2. Start vagrant and login
```bash
vagrant up
vagrant ssh
```
3. Clone this repository https://github.com/haydenjoncolson/itemcatalog in your vagrant directory
4. Change directories
```bash
cd itemcatalog
```
5. Create the database by running
```python
python database_setup.py
```
6. Populate database (You can skip this step if you want to create first items in database)
```python
python items.py
```
7. Run the application
```python
python itemcatalog.py
```
8. Open your localhost: http://localhost:5000/
