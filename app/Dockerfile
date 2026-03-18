FROM python:3.10-slim 

  WORKDIR /app 
 		
   COPY . . 

RUN pip install requests redis fastapi uvicorn  

  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"] 
