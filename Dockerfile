FROM ubuntu
RUN apt-get update
RUN apt-get install -y nginx vim curl git python3 pip 
RUN pip3 install matplotlib flask numpy app xmlrunner pytest flask_sqlalchemy
RUN git clone https://github.com/mohamad0880218/workflow.git 
#COPY .  ./
#CMD ["echo","Image Created"]
RUN pytest ./Final-Project/testt.py --junitxml=report.xml
RUN mv report.xml ./Final-Project/Artifact/
CMD ["python3","./Final-Project/main.py"]
