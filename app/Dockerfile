FROM python:3.10-slim 

  WORKDIR /app 
 		
   COPY . . 

RUN pip install requests redis 

 	 CMD ["python","parser.py"] 
