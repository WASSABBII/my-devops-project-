FROM python:3.10-slim 

  WORKDIR /app 
 		
   COPY parser.py /app/run.py 

RUN pip install requests redis 

 	 CMD ["python","run.py"] 
