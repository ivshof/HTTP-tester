#Run Syntax: http-test.py testUrl numberOfRequests max_workers getRequestTimeout
import logging
import sys
import requests
import uuid
from datetime import *
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s')

global numberOfRequests, workerNumber, respTimeDict
respTimeDict = [0]

#Get arguments from command line
testUrl = str(sys.argv[1])
numberOfRequests = int(sys.argv[2])
workerNumber = int(sys.argv[3])
getRequestTimeout = float(sys.argv[4])

logging.info(">>>>> Starting HTTP GET STRESS TEST >>>>>> ")
logging.info("Input parameters: test URL  = %s,  numberOfRequests = %i, workerNumber = %i, getRequestTimeout = %f", testUrl, numberOfRequests, workerNumber, getRequestTimeout)


# Using requests.get to create HTTP request
def download_file(url, file_name):
    try:
        html = requests.get(url, stream=True, timeout=getRequestTimeout)

        # Save obtained data in json file in "results: directory
        open(f'results//{file_name}.json', 'wb').write(html.content)
        logging.debug("response time = " + str(html.elapsed.total_seconds()) + " seconds " + " result = " + str(html.status_code))
        respTimeDict.append(html.elapsed.total_seconds())
        return html.status_code

    except requests.exceptions.RequestException as e:
        respTimeDict.append(getRequestTimeout)
        logging.debug(e)
        return e

def runner():
    global errorCount
    threads = []
    errorCount = 0
    with ThreadPoolExecutor(max_workers=workerNumber) as executor:
        count = 0
        while count < numberOfRequests:
            file_name = uuid.uuid1()
            threads.append(executor.submit(download_file, testUrl, file_name))
            count += 1

        for task in as_completed(threads):
            print(task.result())
            if str(task.result()) != "200":
                errorCount += 1


startTestTime = datetime.now()
runner()

#Logging Test results
logging.info(">>>>>>>>> TEST RESULTS >>>>>>>>>>>>>>> ")
EndTestTime = datetime.now()
TestTime = EndTestTime - startTestTime
logging.info("Total Test Time = %s seconds", TestTime.seconds)
logging.info("Total GET requests = %i", len(respTimeDict)-1)
logging.info("ERROR COUNT =  %i", errorCount)
logging.info("Longest processing time = %f", max(respTimeDict))
logging.info("Average response time= %f", sum(respTimeDict) / (len(respTimeDict)-1))
logging.info("Input parameters: test URL  = %s,  numberOfRequests = %i, workerNumber = %i, getRequestTimeout = %f", testUrl, numberOfRequests, workerNumber, getRequestTimeout)
logging.info("<<<<<<< END TEST <<<<< ")
logging.info("****************")

#Details
#https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#https://creativedata.stream/multi-threading-api-requests-in-python/
