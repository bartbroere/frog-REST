FROM proycon/lamachine
COPY server.py .
EXPOSE 5000
CMD python3 -m server
