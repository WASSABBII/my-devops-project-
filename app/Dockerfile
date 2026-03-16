FROM python:3.10-slim 

  WORKDIR /app 
 		
   COPY parser.py /app/nur.py 

RUN pip install requests redis 

 	 CMD ["python","nur.py"] 
