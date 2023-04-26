import os

if __name__ == '__main__':
  if os.getenv('JOB_TYPE') == "CONTINUOUS_INTEGRATION" :
    print("Tulsi")
  print("NOT EXECUTE.. :(")