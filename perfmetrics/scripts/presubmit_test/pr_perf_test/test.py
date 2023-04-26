import os

if __name__ == '__main__':
  print("ENV VARIABLE: ",os.getenv('KOKORO_JOB_TYPE'))
  if os.getenv('KOKORO_JOB_TYPE') == "CONTINUOUS_INTEGRATION" :
    print("Tulsi")
  print("NOT EXECUTE.. :(")