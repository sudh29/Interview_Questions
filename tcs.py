import requests
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import matplotlib.pyplot as plt
import sched
import time
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import JSONData  # Import your Django model here

'''
from django.db import models

class JSONData(models.Model):
    json_data = models.JSONField()
'''

#Q1	Download CSV file from XYX endpoint
def download_csv(url):
    """
    Download CSV file from the specified URL.

    Parameters:
        url (str): The URL from which to download the CSV file.
    """
    response = requests.get(url)
    with open('data.csv', 'wb') as f:
        f.write(response.content)


#Q2.Convert the CSV to JSON ( no Pandas library )
def csv_to_json(filename):
    """
    Convert CSV file to JSON format.

    Parameters:
        filename (str): The name of the CSV file.

    Returns:
        list: A list of dictionaries representing the JSON data.
    """
    json_data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            json_data.append(row)
    return json_data

#Q3.Add option to store the JSON data in database using ( any python framework use ORM  )
def store_in_database(json_data):
    """
    Store JSON data in the database using Django ORM.

    Parameters:
        json_data (list): A list of dictionaries representing the JSON data.
    """
    data = JSONData(json_data=json_data)
    data.save()

#Q4.Prepare email and attach the report along with graph and send to particular email group 
def prepare_and_send_email(json_data, graph_image_path, recipient_email):
    """
    Prepare and send email with report and graph attachments.

    Parameters:
        json_data (list): A list of dictionaries representing the JSON data.
        graph_image_path (str): The file path to the graph image.
        recipient_email (list): A list of recipient email addresses.
    """
    msg = MIMEMultipart()
    msg['From'] = 'sender@example.com'
    msg['To'] = ', '.join(recipient_email)
    msg['Subject'] = 'Report with Graph'

    body = 'Please find the attached report and graph.'
    msg.attach(MIMEText(body, 'plain'))

    with open(graph_image_path, 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="jpg")
    attach.add_header('Content-Disposition', 'attachment', filename='graph.jpg')
    msg.attach(attach)

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('sender@example.com', 'password')
    server.sendmail('sender@example.com', recipient_email, msg.as_string())
    server.quit()

def generate_graph(data):
    """
    Generate a graph from the data and save it as an image.

    Parameters:
        data (list): A list of values for the graph.
    """
    plt.plot(data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('graph.jpg')

#Q5.Implement the scheduler to trigger email for every 3 hours once ( no Cron scheduler) 
def send_email_scheduler():
    """
    Main function to execute the email sending process using a scheduler.
    """
    # Download CSV
    download_csv('https://example.com/data.csv')

    # Convert CSV to JSON
    json_data = csv_to_json('data.csv')

    # Store JSON in database
    store_in_database(json_data)

    # Generate and attach graph
    generate_graph([int(row['value']) for row in json_data])
    
    # Prepare and send email
    prepare_and_send_email(json_data, 'graph.jpg', ['recipient1@example.com', 'recipient2@example.com'])

    # Schedule next email in 3 hours
    scheduler.enter(10800, 1, send_email_scheduler)

if __name__ == '__main__':
    # Initialize scheduler
    scheduler = sched.scheduler(time.time, time.sleep)
    
    # Schedule first email
    scheduler.enter(0, 1, send_email_scheduler)
    
    # Start scheduler
    scheduler.run()
